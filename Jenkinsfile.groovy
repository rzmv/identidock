pipeline {
    agent {
        label "docker"
    }
    stages {
        stage('build') {
            steps {
                sh "docker build . -t testapp"
            }
        }

        stage("Test") {
            steps {
                echo "yo tests"
            }
        }
    }
}