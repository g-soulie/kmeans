# -*- coding: utf-8 -*-

import random
import sys
import Observation
import matplotlib.pyplot as plt
import commands

def read_data(filename, skip_first_line = False, ignore_first_column = False):
    '''
    Loads data from a csv file and returns the corresponding list.
    All data are expected to be floats, except in the first column.
    
    @param filename: csv file name.
    
    @param skip_first_line: if True, the first line is not read.
        Default value: False.
    
    @param ignore_first_column: if True, the first column is ignored.
        Default value: False.
    
    @return: a list of lists, each list being a row in the data file.
        Rows are returned in the same order as in the file.
        They contains floats, except for the 1st element which is a string
        when the first column is not ignored.
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

    @param data: a list of lists

    @param filename: the path of the file in which data is written.
        The file is created if necessary; if it exists, it is overwritten.
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

    :return population based on the input file
    :rtype: Observation[]
    """
    population=[]
    data = read_data('./input/input.csv',ignore_first_column = True,skip_first_line = True)
    dimension=len(data[0])-1
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


def display(population,centroids,title):
    """
    This fonction is used to display the population and the centroids on a graph

    :type   population: Observation[]
    :arg    population: set of observations
    :type   centroids: Observation[]
    :arg    centroids: set of centroids
    :type   titre: String
    :arg    titre: name of the graphic
    :rtype: void
    """
    x=[]
    y=[]
    xcentroids=[]
    ycentroids=[]
    for i in range(len(population)):
        x.append((population[i].values)[0])
    for i in range(len(population)):
        y.append(population[i].values[1])
    plt.scatter(x,y,s=1)
    if not centroids is None:
        for i in range(len(centroids)):
            xaffectation.append((centroids[i].values)[0])
        for i in range(len(centroids)):
            yaffectation.append(centroids[i].values[1])
        plt.scatter(xcentroids,ycentroids,s=100,c='red')
    plt.title(title)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.savefig('ScatterPlot.png')
    plt.show()
