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
        HTML_REPORT_DIR = "my_report"
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
                    bat "set PYTHONPATH=%PYTHONPATH%;${PROJECT_ROOT} && call ${VENV_DIR}\\Scripts\\python ${PROJECT_ROOT}\\tests\\tests_api\\placeOrder_api.py"
                }
            }
        }
        stage('Publish Report') {
            steps {
                script {
                    // Check if publishHTML step is available
                    if (this.binding.hasVariable('publishHTML')) {
                        publishHTML([
                            allowMissing: false,
                            alwaysLinkToLastBuild: true,
                            keepAll: true,
                            reportDir: "${PROJECT_ROOT}\\${HTML_REPORT_DIR}",
                            reportFiles: 'report.html',
                            reportName: "HTML Report"
                        ])
                    } else {
                        echo 'publishHTML step not available, skipping report publication.'
                    }
                }
            }
        }
    }
}
