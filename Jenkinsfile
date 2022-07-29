pipeline{
    agent {dockerfile true}
    stages{
        stage("build"){
            steps{
                cd creation_page
                docker-compose build
                docker-compose up
            }
        }
        stage("end"){
            echo "compeleted successfully"
        }
    }
}