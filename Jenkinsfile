pipeline{
    agent {dockerfile true}
    stages{
        stage("Change Directory"){
            steps{
                cd creation_page
            }
        }
	stage("build"){
		stes{
			docker-compose build .
		}
	}
        stage("end step"){
            echo "compeleted successfully"
        }
    }
}
