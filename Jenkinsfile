pipeline {
    agent any  // Use any available agent

    stages {
        stage('Checkout') {
            steps {
                // Pulls the code from your repository
                git branch: 'main', url: 'https://github.com/Pradeep-Yadhav/memo/blob/main/cal.py'
            }
        }

        stage('Run Calculator Program') {
            steps {
                script {
                    // Check the workspace to ensure the cal.py file is there
                    bat 'dir'

                    // Run the cal.py Python script
                    bat 'python cal.py'
                }
            }
        }
    }
}
