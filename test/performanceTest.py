from datetime import datetime as dt
import os
import sys
import time
import platform
import psutil as ps
import numpy as np
import progressbar as pB
import truss10bars as t10
import truss18bars as t18

def benchmark(func, filePath):
	loop = 10000
	# Number of physical cores
	phyCores = ps.cpu_count(logical=False)
	dataCores = np.zeros((phyCores, loop))
	dataRAM = []
	times = []
	pb = pB.ProgressBar()
	total = time.time()
	for i in pb(range(loop)):
		time1 = time.time()
		func
		times.append(time.time() - time1)
	mean10 = np.mean(times)
	if os.path.isfile(filePath):
		sys.stdout = open(filePath, 'a')
	else:
		sys.stdout = open(filePath, 'w')
	print(80 * '=')
	####### Computer data
	print(35 * ' ' + 'Computer data')
	# Wrap the object
	uname = platform.uname()
	# Get system name
	system = uname.system
	print('Operational system: {}'.format(system))
	# Get the release
	release = uname.release
	print('Release: {}'.format(release))
	# Version
	version = uname.version
	print('Version: {}'.format(version))
	# Processor arch
	processorType = uname.processor
	print('Processor type: {}'.format(processorType))
	print('Physical cores: {}'.format(phyCores))
	# Number of logical processors
	logCores = ps.cpu_count(logical=True)
	print('Logical cores: {}'.format(logCores))
	# Max freq of the cpu in GHz
	maxFreq = ps.cpu_freq().max/1e3
	print('Maximun ferquency: {0:.1f} GHz'.format(maxFreq))
	# Total memory in GB
	totalMemo = ps.virtual_memory().total/1024**3
	print('Total RAM memory: {0:.1f} GB'.format(totalMemo))
	print(80 * '=')
	####### Get a way to run the processor check
	####### while running the routine
	for i, pc in enumerate(ps.cpu_percent(percpu=True)):
		pass
	# Percent of memory in usage
	percMemory = ps.virtual_memory().percent
	print(35 * ' ' + 'Results')
	print('Results from {}'.format(dt.now()))
	print('This routine runned {} times'.format(loop))
	print('The average time per run is {0:.2f} seg'.format(mean10))
	print("The total was {0:.2f} seg".format(time.time() - total))
	print(80 * '=')
	sys.stdout.close()

def main():
	benchmark(t10.test(), 'results10bar.bench')
	benchmark(t18.test(), 'results18bar.bench')

if __name__ == '__main__':
	main()


