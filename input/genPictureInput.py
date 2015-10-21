import genInput
import sys
import Image
from Ind import *

def genImage(path,x,y):
	population = []
	im=Image.open("./input/"+path)
	data = list(im.getdata())
	compteur=0
	nb_ind=0
	for i in range(x):
		for j in range(y):
			if data[compteur][1]>200 and (i>75 or j>50):
				population.append(Ind(2))
				population[nb_ind].set_values([j+0.,x-i+0.])
				nb_ind+=1
			compteur+=1
	print("nb de pixels actifs : "+str(nb_ind))
	genInput.write(population,2)



if __name__ == '__main__':
	filename = str(sys.argv[1])
	x = int(sys.argv[2])
	y = int(sys.argv[3])
	genImage(filename,x,y) 