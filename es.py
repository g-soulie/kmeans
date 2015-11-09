# -*- coding: utf-8 -*-

import random
import sys
from Observation import *
import matplotlib.pyplot as plt
import commands
import math
import warnings


#warnings are not displayed
warnings.filterwarnings("ignore")

def read_data(filename, skip_first_line = False, ignore_first_column = False):
    '''
    Loads data from a csv file and returns the corresponding list.
    All data are expected to be floats, except in the first column.
    
    :param filename: csv file name.
    :type filename: String
    
    :param skip_first_line: if True, the first line is not read.
        Default value: False.
    :type skip_first_line: boolean
    
    :param ignore_first_column: if True, the first column is ignored.
        Default value: False.
    :type ignore_first_column: boolean
    
    :return: a list of lists, each list being a row in the data file.
        Rows are returned in the same order as in the file.
        They contains floats, except for the 1st element which is a string
        when the first column is not ignored.
    :rtype: float[][]
    '''
    
    f = open(filename,'r')
    if skip_first_line:
        f.readline()
    
    data = []
    for line in f:
        line = line.split(",")
        line[1:] = [ float(x) for x in line[1:] ]
        if ignore_first_column:
            line = line[1:]
        data.append(line)
    f.close()
    return data

def write_data(data, filename):
    '''
    Writes data in a csv file.

    :param data: a list of lists to write
    :type data: float[][]
    :param filename: the path of the file in which data is written.
        The file is created if necessary; if it exists, it is overwritten.
    :type filename: String
    '''
    # If you're curious, look at python's module csv instead, which offers
    # more powerful means to write (and read!) csv files.
    f = open(filename, 'w')
    for item in data:
        f.write(','.join([str(x) for x in item]))
        f.write('\n')
    f.close()
        
def read_kmeans_input():
    """
    This fonction reads the file "input.csv" within the input folder

    :return: population based on the input file
    :rtype: Observation[]
    """
    population=[]
    data = read_data('./input/input.csv',ignore_first_column = True,skip_first_line = True)
    dimension=len(data[0])
    for i in range(len(data)):
        population.append(Observation(dimension))
        population[i].set_values(data[i])
    return population

def write_kmeans_output(population,centroids,affectation):
    """
    This fonction writes the files *affectation.csv* and *centroids.csv* in the output folder.

    :type   population: Observation[]
    :arg    population: set of observations
    :type   centroids: Observation[]
    :arg    centroids: set of centroids
    :type   affectation: int[]
    :arg    affectation: list of the observation's centroid label 
    :rtype: void
    """
    dimension = len(population[0].values)

    #Ecriture du fichier centroid.csv :
    data=[["# no_centre"]]
    for i in range(dimension):
        data[0].append("attribut_"+str(i))
    for i in range(len(centroids)):
        data.append([i])
        for j in range(len(centroids[i].values)):
            data[i+1].append(centroids[i].values[j])
    commands.getoutput("mkdir ./output/")
    commands.getoutput("rm ./output/centroids.csv")
    write_data(data,'./output/centroids.csv')

    #Ecriture du fichier affectation.csv :
    data=[["# no_observation"]]
    for i in range(dimension):
        data[0].append("attribut_"+str(i))
    data[0].append("no_classe")
    for i in range(len(population)):
        data.append([i])
        for j in range(dimension):
            data[i+1].append(population[i].values[j])
        data[i+1].append(affectation[i])
    commands.getoutput("rm ./output/affectation.csv")
    write_data(data,'./output/affectation.csv')

def write_kmeans_input(population,dimension):
    """
    This function write the file *input.csv* in the input folder

    :arg population: the set of observation we want to compute
    :type population: float[][]

    """

    #get the dimension of the observations
    dimension = len(population[0].values)

    #create the table data to write
    data=[["# no_observation"]]
    for i in range(dimension):
        data[0].append("attribut_"+str(i))



    for i in range(len(population)):
        data.append([i])
        for j in range(dimension):
            data[i+1].append(population[i].values[j])

    #write the datas
    commands.getoutput("mkdir ./input/")
    commands.getoutput("rm ./input/input.csv")
    write_data(data,'./input/input.csv')

def display(population,centroids,title,keep):
    """
    This fonction is used to display the population and the centroids on a graph

    :type   population: observation[]
    :arg    population: set of observations
    :type   centroids: Observation[]
    :arg    centroids: set of centroids
    :type   title: String
    :arg    title: name of the graphic
    :arg    keep: if true, the figure stay open until the user close it
    :type   keep: boolean
    :rtype: void
    """

    

    plt.clf()
    plt.hold(True)
    x=[]
    y=[]
    xcentroids=[]
    ycentroids=[]
    
    #Add the observations to the figures
    for i in range(len(population)):
        x.append((population[i].values)[0])
    for i in range(len(population)):
        y.append((population[i].values)[1])
    plt.scatter(x,y,s=1)

    #Add the clusters to the figure
    if not centroids is None:
        for i in range(len(centroids)):
            xcentroids.append((centroids[i].values)[0])
        for i in range(len(centroids)):
            ycentroids.append(centroids[i].values[1])
        plt.scatter(xcentroids,ycentroids,s=100,c='red')


    plt.title(title)
    plt.xlabel('x')
    plt.ylabel('y')
    

    if keep:
        plt.ioff()
        plt.waitforbuttonpress(timeout=5)
        plt.savefig("output/'"+str(title)+"'.png")
    else:
        plt.waitforbuttonpress(timeout=0.005)
        

def display_histogramme(x,title=""):
    """
    display the histogramm of a vector

    :arg x: list to display
    :type x: float[]
    :param title: the title to display
    :type title: String
    :rtype: void
    """

    #number of bars
    nb_bins = math.sqrt(x.shape[0])

    #time to keep displayed 
    time = 4

    plt.clf()
    plt.hold(True)
    plt.title(title)
    plt.hist(x,nb_bins)
    plt.savefig("output/"+str(title)+".png")
    plt.waitforbuttonpress(timeout=time)

def display_Direction(centroid0,centroid1,k=None,cluster=None):
    """
    display the histogramm of a vector

    :arg centroid0: first centroid
    :type centroid0: Observation
    :arg centroid1: second centroid
    :type centroid1: Observation
    :param k: k of kmeans, for title
    :type k: int
    :param cluster: cluster whose direction is computed, for title
    :type cluster: int
    :rtype: void
    """


    dx = float(abs(centroid0.values[0]-centroid1.values[0]))
    dy = float(abs(centroid0.values[1]-centroid1.values[1]))

    if (centroid0.values[0]-centroid1.values[0])*(centroid0.values[1]-centroid1.values[1]) < 0:
        dy = -dy

    x = [(float(centroid0.values[0]+centroid1.values[0]))/2-1.5*dx,(float(centroid0.values[0]+centroid1.values[0]))/2+1.5*dx]
    y = [(float(centroid0.values[1]+centroid1.values[1]))/2-1.5*dy,(float(centroid0.values[1]+centroid1.values[1]))/2+1.5*dy]

    #time to keep displayed 
    time = 4

    plt.hold(True)
    plt.plot(x,y,c='red',linewidth=3)
    plt.waitforbuttonpress(timeout=time)
    plt.savefig("output/"+str(k)+str(cluster)+".png")

    

