pipeline {
    agent any  // Use any available agent

    stages {
        stage('Checkout') {
            steps {
                // Pulls the code from your repository (the correct repo URL)
                git branch: 'main', url: 'https://github.com/Pradeep-Yadhav/memo.git'
            }
        }

        stage('Run Calculator Program') {
            steps {
                script {
                    // Check the workspace to ensure the cal.py file is there (Linux)
                    sh 'ls -l'

                    // Run the calculator Python script (for Linux)
                    sh 'python3 cal.py'
                }
            }
        }
    }
}
