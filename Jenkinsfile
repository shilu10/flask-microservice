
pipeline{
    agent any
    stages{
        
        stage("WebUI Test"){
            when{
                branch 'PR-*'
            }
            steps{
                sh"""
                    echo "Started the WEBUI Testing"
                    docker build -t python-img .
                    docker run python-img
                """
            }
        }
       
}
}


