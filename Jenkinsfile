pipeline {

	agent any

	stages {

		stage('unit tests of utils') {
			steps {
				sh 'python3 ./Python/test_utils/testarray.py'
				sh 'python3 ./Python/test_utils/testheap.py'
				sh 'python3 ./Python/test_utils/testlinkedlist.py'
				sh 'python3 ./Python/test_utils/testqueue.py'
				sh 'python3 ./Python/test_utils/testtree.py'
				sh 'python3 ./Python/test_utils/testpriorityqueue.py'
			}
		}

		stage('unit tests of sorts') {
			steps {
				sh 'python3 ./Python/test_sorts/testbubblesort.py'
				sh 'python3 ./Python/test_sorts/testbucketsort.py'
				sh 'python3 ./Python/test_sorts/testcocktailsort.py'
				sh 'python3 ./Python/test_sorts/testquicksort.py'
				sh 'python3 ./Python/test_sorts/testcountsort.py'
				sh 'python3 ./Python/test_sorts/testheapsort.py'
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
				sh 'python3 ./Python/projects/lcucache.py'
				sh 'python3 ./Python/projects/astarsearch.py'
				sh 'python3 ./Python/projects/redpackage.py'
			}
		}
	}
}
