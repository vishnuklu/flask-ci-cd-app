post {
    success {
        echo 'Build succeeded!'
        emailext (
            subject: "Build Successful: ${env.JOB_NAME} #${env.BUILD_NUMBER}",
            body: "Good job! The build succeeded.\nCheck it here: ${env.BUILD_URL}",
            to: 'cmvishnubabu08@gmail.com'
        )
    }
    failure {
        echo 'Build failed!'
        emailext (
            subject: "Build Failed: ${env.JOB_NAME} #${env.BUILD_NUMBER}",
            body: "The build failed. Check it here: ${env.BUILD_URL}",
            to: 'cmvishnubabu08@gmail.com'
        )
    }
}
