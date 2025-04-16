 {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building...'
                sh 'echo "Build step completed successfully."' // Now succeeds
            }
        }
    }

    post {
        success {
            emailext (
                subject: "\u2705 Build Success: ${env.JOB_NAME} #${env.BUILD_NUMBER}",
                body: """<p>Good news! The build was successful.</p>
                         <p>Job: ${env.JOB_NAME}<br>Build: #${env.BUILD_NUMBER}</p>""",
                to: 'cmvishnubabu08@gmail.com'
            )
        }
        failure {
            emailext (
                subject: "\u274c Build Failed: ${env.JOB_NAME} #${env.BUILD_NUMBER}",
                body: """<p>Oops! The build failed.</p>
                         <p>Job: ${env.JOB_NAME}<br>Build: #${env.BUILD_NUMBER}</p>""",
                to: 'cmvishnubabu08@gmail.com'
            )
        }
    }
}