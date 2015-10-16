import random
from math import *
from Ind import *
from Bary import *
import Image
import matplotlib.pyplot as plt
import es

def index_min(tab):
	min=tab[0]
	index_min=0
	for i in range(len(tab)-1):
		i=i+1
		if tab[i]<min:
			index_min=i
			min=tab[i]
	return index_min

def afficher(population,barycentres,titre):
	x=[]
	y=[]
	xbarycentres=[]
	ybarycentres=[]
	for i in range(len(population)):
		x.append((population[i].values)[0])
	for i in range(len(population)):
		y.append(population[i].values[1])
	plt.scatter(x,y,s=1)
	if not barycentres is None:
		for i in range(len(barycentres)):
			xbarycentres.append((barycentres[i].values)[0])
		for i in range(len(barycentres)):
			ybarycentres.append(barycentres[i].values[1])
		plt.scatter(xbarycentres,ybarycentres,s=100,c='red')
	plt.title(titre)
	plt.xlabel('x')
	plt.ylabel('y')
	plt.savefig('ScatterPlot.png')
	plt.show()


def lireImage(path,x,y,dimension):
	population = []
	im=Image.open(path)
	data = list(im.getdata())
	compteur=0
	nb_ind=0
	for i in range(x):
		for j in range(y):
			if data[compteur][1]>200 and (i>75 or j>50):
				population.append(Ind(dimension))
				population[nb_ind].set_values([j+0.,x-i+0.])
				nb_ind+=1
			compteur+=1
	print("nb de pixels actives : "+str(nb_ind))
	return population


def genAleatoire(dimension):
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
	return population


def read(filename):
	population=[]
	data = es.read_data(filename,ignore_first_column = True)
	dimension=len(data[0])
	for i in range(len(data)):
		population.append(Ind(dimension))
		population[i].set_values(data[i])
	return population


def write(filename,centroids):
	data=[]
	for i in range(len(centroids)):
		data.append([])
		data[i].append(centroids[i])
	es.write_data(data,filename)



if __name__ == '__main__':
	#n=400
	dimension=2
	population = []
	#population=genAleatoire(dimension)
	population=lireImage("bretagne-3.jpg",413,500,dimension)
	#population=read("iris.csv")
	barycentres=[]#
	k=20
	B=[]

	print(str(population[0].values))


##Phase 1 : initialisation


	for i in range(len(population)):
		B.append(0)
	for i in range(k):
		while True:
			index = int(floor(random.random()*len(population)))
			if B[index]==0:
				barycentres.append(population[index].copy())
				B[index]=1
				break

	
	centroids=[]
	for i in range(len(population)):
		centroids.append(0)
	afficher(population,None,"population : ")
	stop=False
	while not stop:
##Phase 2 : reaffectation
		afficher(population,barycentres,"computing k-means")
		distance=[[]]
		for i in range(len(population)):
			distance.append([])
			for j in range(k):
				distance[i].append(population[i].dist(barycentres[j]))
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
			barycentres[j]=barycentre
			barycentres[j].updates()
	write("output.csv",centroids)


	afficher(population,barycentres,"||||||||||||||||||||")



