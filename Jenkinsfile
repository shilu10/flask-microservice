pipeline{
    agent any
    stages{
        stage("Tooling"){
            steps{
                echo "Tooling versions: "
                sh """
                    docker version
                    docker-compose version        
                 """
                }
            }
        stage ("Build and Testing Stage!!"){
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
                        echo "Starting the test cases!!!"
                        sh  """
                            sleep 20
                            docker exec -it creation_page_backend1_1 pytest
                        """
                        echo "Ended the test cases"
                    }
                }  
            }
        }
        
        stage("End Stage"){
            steps{
                echo "compeleted successfully and ended"
            }
        }
}
}

