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
        stage('Preparation') {
            steps {
                echo 'Checking out SCM'
                checkout scm
            }
        }
        stage('Setup Python Environment') {
            steps {
                script {
                    bat "cd ${PROJECT_ROOT}"
                    bat "if not exist ${VENV_DIR} call \"%PYTHON_PATH%\" -m venv ${VENV_DIR}"
                    bat "call ${VENV_DIR}\\Scripts\\activate"
                    bat "call ${VENV_DIR}\\Scripts\\python.exe -m pip install --upgrade pip"
                    bat "call ${VENV_DIR}\\Scripts\\pip install -r requirements.txt"
                }
            }
        }
        stage('Run Tests') {
            steps {
                script {
                    bat "call ${VENV_DIR}\\Scripts\\activate"
                    bat "set PYTHONPATH=%PYTHONPATH%;${PROJECT_ROOT} && call ${VENV_DIR}\\Scripts\\python ${PROJECT_ROOT}\\test_Runner.py"
                }
            }
        }
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
        stage('Verify Report') {
    steps {
        script {
            bat "type ${PROJECT_ROOT}\\${HTML_REPORT_DIR}\\report.html"
        }
    }
}

        stage('Archive Reports') {
            steps {
                archiveArtifacts artifacts: "${HTML_REPORT_DIR}/*", allowEmptyArchive: true
            }
        }
    }
}
