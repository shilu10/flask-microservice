pipeline{
    agent {dockerfile true}
    stages{
	stage("started multibuild"){
    when {
            branch 'PR-*'
        }
	steps{
		echo "started the multibranch"
		}
	}
        stage("Change Directory"){
            steps{
                cd creation_page
            }
        }
	stage("build"){
		steps{
			docker-compose build 
		}
	}
        stage("end step"){
            echo "compeleted successfully"
        }
    }
}
