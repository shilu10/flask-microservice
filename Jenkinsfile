
pipeline{
    agent any
    stages{
        stage("Tooling"){
            when {
                branch 'PR-*'
            }
            steps{
                echo "Tooling versions: "
                sh """
                    docker version
                    docker-compose version        
                 """
                }
            }
        stage('SonarQube Analysis') {
                steps{       
                    withSonarQubeEnv("SonarScanner") {
                    sh "${tool 'SonarScanner'}/bin/sonar-scanner"
                    }
                }
           
            
        }
		
        stage ("Building and Testing Stages of Creation Page Microservice!!"){
            when {
                branch 'PR-*'
            }
            parallel{
                stage("Build Stage"){
                    steps{
                        echo "Started Building the project!!!"
                        sh """
                            cd creation_page
                            docker-compose build
                            docker-compose up &
                            sleep 100
                        """
                        echo "Build is Successful"
                    }
                }
                stage("Testing Stage"){
                    steps{
                        echo "Starting the Unit and Functionality test cases!!!"
                        sh  """
                            sleep 80
                            docker exec creation_page_backend1_1 python3 -m pytest
                        """
                        echo "Test Cases ran Successfully!!"
                    }
                }  
            }
        }

        stage ("Building and Testing Stages of Main Page Microservice!!"){
            when {
                branch 'PR-*'
            }
            parallel{
                stage("Build Stage"){
                    steps{
                        echo "Started Building the project!!!"
                        sh """
                            cd main_page
                            docker-compose build
                            docker-compose up &
                            sleep 250
                        """
                        echo "Build is Successful"
                    }
                }
                stage("Testing Stage"){
                    steps{
                        echo "Starting the Unit and Functionality test cases!!!"
                        sh  """
                            sleep 250s
                            docker exec main_page_backend_1 python3 -m pytest
                        """
                        echo "Test cases ran successfully!!"
                    }
                }  
            }
        }
    }
    post {
        always {
            echo 'The pipeline completed'
        }
        success {                   
            echo "Building and Testing of the application is successfull"
        }
        failure {
            echo 'Build stage failed'
            error('Stopping early…')
        }
      }

}

