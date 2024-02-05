pipeline {
    agent {
        label: "docker"
    }
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