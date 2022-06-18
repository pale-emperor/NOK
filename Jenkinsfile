pipeline {
    environment {
        TESTS_PATH = "/home/tempesta/tempesta-test"
    }

    agent {
       label "tempesta-test"
    }

    stages {
        stage('Set buildName and cleanWS'){
            steps {
                catchError(buildResult: 'SUCCESS', stageResult: 'FAILURE') {
                    script {
                        currentBuild.displayName = "PR-${ghprbPullId}"
                    }
                    dir('${TESTS_PATH}'){
                        sh 'pwd'
                        sh 'ls'
                    }
                    cleanWs()
                    sh 'rm -rf /root/tempesta'
                    sh 'ls /home/tempesta/tempesta-test'
                    sh 'ls ${TESTS_PATH}'
                    sh 'echo ${TESTS_PATH}'
                }
            }
        }

        stage('Build tempesta-fw') {
            steps {
                sh 'cp -r . /root/tempesta'
                dir("/root/tempesta"){
                    sh 'make'
                }
            }
        }

        stage('Checkout tempesta-tests') {
            steps {
                sh 'rm -rf ${TEMPESTA_PATH}'
                sh 'git clone https://github.com/tempesta-tech/tempesta-test.git ${TESTS_PATH}'
            }
        }

        stage('Run tests') {
            steps {
                dir('${TEMPESTA_PATH}'){
                    sh './run_tests.py'
                }
            }
        }

    }
}
