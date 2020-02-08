'''
Esse script é somente um teste de desempenho
utilzando o caso do TCC de um treliça de 18 barras

Performance Benchmark:

- Este script demorou 664 segundos para rodar num Dell Precision T3610
com Windows 7, 16GB RAM e SSD 256GB;
- Este script demorou 1473.751 segundos para rodar num HP v064br,
com Ubuntu 18.04LTS, 10GB RAM e SSD 100GB(partição Linux completa).
Utilizando desempenho em 100%;
- Este script demorou 691.431 segundos para rodar num Lenovo T460,
processador i5-6300U vPro,
com Windows 10 Pro, 8GB RAM, SSD 237GB;

'''

import numpy as np
import DS_Method as dsm
import time
import sys, os

def test():
	# coordenadas dos nós em mm
	nos = np.array([[31.75,6.35],[25.4,6.35],[25.4,0],[19.05,6.35],[19.05,0],[12.7,6.35],[12.7,0],[6.35,6.35],[6.35,0],[0,6.35],[0,0]]
)
	barras = [(0,1),(0,2),(1,2),(3,1),(3,2),(4,2),(3,4),(3,5),(5,4),(6,4),(5,6),(5,7),(7,6),(8,6),(7,8),(9,7),(9,8),(10,8)]
	# area das barras
	areas = [50 for i in range(len(barras))]
	# momento de inercia
	m = [6895e4 for i in range(len(barras))]
	# carregamentos em 
	load = [[1, -88.964432], [3, -88.964432], [7, -88.964432], [11, -88.964432], [15, -88.964432]]
	# nós com restrição
	drest = [18, 19, 20, 21]
	# Calular as matrizes de rigidez
	mrl, mrg = dsm.stiff_matrices(barras, nos, areas, m)
	for i, j in enumerate(barras):
		print('\n')
		print(70*'#')
		print("Essa é a matriz de rigidez da barra {}".format(i+1))
		print('\n')
		print(mrl[:,:,i])
		print('\n')
		print(70*'#')

	print(70*'#')
	print('A matriz de rigidez global é:\n')
	print(mrg[:4, :4])
	print('\n')
	print(70*'#')

	des = dsm.desloc(drest,barras, nos, areas, m, load)
	print('\n')
	print('Esses são os deslocamentos: \n')
	print(des)

	forca = dsm.scalar_bar_force(drest,barras, nos, areas, m, load)
	for m, n in enumerate(barras):
		print('\n')
		print(70*'#')
		print('A força na barra {} é de:\n'.format(m+1))
		print(forca[m])

if __name__ == '__main__':
	sTime = time.time()
	for i in range(50000):
		# Disable stdout
		sys.stdout = open(os.devnull, 'w')
		# Run the script
		test()
		# Enable output
		sys.stdout = sys.__stdout__
		if i % 5e3 == 0:
			print('----------------------------------------------------')
			print('-------        This is the {}th run          -------'.format(i))
			print('------- Its been {0:.3f} sec since the start -------'.format(time.time() - sTime))
			print('----------------------------------------------------')
	print('------- It took a total of {0:.3f} sec -------------'.format(time.time() - sTime))
	print('------------------------ Fineshed! -----------------')
	print('----------------------------------------------------')
