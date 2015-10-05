import random
from math import *
from Ind import *
from Bary import *
import matplotlib.pyplot as plt

def index_min(tab):
	min=tab[0]
	index_min=0
	for i in range(len(tab)-1):
		i=i+1
		if tab[i]<min:
			index_min=i
			min=tab[i]
	return index_min

def afficher(population,G,titre):
	x=[]
	y=[]
	xG=[]
	yG=[]
	for i in range(len(population)):
		x.append((population[i].values)[0])
	for i in range(len(population)):
		y.append(population[i].values[1])


	plt.scatter(x,y,s=100)

	if not G is None:
		for i in range(len(G)):
			xG.append((G[i].values)[0])
		for i in range(len(G)):
			yG.append(G[i].values[1])

	
		plt.scatter(xG,yG,s=100,c='red')


	plt.title(titre)
	plt.xlabel('x')
	plt.ylabel('y')
	plt.savefig('ScatterPlot.png')
	plt.show()



if __name__ == '__main__':
	n=400
	dimension=2
	population = []
	for i in range(n/3):
		population.append(Ind(dimension))
		population[i].set_values([-15+random.gauss(0.,1.)*3,0+random.gauss(0.,1.)*3])
	for i in range(n/3):
		population.append(Ind(dimension))
		population[n/3+i].set_values([random.gauss(0.,1.)*3,0+random.gauss(0.,1.)*3])
	for i in range(n/3):
		population.append(Ind(dimension))
		population[2*n/3+i].set_values([-5+random.gauss(0.,1.)*3,15+random.gauss(0.,1.)*3])


##Phase 1 : initialisation

	G=[]
	k=3
	B=[]

	for i in range(len(population)):
		B.append(0)
	for i in range(k):
		while True:
			index = int(floor(random.random()*len(population)))
			if B[index]==0:
				G.append(population[index].copy())
				B[index]=1
				break

	
	centroids=[]
	for i in range(len(population)):
		centroids.append(0)
	afficher(population,None,"population : ")
	stop=False
	while not stop:
##Phase 2 : reaffectation
		afficher(population,G,"computing k-means")


		distance=[[]]
		for i in range(len(population)):
			distance.append([])
			for j in range(k):
				distance[i].append(population[i].dist(G[j]))

		stop = True
		for i in range(len(population)):
			index_mini = index_min(distance[i])
			if not centroids[i]==index_mini:
				centroids[i]=index_mini
				stop = False
		#print centroids
##Phase 3 : recalculation
		for j in range(k):
			barycentre = Bary(dimension)
			for i in range(len(population)):
				if centroids[i]==j:
					barycentre.add(population[i])
			G[j]=barycentre
		#print G
	afficher(population,G,"||||||||||||||||||||")


##Phase 4 : critere d'arret


