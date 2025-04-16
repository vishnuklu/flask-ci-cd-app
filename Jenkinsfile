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
                        // Attempt to run the Flask app using python3
                        sh 'python3 app.py'
                    } catch (Exception e) {
                        // Mark the build as failure and send failure email
                        currentBuild.result = 'FAILURE'  // Set build result as FAILURE
                        throw e  // Propagate the error to Jenkins
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
                body: "Unfortunately, the build failed. Please check the console output."
        }
    }
}
