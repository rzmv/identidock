pipeline {
    agent any
    stages {
        stage('build') {
            steps {
                docker build . -t testapp
            }
        }

        stage("Test") {
            steps {
                echo "yo tests"
            }
        }
    }
}