pipeline{
    agent any
    stages{
        stage("Tooling"){
            steps{
                echo "Tooling versions: "
                sh """
                    docker version
                    docker-compose version  
                    cd creation_page      
                 """
                }
            }
        stage("Build Stage"){
            steps{
                echo "Started Building the project!!!"
                sh """
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
                    docker exec -it creation_page_backend1_1 pytest
                """
            }
        }  
        stage("End Stage"){
            steps{
                echo "compeleted successfully and ended"
            }
        }
}
}

