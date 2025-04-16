pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                echo 'Installing dependencies with pipx...'
                sh 'pipx install -r requirements.txt'  // Using pipx to handle dependencies
            }
        }

        stage('Build') {
            steps {
                echo 'Building...'
            }
        }

        stage('Test') {
            steps {
                echo 'Running tests...'
                script {
                    try {
                        // Run the Flask app with pipx-managed Python
                        sh 'pipx run python3 app.py'  // Using pipx to run app.py
                    } catch (Exception e) {
                        currentBuild.result = 'FAILURE'  // Mark build as FAILURE
                        throw e  // Propagate the error
                    }
                }
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying...'
            }
        }

        stage('Post Actions') {
            steps {
                emailext(
                    subject: "Build failed for ${JOB_NAME}",
                    body: "The build has failed. Please check the logs for more details.",
                    to: "cmvishnubabu08@gmail.com"
                )
            }
        }
    }
}
