# -*- coding: utf-8 -*-
import es,sys
from Observation import *
import random
import matplotlib.image as mpimg
import commands



def gen_random_data(gaussiennes,dimension=2,\
	taille_population=1000):
	"""
	Génére des gaussiennes de dimension dimension, et de forme définies par
		l'argument gaussienne.

	:arg gaussiennes: dictionnaire des gaussiennes à générées, de la forme :
		{"gaussienne1":{"direction":[],centre[]}}
	:type gaussiennes: dictionnaire
	:param dimension: dimensions des observations
	:type dimension: int
	:rtype: void
	"""
	population = []

	#set the nb of points per gaussian
	n = int(taille_population / len(gaussiennes))
	
	#generate the gaussian
	compteur=-1
	for name in gaussiennes:
		compteur+=1
		for i in range(n):
			population.append(Observation(dimension))
			for j in range(dimension):
				population[i+compteur*n].values[j]=random.gauss(0.,1.)\
				*gaussiennes[name]["direction"][j]+gaussiennes[name]["centre"][j]

	#write the datas in input.csv
	es.write_kmeans_input(population,dimension)

def gen_iris_data():
	"""
	Génére les données de type iris

	:rtype: void
	"""

	#copy the saved iris data in input.csv
	commands.getoutput("cp ./input/.iris.csv ./input/input.csv")

def gen_picture_data(name):
	"""
	Génére les données en provenance d'une image placée dans le fichier input.

	:arg name: nom de l'image à analyser.
	:type name: String
	:rtype: void
	"""
	
	#read the image and get its size:
	image=mpimg.imread("./input/"+name)
	x=image.shape[0]
	y=image.shape[1]

	#begin a loop on each pixel of the picture
	population = []
	nb_Observation=0
	for i in range(x):
		for j in range(y):
			if image[i][j][1]>200 and (i>75 or j>50):
				population.append(Observation(2))
				population[nb_Observation].set_values([j+0.,x-i+0.])
				nb_Observation+=1
	print("nb de pixels actifs : "+str(nb_Observation))
	es.write_kmeans_input(population,2)


if __name__ == "__main__":
	"""
	Generate some input data for the kmeans algorithms.

	:option -type: type of generated data. Can be "random", "iris" or "picture"
	:option -name: name of the picture to load. require *-type picture*
	:option -s: number of the gaussian sample to load. require *-type random*


	"""
	options={"-type":"random","-name":"bretagne.jpg","-s":"1","-d":"False"}

	#Read and cast the options: 
	i=1
	while i <len(sys.argv):
	    if sys.argv[i] in options:
	        options[sys.argv[i]]=sys.argv[i+1]
	        i+=1
	    i=i+1

	options["-s"]=int(options["-s"])-1
	options["-d"]=bool(options["-d"])


	#Gaussians data generation case:
	if options["-type"] == "random":
		print("génération de donnée aléatoire...")
		gaussienne_sample=[]
		gaussienne_sample.append({"1":{"direction":[1,0.5],"centre":[1,1]},\
			"2":{"direction":[0.1,1],"centre":[0,0]}})
		gaussienne_sample.append({"1":{"direction":[1,0.5],"centre":[2,2]},\
			"2":{"direction":[0.1,1],"centre":[0,0]}})
		gaussienne_sample.append({"1":{"direction":[1,0.5],"centre":[-2,-2]},\
			"2":{"direction":[0.1,1],"centre":[0,0]},"3":{"direction":[1,0.5],"centre":[2,2]}})
		gen_random_data(gaussienne_sample[options["-s"]])
		print("... gaussiennes "+str(options["-s"]+1)+" générées.")

	#Iris data generation case:
	elif options["-type"] == "iris":
		print("generation des données iris...")
		gen_iris_data()
		print("... données iris générées.")

	#picture data generation case:
	elif options["-type"] == "picture":
		print("génération des données d'image...")
		gen_picture_data(options["-name"])
		print("... données d'image chargées.")

	if options["-d"]:
		es.display(es.read_kmeans_input(),None,"Generated datas :",True)
