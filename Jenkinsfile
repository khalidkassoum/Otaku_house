pipeline {
    agent any
    environment {
        // Define the Python virtual environment directory
        VENV_DIR = 'venv'
        // Define the project's root directory
        PROJECT_ROOT = "C:\\Users\\Owner\\PycharmProjects\\Otaku_house"
        // Define the path to the Python executable
        PYTHON_PATH = "C:\\Users\\Owner\\AppData\\Local\\Programs\\Python\\Python312\\python.exe"
        // Define the directory where the HTML report is generated
        HTML_REPORT_DIR = "reports"
    }
    stages {
        // ... Other stages remain unchanged ...

        stage('List Report') {
            steps {
                script {
                    bat "dir ${PROJECT_ROOT}\\${HTML_REPORT_DIR}"
                }
            }
        }

        stage('Publish Report') {
            steps {
                publishHTML target: [
                    allowMissing: false,
                    alwaysLinkToLastBuild: true,
                    keepAll: true,
                    reportDir: "${PROJECT_ROOT}\\${HTML_REPORT_DIR}",
                    reportFiles: 'report.html',
                    reportName: "HTML Report"
                ]
            }
        }
    }
}
