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

	def set_values(self, values):
		self.values=values

	def __init__(self,length,type="data"):
		self.values=[]
		self.length=length
		self.type = type
		self.weight=0
		for i in range(length):
			self.values.append(random.random())

	def __eq__(self, Observation):
		if Observation is None:
			return False
		if not isinstance(Observation, Observation):
			return False
		if not self.length == Observation.length:
			return False
		for i in range(self.length):
			if not self.values[i]==Observation.values[i]:
				return False
		return True

	def dist(self,Observation):
		somme=0
		for i in range(self.length):
			somme+=(float(self.values[i])-float(Observation.values[i]))**2
		return sqrt(somme)

	def copy(self):
		i=Observation(self.length)
		i.set_values(self.values)
		return i

	def add(self,observation):
		for i in range(self.dimension):
			self.values[i] = (self.weight*self.value[i]+observation.value[i])/(self.weight+1)
			self.weight+=1