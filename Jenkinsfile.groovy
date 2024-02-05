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
                sh "docker run --env ENV="UNIT" testapp"
            }
        }
    }
}