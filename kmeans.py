# -*- coding: utf-8 -*-
"""
Created on october 2015
@author: B. Pacreau, G. Soulié
"""
import random
from math import *
from Observation import *
import es
import sys


def compute_kmeans(k,display=False,max_iteration=99999):
	"""
	Compute and display the k-means algorithm on the input file 
		(*./input/input.csv*)

	:arg k: the k of k-means : number of centroids
	:type k: int
	:param max_iteration: the number maximum of iteration we allow
	:type max_iteration: int
	:param display: if True, the first and the second coordinate of the 
		populations are displayed setep by step
	:type display: boolean
	"""

	population = es.read_kmeans_input()
	dimension = len(population[0].values)
	


#=============================================================================#
#						Phase 1 : Initialisation 							  #
#=============================================================================#

	#centroids initialisation:
	centroids=[]
	isSelected=[]
	for i in range(len(population)):
		isSelected.append(0)
	for i in range(k):
		while True:

			#centroids are ranomly choose in the population
			index = int(floor(random.random()*len(population)))

			#We checked that we don't take the same centroid twice
			if isSelected[index]==0:
				centroids.append(population[index].copy())
				isSelected[index]=1
				break

	#affectation initialisation:
	affectation=[]
	for i in range(len(population)):
		affectation.append(0)
	
	#if display, display the population
	if display:
		es.display(population,None,"Population : ",False)
	
	#Loop stop condition initialisation:
	stop=False
	

	iteration = 0
	while not stop and iteration < max_iteration:
		iteration+=1
#=============================================================================#
#							Phase 2: Affectation 						      #
#=============================================================================#

		#if display, we print the population and the centroids
		if display:
			es.display(population,centroids,\
				"computing k-means : iteration "+str(iteration),False)

		#Compute the distance between each observation and each centroid
		distance=[[]]
		for i in range(len(population)):
			distance.append([])
			for j in range(k):
				distance[i].append(population[i].dist(centroids[j]))

		#The loop stop condition is fixed to True
		stop = True

		#Affect the nearest centroid to each observation.
		for i in range(len(population)):
			index_du_minimum = distance[i].index(min(distance[i]))
			if not affectation[i]==index_du_minimum:
				affectation[i]=index_du_minimum

		#If there is any changement, the loop stop condition became false
				stop = False


#=============================================================================#
#							Phase 3: Calculation 							  #
#=============================================================================#
		
		#Compute the new centroids
		for j in range(k):
			centroid = Observation(dimension)
			for i in range(len(population)):
				if affectation[i]==j:
					centroid.add(population[i])
			centroids[j]=centroid
	
	#write the output files
	es.write_kmeans_output(population,centroids,affectation)

	#if display, we print the population and the centroids
	if display:
		es.display(population,centroids,"K-means computed",True)



if __name__ == '__main__':
	
	#Set the default options:
	options={"-k":10,"-d":False}

	#Read the options: 
	i=1
	while i <len(sys.argv):
	    if sys.argv[i] in options:
	        options[sys.argv[i]]=sys.argv[i+1]
	        i+=1
	    i=i+1

	#Compute k-means:
	compute_kmeans(int(options['-k']), display = bool(options['-d']))