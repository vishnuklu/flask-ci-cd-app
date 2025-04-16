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
                echo 'Installing dependencies globally...'
                script {
                    // Install dependencies globally using pip3
                    sh 'pip3 install -r requirements.txt'
                }
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
                        // Run the Flask app using the global Python
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
