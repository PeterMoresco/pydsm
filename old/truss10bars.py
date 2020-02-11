'''
Este script tem por intenção testar a performance do modulo 
DS_Method que desenvolvido para o meu trabalho de conclusão de 
curso. 
Aqui é montada uma treliça de 10 barras.
'''

import numpy as np
import DS_Method as dsm

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
	####### Inicio dos calculos do modulo
	# Calular as matrizes de rigidez
	mrl, mrg = dsm.stiff_matrices(barras, nos, areas, m)
	# Calcula o deslocamento dos nós
	des = dsm.desloc(drest,barras, nos, areas, m, load)
	# Calcula a forca por grau de liberadade da barra
	bf = dsm.bar_force(drest, barras, nos, areas, m, load)
	# Calcula as reacoes dos suportes
	sr = dsm.support_reac(drest, barras, nos, areas, m, load)
	# Calculo das forcas por barra
	forca = dsm.scalar_bar_force(drest,barras, nos, areas, m, load)

if __name__ == '__main__':
	test()
