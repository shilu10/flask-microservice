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
            echo "changed the directory successfully"
            }
        }
	stage("build"){
		steps{
			echo "Running the build for "
		}
	}
    stage("end step"){
        steps{
            echo "compeleted successfully"
        }
    }
}
}
