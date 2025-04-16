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
                echo 'Setting up virtual environment and installing dependencies...'
                // Create a virtual environment in the workspace
                sh 'python3 -m venv venv'
                // Activate the virtual environment and install dependencies
                sh './venv/bin/pip install -r requirements.txt'
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
                        // Run the Flask app using the virtual environment's Python
                        sh './venv/bin/python app.py'  // Run app.py with virtual environment's python
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
