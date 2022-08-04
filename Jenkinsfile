
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
        stage('SonarQube Analysis(SAST)') {
            when {
                branch 'PR-*'
            }
            steps{       
                withSonarQubeEnv("sonarqube_server") {
                    sh "${tool 'SonarScanner'}/bin/sonar-scanner"
                    }
                }        
            }
        
        stage("Source Composition Analysis"){
            when{
                branch 'PR-*'
            }
            steps{
                sh """
                    echo "Started the Dependency Check"
                    wget https://raw.githubusercontent.com/devopssecure/webapp/master/owasp-dependency-check.sh
                    chmod +x owasp-dependency-check.sh
                    cd creation_page
                    bash ../owasp-dependency-check.sh
                    cd ../main_page
                    bash ../owasp-dependency-check.sh
                """
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
                        echo "Starting the Unit, Functionality test cases!!!"
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
                stage("Build"){
                    steps{
                        echo "Started Building the project!!!"
                        sh """
                            cd main_page
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
                            sleep 80s
                            docker exec main_page_backend_1 python3 -m pytest
                        """
                        echo "Test cases ran successfully!!"
                    }
                } 
            }
        }
        stage("Starting React App"){
            when{
                branch "PR-*"
            }
            steps{
                sh"""
                    cd react-frontend
                    docker build -t react-app .
                    docker run react-app &
                """
            }
        }
        stage("Starting the Selenium Grid"){
            when{
                branch 'PR-*'
            }
            steps{
                sh"""
                    echo "starting the selenium standlone browser in docker container"
                    docker --net=host -d --name=chrome run selenium/standalone-chrome 
                    echo "Started the browser successfully"
                """
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
        stage("WebUI Test"){
            sh"""
                echo "Started the Web UI Testing"
                pytest tests/
            """
        }
        stage("Destroying the infra"){
            when{
                branch 'PR-*'
            }
            steps{
                 sh """
                    cd creation_page
                    docker-compose down
                    cd ..
                    cd main_page
                    docker-compose down
                    docker stop react-app
                    docker stop chrome
                    echo "Docker container are successfully down"
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


