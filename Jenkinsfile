pipeline {

	agent any

	stages {

		stage('unit tests of utils') {
			steps {
				sh 'python3 ./Python/tests/testutils.py -v'
			}
		}

		stage('unit tests of sorts') {
			steps {
				sh 'python3 ./Python/tests/testsorts.py -v'
			}
		}

		stage('unit tests of apps') {
			steps {
				sh 'python3 ./Python/test_apps/testbestgoldmining.py'
				sh 'python3 ./Python/test_apps/testcyclelist.py'
				sh 'python3 ./Python/test_apps/testdictionarysort.py'
				sh 'python3 ./Python/test_apps/testgreatestcommondivisor.py'
				sh 'python3 ./Python/test_apps/testgreatestsorteddistance.py'
				sh 'python3 ./Python/test_apps/testlostnumber.py'
				sh 'python3 ./Python/test_apps/testmediansortedarrays.py'
				sh 'python3 ./Python/test_apps/testminstack.py'
				sh 'python3 ./Python/test_apps/testremovekdigits.py'
				sh 'python3 ./Python/test_apps/teststackqueue.py'
			}
		}

		stage('unit tests of projects') {
			steps {
				sh 'python3 ./Python/test_projects/testbitmap.py'
				sh 'python3 ./Python/test_projects/testlrucache.py'
				sh 'python3 ./Python/test_projects/testastarsearch.py'
				sh 'python3 ./Python/test_projects/testredpackage.py'
			}
		}
	}
}
