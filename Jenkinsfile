post {
    always {
        // Always send an email after the pipeline completes
        emailext(
            subject: "Build Notification: ${currentBuild.currentResult} - Build #${env.BUILD_NUMBER}",
            body: """
                <h2>Build Result: ${currentBuild.currentResult}</h2>
                <p><b>Job:</b> ${env.JOB_NAME}</p>
                <p><b>Build #:</b> ${env.BUILD_NUMBER}</p>
                <p><b>Build URL:</b> <a href="${env.BUILD_URL}">${env.BUILD_URL}</a></p>
            """,
            to: 'your-email@example.com',
            mimeType: 'text/html'
        )
    }
    success {
        // If the build succeeds, send a success email
        emailext(
            subject: "✅ SUCCESS: Build #${env.BUILD_NUMBER}",
            body: """
                <h2>✅ Build Successful</h2>
                <p><b>Job:</b> ${env.JOB_NAME}</p>
                <p><b>Build #:</b> ${env.BUILD_NUMBER}</p>
                <p><b>URL:</b> <a href="${env.BUILD_URL}">${env.BUILD_URL}</a></p>
            """,
            to: 'cmvishnubabu08@gmail.com',
            mimeType: 'text/html'
        )
    }
    failure {
        // If the build fails, send a failure email
        emailext(
            subject: "❌ FAILED: Build #${env.BUILD_NUMBER}",
            body: """
                <h2>❌ Build Failed</h2>
                <p><b>Job:</b> ${env.JOB_NAME}</p>
                <p><b>Build #:</b> ${env.BUILD_NUMBER}</p>
                <p><b>URL:</b> <a href="${env.BUILD_URL}">${env.BUILD_URL}</a></p>
            """,
            to: 'cmvishnubabu08@gmail.com',
            mimeType: 'text/html'
        )
    }
}
