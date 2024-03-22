pipeline {
    agent any
    environment {
        // Define the Python virtual environment directory
        VENV_DIR = 'venv'
        // Define the project's root directory
        PROJECT_ROOT = "C:\\Users\\Owner\\PycharmProjects\\Otaku_house"
        // Define the path to the Python executable
        PYTHON_PATH = "C:\\Users\\Owner\\PycharmProjects\\Otaku_house\\.venv\\Scripts\\python.exe"
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
                    // Navigate to project's root directory
                    bat "cd ${PROJECT_ROOT}"
                    // Set up virtual environment if it doesn't exist
                    bat "if not exist ${VENV_DIR} call \"%PYTHON_PATH%\" -m venv ${VENV_DIR}"
                    // Activate virtual environment
                    bat "call ${VENV_DIR}\\Scripts\\activate"
                    // Upgrade pip to the latest version
                    bat "call ${VENV_DIR}\\Scripts\\python.exe -m pip install --upgrade pip"
                    // Install requirements
                    bat "call ${VENV_DIR}\\Scripts\\pip install -r requirements.txt"
                }
            }
        }
        stage('Run Tests') {
        steps {
        script {
            // Activate the virtual environment
            bat "call ${VENV_DIR}\\Scripts\\activate"
            // Set PYTHONPATH and run the tests in one command to ensure the environment variable is applied
            bat "set PYTHONPATH=%PYTHONPATH%;C:\\Users\\Owner\\PycharmProjects\\Otaku_house && call ${VENV_DIR}\\Scripts\\python C:\\Users\\Owner\\PycharmProjects\\Otaku_house\\tests\\tests_api\\placeOrder_api.py"
        }
    }
}


            }
 }