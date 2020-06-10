pipeline {

	agent any
	   	//{
		//docker {
		//	image 'python:3.6.9'
		//}
	//}

	stages {
		stage('build') {
			steps {
				sh 'python3 --version'
				sh 'python3 ./Python/projects/redpackage.py'
			}
		}
	}
}
