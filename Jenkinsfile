pipeline {
    agent any 

    stages {
        stage('Clone Repository') {
            steps {
                // Clone your GitHub repository
                git 'https://github.com/username/repo-name.git' // Replace with your repository URL
            }
        }
        
        stage('Count Files') {
            steps {
                script {
                    // Execute a shell command to count files
                    def fileCount = sh(script: 'find . -type f | wc -l', returnStdout: true).trim()
                    echo "Number of files in the repository: ${fileCount}"
                }
            }
        }
    }
}
