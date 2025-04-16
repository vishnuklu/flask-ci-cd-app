pipeline {
    agent any

    environment {
        EMAIL_RECIPIENT = 'cmvishnubabu08@gmail.com'
    }

    stages {
        stage('Clone Repo') {
            steps {
                git 'https://github.com/vishnuklu/flask-ci-cd-app.git'
            }
        }

        stage('Set Up Virtualenv and Install Requirements') {
            steps {
                script {
                    sh 'python3 -m venv venv'
                    sh './venv/bin/pip install -r requirements.txt'
                }
            }
        }

        stage('Run Flask App') {
            steps {
                sh './venv/bin/python app.py &'
                sleep 5 // wait for server to start
            }
        }

        stage('Tests') {
            steps {
                echo "✅ Test placeholder"
            }
        }
    }

    post {
        success {
            emailext(
                subject: "✅ SUCCESS: Build #${env.BUILD_NUMBER}",
                body: """
                    <h2>✅ Build Successful</h2>
                    <p><b>Job:</b> ${env.JOB_NAME}</p>
                    <p><b>Build #:</b> ${env.BUILD_NUMBER}</p>
                    <p><b>URL:</b> <a href="${env.BUILD_URL}">${env.BUILD_URL}</a></p>
                """,
                to: "${EMAIL_RECIPIENT}",
                mimeType: 'text/html'
            )
        }

        failure {
            emailext(
                subject: "❌ FAILED: Build #${env.BUILD_NUMBER}",
                body: """
                    <h2>❌ Build Failed</h2>
                    <p><b>Job:</b> ${env.JOB_NAME}</p>
                    <p><b>Build #:</b> ${env.BUILD_NUMBER}</p>
                    <p><b>URL:</b> <a href="${env.BUILD_URL}">${env.BUILD_URL}</a></p>
                """,
                to: "${EMAIL_RECIPIENT}",
                mimeType: 'text/html'
            )
        }
    }
}
