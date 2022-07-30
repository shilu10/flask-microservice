pipeline{
    agent any
    stages{
        stage("Tooling"){
            steps{
                    sh """
                        docker version
                        docker-compose version        
                    """
                }
            }
        stage("Build Stage"){
            steps{
                sh """
                    cd creation_page
                    docker-compose build
                    docker-compose up
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

