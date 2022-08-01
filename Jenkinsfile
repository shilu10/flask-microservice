
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
            when {
                branch 'PR-*'
            }
            steps{       
                withSonarQubeEnv("sonarqube_server") {
                    sh "${tool 'SonarScanner'}/bin/sonar-scanner"
                    }
                }        
            }
		
        stage ("Building and Testing Stages of Creation Page Microservice!!"){
            when {
                branch 'PR-*'
            }
            parallel{
                stage("Build"){
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
                stage("Test"){
                    steps{
                        echo "Starting the Unit and Functionality test cases!!!"
                        sh  """
                            sleep 80
                            docker exec creation_page_backend1_1 python3 -m pytest
                        """
                        echo "Test Cases ran Successfully!!"
                        sh """
                            cd creation_page
                            docker-compose down
                        """
                    }
                }  
            }
        }

        stage ("Building and Testing Stages of Main Page Microservice!!"){
            when {
                branch 'PR-*'
            }
            parallel{
                stage("Build"){
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
                stage("Test"){
                    steps{
                        echo "Starting the Unit and Functionality test cases!!!"
                        sh  """
                            sleep 250s
                            docker exec main_page_backend_1 python3 -m pytest
                        """
                        echo "Test cases ran successfully!!"
                        sh """
                            cd main_page
                            docker-compose down
                        """
                    }
                } 
            }
        }
        stage ("Container image scanning"){
            when {
                branch 'PR-*'
            }
            steps{
                sh """
                    echo "Started the image scanning and writing to the files"
                    trivy image main_page_backend --severity=HIGH,CRITICAL > main_page_backend.txt
                    trivy image main_page_queue --severity=HIGH,CRITICAL > main_page_queue.txt
                    trivy image creation_page_queue1 --severity=HIGH,CRITICAL > creation_page_queue1.txt
                    trivy image creation_page_backend1 --severity=HIGH,CRITICAL > creation_page_backend1.txt
                    trivy image mysql --severity=HIGH,CRITICAL > mysql.txt
                    trivy image mysql:5.7.39 --severity=HIGH,CRITICAL > mysql:5.7.39.txt
                    echo "Ended the image Scanning process successfully"
                """
            }
        }
    }
    post {
        always {
            echo 'The pipeline completed'
             always {
                junit 'build/reports/**/*.xml'
            }
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

