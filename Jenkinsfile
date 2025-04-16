pipeline {
    agent any

    stages {
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
                        sh 'python3 app.py'  // Make sure the Python3 command is used
                    } catch (Exception e) {
                        // Mark the build as FAILURE if an exception occurs
                        currentBuild.result = 'FAILURE'  // Set build result to FAILURE
                        throw e  // Propagate the error to Jenkins to fail the build
                    }
                }
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying...'
            }
        }
    }

    post {
        success {
            emailext to: 'cmvishnubabu08@gmail.com',
                subject: "Build Success: ${env.JOB_NAME} [${env.BUILD_NUMBER}]",
                body: "Good news! Build was successful."
        }
        failure {
            emailext to: 'cmvishnubabu08@gmail.com',
                subject: "Build Failed: ${env.JOB_NAME} [${env.BUILD_NUMBER}]",
                body: "Unfortunately, the build failed due to an error in the application. Please check the console output for details."
        }
    }
}
