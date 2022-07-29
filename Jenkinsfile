pipeline{
    agent {dockerfile true}
    stages{
        stage("Change Directory"){
            steps{
                cd creation_page
            }
        }
	stage("build"){
		step{
			docker-compose build .
		}
	}
        stage("end step"){
            echo "compeleted successfully"
        }
    }
}
