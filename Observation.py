# -*- coding: utf-8 -*-
"""
Created on October 2015
@author: B.pacreau, G. Soulié
"""

from math import *
import random

class Observation:
	"""
    Représente une observation
    """

	def __init__(self,dimension):
		"""
		Create a new observation.

		:arg dimension: dimension of the observation
		:type dimension: int
		"""

		self.values = []
		self.dimension = dimension
		self.weight = 0.
		for i in range(dimension):
			self.values.append(0.)

	def add(self,observation):
		"""
		Add another observation values to self.values, with ponderation by self.weight.
		Typically use wen this instanciation of Observation is a centroid.
		This function permits to compute easily a barycentre of several observations

		:arg observation: the observation to add to the barycentre
		:type observation: Observation
		"""
		for i in range(self.dimension):
			self.values[i] = (self.weight*self.values[i]+observation.values[i])/(self.weight+1.)
		self.weight+=1.

	def set_values(self, values):
		"""
		set the values of the observation

		:arg values: valeurs de l'observation
		:type values: float[]
		:rtype: void
		"""
		for i in range(self.dimension):
			self.values[i] = values[i]

	def dist(self,observation):
		"""
		compute and return the euclidian distance between self \
			and another observation

		:arg observation: the observation to compute the distance with
		:type observation: Observation
		:rtype: float
		"""
		somme=0.
		for i in range(self.dimension):
			somme+=(self.values[i]-observation.values[i])**2
		return sqrt(somme)


	def copy(self):
		"""
		Return another obseration with the same values

		:rtype: Observation
		"""
		copy=Observation(self.dimension)
		copy.set_values(self.values)
		return copy

	def substract(self,observation):
		"""
		Return an obseration which is the substraction of self - observation

		:arg observation: the observation to compute substraction with
		:type observation: Observation
		:rtype: Observation
		"""
		sub=Observation(self.dimension)
		for i in range(self.dimension):
			sub.values[i] = self.values[i]-observation.values[i]
		return sub


