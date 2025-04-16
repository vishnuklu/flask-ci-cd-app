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
                echo 'Installing dependencies...'
                sh 'pip3 install -r requirements.txt'  // Ensure dependencies are installed
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
                        // Run the Flask app
                        sh 'python3 app.py'  // Run app.py with python3
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
