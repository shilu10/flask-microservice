pipeline{
    agent any
    stages{
        stage("Tooling"){
            steps{
                    sh"""
                        docker version
                        docker-compose version        
                    """
                }
            }
        stage("Build"){
            steps{
                sh """
                    cd creation_page
                    docker-compose build
                    docker-compose up
                """
            }
       
        stage("end step"){
            steps{
                echo "compeleted successfully and ended"
            }
        }
}
}
}
