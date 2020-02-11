'''
Este script tem por intenção testar a performance do modulo
DS_Method que foi desenvolvido para o meu trabalho de conclusão
de curso.
Aqui é montada uma treliça de 18 barras.
'''

import numpy as np
import DS_Method as dsm

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
	# Calcula o deslocamento dos nós
	des = dsm.desloc(drest,barras, nos, areas, m, load)
	# Calcula a força por grau de liberada
	bf = dsm.bar_force(drest, barras, nos, areas, m, load)
	# Calcula as reacoes dos suportes
	sr = dsm.support_reac(drest, barras, nos, areas, m, load)
	# Calculo das forcas por barra
	forca = dsm.scalar_bar_force(drest,barras, nos, areas, m, load)

if __name__ == '__main__':
	test()
