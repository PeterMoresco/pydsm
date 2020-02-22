#include <math.h>
#include <iostream>
#include <list>
#include <xtensor/xarray.hpp>
#include <xtensor/xio.hpp>
#include <xtensor/xview.hpp>

//auto stiff_matrices(std::list<int> bars, std::list<std::list<int>> nodes, std::list<double> areas, std::list<double> mom_e)
int stiff_matrices(auto nodes, auto bars)
{
	// Initializes the vector for identification of
	// the forces. Since these are in 2D, there are
	// 2 directions for the forces
	std::vector<std::vector<int> > forcaID(nodes.size());
	int fi = 0;
	for (int i =0; i < nodes.size(); i++) {
		forcaID[i] = std::vector<int> {fi, fi+1};
		fi += 2;
	}
	// Just logging
	std::cout << "This is the forcaID vector" << std::endl;
	for (std::vector<int> v : forcaID) {
		std::cout << std::endl;
		for (int j : v){
		std::cout << j;
		std::cout << " ";
		}
	}
	std::cout << "\n";
	// Here the assigment order changes
	// And yes, this is necessary!
	// mrl = Matriz de Rigidez Local/Local Stiffnes Matrix
	int bSize = bars.size();
	auto mrl = xt::zeros<double>({4, 4, bSize});
	double compBarras[bSize];
	for (int b = 0; b < bSize; b++) {
		double x0 = nodes[bars[b][0]][0];
		double x1 = nodes[bars[b][1]][0];
		double y0 = nodes[bars[b][0]][1];
		double y1 = nodes[bars[b][1]][1];
		compBarras[b] = hypot(x1 - x0, y1 - y0);
		std::cout << "This is the lentgh of the bar: " << b << std::endl;
		std::cout << compBarras[b] << std::endl;
	}
	// Initializing the Global Stiffnes Matrix
	int gL = 2 * nodes.size();
	auto mrg = xt::zeros<double>({gL, gL});
	// Calculating the Local Stiffness Matrices
	
	return 0;
}

int main()
{
	std::vector<std::vector<double> > nos = {{0, 0},
					      {0, 9.144},
					      {9.144, 0},
					      {9.144, 9.144},
					      {18.288, 0},
					      {18.288, 9.144}};
	std::vector<std::vector<int> > barras = {{0, 2},
					         {0, 3},
						 {1, 2},
						 {1, 3},
						 {3, 2},
						 {3, 4},
						 {5, 2},
						 {3, 5},
						 {2, 4},
						 {4, 5}};
	int tmp = stiff_matrices(nos, barras);
	return 0;
}

