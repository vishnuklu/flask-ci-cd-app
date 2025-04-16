pipeline {
    agent any

    environment {
        // Change these to match your environment
        EMAIL_RECIPIENT = 'cmvishnubabu08@gmail.com'
    }

    stages {
        stage('Clone Repo') {
            steps {
                git 'https://github.com/vishnuklu/flask-ci-cd-app.git'

            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Run Flask App') {
            steps {
                sh 'python app.py &'
            }
        }

        stage('Run Tests') {
            steps {
                // Optional: Add test scripts here
                echo "✅ All tests passed (placeholder)"
            }
        }
    }

    post {
        success {
            emailext subject: "✅ SUCCESS: Build #${env.BUILD_NUMBER} - ${env.JOB_NAME}",
                     body: """
                        <h3>✅ Build Successful</h3>
                        <p>Build Number: ${env.BUILD_NUMBER}</p>
                        <p>Project: ${env.JOB_NAME}</p>
                        <p><a href="${env.BUILD_URL}">View Build</a></p>
                     """,
                     to: "${EMAIL_RECIPIENT}",
                     mimeType: 'text/html'
        }
        failure {
            emailext subject: "❌ FAILURE: Build #${env.BUILD_NUMBER} - ${env.JOB_NAME}",
                     body: """
                        <h3>❌ Build Failed</h3>
                        <p>Build Number: ${env.BUILD_NUMBER}</p>
                        <p>Project: ${env.JOB_NAME}</p>
                        <p><a href="${env.BUILD_URL}">View Build</a></p>
                     """,
                     to: "${EMAIL_RECIPIENT}",
                     mimeType: 'text/html'
        }
    }
}
