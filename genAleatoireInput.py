import genInput
from Ind import *

def genAleatoire(dimension):	
	population = []
	n=400
	for i in range(n/3):
		population.append(Ind(dimension))
		population[i].set_values([-15+random.gauss(0.,1.)*3,0+random.gauss(0.,1.)*3])
	for i in range(n/3):
		population.append(Ind(dimension))
		population[n/3+i].set_values([random.gauss(0.,1.)*3,0+random.gauss(0.,1.)*3])
	for i in range(n/3):
		population.append(Ind(dimension))
		population[2*n/3+i].set_values([-5+random.gauss(0.,1.)*3,15+random.gauss(0.,1.)*3])
	genInput.write(population,2) #2 = the dimension of the vectors

if __name__ == '__main__':
	genAleatoire(2) #2 = the dimension of the vectors