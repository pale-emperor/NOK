pipeline {
    agent {
       label "epyc-tempesta-test"
    }

    stages {
        stage('Set buildname'){
            buildName '#PR-${ghprbPullId}'
        }
        
        stage('build tempesta-fw') {
            steps {
                sh 'rm -rf /root/tempesta'
                sh 'git clone https://github.com/tempesta-tech/tempesta.git'
                sh 'mv tempesta /root/tempesta'
                dir("/root/tempesta"){
                    sh 'make'
                }
            }
        }

        stage('Checkout tempesta-tests') {
            steps {
                sh 'rm -rf /home/tempesta/tempesta-test'
                sh 'git clone https://github.com/tempesta-tech/tempesta-test.git /home/tempesta/tempesta-test'
            }
        }

        stage('Run tests') {
            steps {
                dir("/home/tempesta/tempesta-test"){
                    sh './run_tests.py ws'
                }
            }
        }

    }
}