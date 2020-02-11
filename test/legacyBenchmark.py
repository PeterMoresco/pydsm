import sys
import os
sys.path.append(os.getcwd()+'/legacy/')
import truss10bars as t10
import truss18bars as t18
from performanceTest import benchmark


def main():
	benchmark(t10.test(), os.getcwd()+'/legacy/results10bar.bench')
	benchmark(t18.test(),os.getcwd()+ '/legacy/results18bar.bench')

if __name__ == '__main__':
	main()


