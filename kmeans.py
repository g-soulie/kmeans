"""
Created on 29 July 2012
@author: Lisa Simpson
"""

import random
from math import *
from Ind import *
from Bary import *
import Image
import matplotlib.pyplot as plt
import es
import commands


def index_min(tab):
	"""
	This function is used to determine the index the index of a list of floats
	@type	tab: list<float>
	@param	tab: tableau de float quelconque
	@rtype: int
	@return:	the index of the minimum of the list tab.

	"""
	min=tab[0]
	index_min=0
	for i in range(len(tab)-1):
		i=i+1
		if tab[i]<min:
			index_min=i
			min=tab[i]
	return index_min

def display(population,barycentres,title):
	"""
	This fonction is used to display the population and the centroids on a graph
	@type	population: list<Ind>
	@param	population: list of Ind representing a vector
	@type	barycentres: list<Ind>
	@param	barycentres: list of centroids
	@type	titre: String
	@param	titre: name of the graphic
	"""
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
	plt.title(title)
	plt.xlabel('x')
	plt.ylabel('y')
	plt.savefig('ScatterPlot.png')
	plt.show()

def read():
	"""
	This fonction is used to read the file "input.csv" within the input folder
	@return a population based on the input file
	"""
	population=[]
	data = es.read_data('./input/input.csv',ignore_first_column = True,skip_first_line = True)
	dimension=len(data[0])-1
	for i in range(len(data)):
		population.append(Ind(dimension))
		population[i].set_values(data[i])
	return population

def write_output(population,barycentres,centroids):
	"""
	This fonction is used to
	@type	population: list<Ind>
	@param	population: set of observations
	@type	population: list<Ind>
	@param	population: set of observations
	@type	population: list<Ind>
	@param	population: set of observations
		

	@return
	"""
	#Ecriture du fichier centroid.csv :
	data=[["# no_centre"]]
	for i in range(dimension):
		data[0].append("attribut_"+str(i))
	for i in range(len(barycentres)):
		data.append([i])
		for j in range(len(barycentres[i].values)):
			data[i+1].append(barycentres[i].values[j])
	commands.getoutput("mkdir ./output/")
	commands.getoutput("rm ./output/centroids.csv")
	es.write_data(data,'./output/centroids.csv')

	#Ecriture du fichier affectation.csv :
	data=[["# no_observation"]]
	for i in range(dimension):
		data[0].append("attribut_"+str(i))
	data[0].append("no_classe")
	for i in range(len(population)):
		data.append([i])
		for j in range(dimension):
			data[i+1].append(population[i].values[j])
		data[i+1].append(centroids[i])
	commands.getoutput("rm ./output/affectation.csv")
	es.write_data(data,'./output/affectation.csv')

if __name__ == '__main__':
	#n=400
	
	population = []
	#population=genAleatoire(dimension)
	#population=lireImage("bretagne-3.jpg",413,500,dimension)
	#population=read("iris.csv")
	population = read()
	dimension = len(population[0].values)
	barycentres=[]#
	k=15
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
	display(population,None,"population : ")
	stop=False
	while not stop:
##Phase 2 : reaffectation
		#display(population,barycentres,"computing k-means")
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
	write_output(population,barycentres,centroids)


	display(population,barycentres,"||||||||||||||||||||")



