'''
Esse é um teste de conceito para
apurar as ideias para o projeto do 
DS_Method OOP
Baseado no exemplo Pg47 do material da Altair
Practical Aspects of FE Simulation

####### Ideias #######
- Permitir imputar as barras por ponto inicial e ângulo;
- Permitir acessar a matriz individual de cada barra;
- Fazer orientado a objeto;
- identificar carregamento por nó
- identificar restrição por nó
- identificar as areas por barras
- permitir lsita para momentos de inércia ou valor
- disponibilizar via pip
- disponibilizar visualização
- utilizar bibliotecas em cpp
- utilizar teste unitário
- utilizar teste de performance
- Criar diretório no GitHub
'''

import numpy as np
import DS_Method as dsm
import time
import sys, os

def test():
	# momento de inercia
	m = [210, 70, 210]
	# coordenadas dos nós em mm
	nos = np.array([[0,810], [971.14,680], [0,0], [361.71,480]])
	barras = [(2,0), (2,3), (2,1)]
	# area das barras
	areas = [280, 280, 280]
	# carregamentos em 
	f = 29
	load = [[4,f*np.cos(37*np.pi/180)], [5,-f*np.sin(37*np.pi/180)]]
	# nós com restrição
	drest = [0,1,2,3,6,7]
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
	# Disable stdout
	sys.stdout = open(os.devnull, 'w')
	# Run the script
	test()
	# Enable output
	sys.stdout = sys.__stdout__
	print('\n')
	print('------- {0:.3f} segundos -------'.format(time.time() - sTime))
