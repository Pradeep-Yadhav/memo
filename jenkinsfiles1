pipeline {
    agent any

    stages {
        stage('Hello') {
            steps {
                echo 'Hello World'
            }
        }
        
        stage('Test') {
            steps {
                echo 'Hello World'
            }
        }
        
        stage('Deploy') {
            steps {
                echo 'Hello World'
            }
        }
    
    }
    post{
            always{
                emailext body: 'SUCCESSFULL', subject: 'PIPE LINE STATUS', to: 'jenkinsndocker14@gmail.com'
            }
        }
    
}
