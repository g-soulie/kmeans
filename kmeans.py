# -*- coding: utf-8 -*-
"""
Created on october 2015
@author: B. Pacreau, G. Soulié
"""
import random
import math
from Observation import *
import es
import sys
import numpy as np
from scipy.stats import norm


def compute_gmeans(population,k = 1, alpha = 1,display=False):
	"""
	compute the g-means algorithm on the input file (*./input/input.csv*).

	:params k: the g-means algorithm will start with this k.
	:type k: int
	:arg population: the population of Observations tocompute g-means on.
	:type population: Observation[]
	:params alpha: significance level of the gaussian test
	:type alpha: float
	:param display: if True, the first and the second coordinate of the 
		populations are displayed step by step
	:type display: boolean
	:rtype: void
	"""

	#initialisation of the centroids
	centroids = None

	#getting the dimension of the observations
	dimension = len(population[0].values)

	#Stop condition of the while loop which increase k
	stop = False
	
	while not stop:
		
		#re-initialize the stop-condition
		stop = True

		#compute the k-means algorithms on the population
		temp = compute_kmeans(k,population,centroids = centroids,display = \
			display, title="G-means : k = "+str(k)+" - ")

		#getting the results of the computation
		centroids = temp[0]
		affectation = temp[1]
		
		#Loop on each cluster to check the gaussian-like
		for i in range(k):
			
			#getting the population of the cluster
			subPopulation = []
			for j in range(len(population)):
				if affectation[j] == i:
					subPopulation.append(population[j])

			#getting the size of the cluster
			n = len(subPopulation)

			#Getting the direction of the cluster
			dual_centroids = compute_kmeans(2,subPopulation,display=display,\
				title="G-means : k = "+str(k)+" - direction of cluster "\
				+ str(i+1) + "out of" + str(k) + " - ")[0]


			es.display_Direction(dual_centroids[0],dual_centroids[1],k=k,cluster=i)

			direction_vector = dual_centroids[0].substract(dual_centroids[1])
			
			#Porjecting the clusters on its direction : 
			norme = direction_vector.dist(Observation(dimension))
			projections = []
			for j in range(len(subPopulation)):
				projection = 0
				for l in range(dimension):
					projection+=subPopulation[j].values[l]*\
					direction_vector.values[l]/norme/norme
				projections.append(projection)

			#using numpy to help for mathematicall stuff
			projections = np.array(projections)

			#centering around 0
			projections = (projections-projections.mean())

			#scaling
			projections /= math.sqrt(projections.var())

			#ordering
			projections.sort()

			if display:
				es.display_histogramme(projections, title = \
					"histogramme of the cluster "+str(i+1))

			#considering the N(0, 1) cumulative distribution function
			Z = norm.cdf(projections)

			#computing A²(Z)
			A_carre = 0
			for j in range(n):
				A_carre += (2*(j+1)-1)*(math.log(Z[j])+math.log(1-Z[n-j-1]))	
			A_carre /= - n
			A_carre -= n

			#computing A²*(Z)
			A_star_carre = A_carre * (1+4/n-25/(n**2))

			#increasing k condition :
			if A_star_carre > alpha * len(population):

				#Setting the new centroids
				new_centroids = dual_centroids
				for j in range(k):
					if not i==j:
						new_centroids.append(centroids[j])
				centroids = new_centroids

				#increasing k
				k += 1
				print("cluster "+str(i+1)+" non validé gaussien : " + \
					str(A_star_carre/len(population)/alpha) + "!")
				print("-------- increasing k --> "+str(k)+" -----------")

				#change the while loop stop condition
				stop = False

				break

			else:

				#The cluster is gaussian like.
				print("cluster "+str(i+1)+" validé gaussien : " + str(A_star_carre	\
				/len(population)/alpha) + "!")


	compute_kmeans(k,population,display=display)
				



def compute_kmeans(k,population,centroids = None,display=False,\
	max_iteration=99999,title=""):
	"""
	Compute the k-means algorithm on the input file 
		(*./input/input.csv*)

	:arg k: the k of k-means : number of centroids
	:type k: int
	:arg population: the population of Observations tocompute k-means on.
	:type population: Observation[]
	:param max_iteration: the number maximum of iteration we allow
	:type max_iteration: int
	:param centroids: the initial positions of centroids
	:type controids: Observation[]
	:param display: if True, the first and the second coordinate of the 
		populations are displayed setep by step
	:type display: boolean
	:arg title: title to print on top of the figures
	:type title: String
	:return: a table of centroids and a table of affectations
	:rtype: Observation[][]
	"""

	
	dimension = len(population[0].values)
	


#=============================================================================#
#						Phase 1 : Initialisation 							  #
#=============================================================================#

	if centroids == None:
		
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
		es.display(population,None,title + "Population : ",False)
	
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
			es.display(population,centroids,title +\
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
		es.display(population,centroids,title + "K-means computed",True)

	return [centroids,affectation]



if __name__ == '__main__':
	"""
	:option -d: True if you want to display the algorithm steps
	:option -a: Set the value og g-means alpĥa (significance level)
	:option -k: initialisation of the k in k-means or g-means algorithm.
	:option -g: if False, single k-mean is launch
	"""
	
	#Set the default options:
	options={"-k":"1","-d":False,"-g":"True","-a":"0.001"}

	#Read the options: 
	i=1
	while i <len(sys.argv):
	    if sys.argv[i] in options:
	        options[sys.argv[i]]=sys.argv[i+1]
	        i+=1
	    i=i+1

	#Process the options
	display = False
	k = int(options["-k"])
	alpha = float(options["-a"])

	#Setting the display option
	if options["-d"] == "True":
		display = True

	#Getting the population
	population = es.read_kmeans_input()

	if options["-g"] == "True":

		#Computing g-means
		compute_gmeans(population,display=display, k=k, alpha = alpha)

	else:

		#computing k-means
		compute_kmeans(k, population, display = (options['-d']))
	