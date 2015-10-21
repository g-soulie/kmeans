# -*- coding: utf-8 -*-
"""
Created on october 2015
@author: B. Pacreau, G. Soulié

:option -k: the k-means k (number of centroids)
:type -k: int
:option -d: k
"""
import random
from math import *
from Observation import *
import es


def compute_kmeans(k,display=False):
	"""
	Compute and display the k-means algorithm on the input file (*./input/input.csv*)

	:arg k: the k of k-means : number of centroids
	:type k: int
	:param display: if True, the first and the second coordinate of the populations are displayed setep by step
	:type display: boolean
	"""
	population = es.read_kmeans_input()
	dimension = len(population[0].values)
	centroids=[]
	affectation=[]
	k=15
	

	##Phase 1 : initialisation of the centroids
	isSelected=[]
	for i in range(len(population)):
		isSelected.append(0)
	for i in range(k):
		while True:
			index = int(floor(random.random()*len(population)))
			if isSelected[index]==0:
				centroids.append(population[index].copy())
				isSelected[index]=1
				break

	#initialisation of the affectations
	for i in range(len(population)):
		affectation.append(0)
	if display:
		es.display(population,None,"Population : ")
	
	stop=False
	

	while not stop:
	##Phase 2 : reaffectation
		if display:
			es.display(population,centroids,"computing k-means")
		distance=[[]]
		for i in range(len(population)):
			distance.append([])
			for j in range(k):
				distance[i].append(population[i].dist(centroids[j]))
		stop = True
		for i in range(len(population)):
			index_du_minimum = distance[i].index(min(distance[i]))
			if not affectation[i]==index_du_minimum:
				affectation[i]=index_du_minimum
				stop = False



##Phase 3 : recalculation
		for j in range(k):
			centroid = Observation(dimension,type="centroid")
			for i in range(len(population)):
				if affectation[i]==j:
					centroid.add(population[i])
			centroids[j]=centroid
	 
	es.write_kmeans_output(population,centroids,affectation)

	if display:
		es.display(population,centroids,"Fin de kmeans")



if __name__ == '__main__':
	#Lecture des options
	params={"-k":10,"-d":False}
	i=1
	while i <len(sys.argv):
	    if sys.argv[i] in params:
	        params[sys.argv[i]]=sys.argv[i+1]
	        i+=1
	    i=i+1
	compute_kmeans(int(params['-k']), display = bool(params['-d']))