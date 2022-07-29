pipeline{
    agent {dockerfile true}
    stages{
        stage("Change Directory"){
            steps{
                cd creation_page
            }
        }
	stage("build"){
		docker-compose build .
		docker-compose up
	}
        stage("end step"){
            echo "compeleted successfully"
        }
    }
}
