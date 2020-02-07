'''
Esse script é somente um teste de desempenho
utilzando o caso do TCC de um treliça de 10 barras

Este script demorou 389 segundos para rodar num Dell Precision T3610
com Windows 7, 16GB RAM e SSD 256GB
'''

import numpy as np
import DS_Method as dsm
import time
import sys, os

def test():
	# coordenadas dos nós em mm
	nos = np.array([[0,0], [0, 9.144], [9.144, 0],[9.144,9.144],[18.288,0],[18.288,9.144]])
	barras = [(0,2),(0,3),(1,2),(1,3),(3,2),(3,4),(5,2),(3,5),(2,4),(4,5)]
	# area das barras
	areas = [50 for i in range(len(barras))]
	# momento de inercia
	m = [6895e4 for i in range(len(barras))]
	# carregamentos em 
	load = [[5, -444.82], [9, -444.82]]
	# nós com restrição
	drest = [0,1,2,3]
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
