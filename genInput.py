import commands
import es

def write(population,dimension):
	#Ecriture du fichier input.csv :
	data=[["# no_observation"]]
	for i in range(dimension):
		data[0].append("attribut_"+str(i))
	for i in range(len(population)):
		data.append([i])
		for j in range(dimension):
			data[i+1].append(population[i].values[j])
	commands.getoutput("mkdir ./input/")
	commands.getoutput("rm ./input/input.csv")
	es.write_data(data,'./input/input.csv')