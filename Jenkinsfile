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
                        // Run Flask app which will fail due to ZeroDivisionError
                        sh 'python app.py'
                    } catch (Exception e) {
                        currentBuild.result = 'FAILURE'  // Mark the build as failure
                        throw e  // Re-throw the error to propagate the failure
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
