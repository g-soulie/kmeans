Implémentation de k-means
===============================================

.. module:: kmeans

Pour implémenter l'algorithme kmeans, nous avons utilisé deux fichiers : 
kmeans.py et Observation.py

Le fichier kmeans contient la focntion compute_kmeans
	

La fonction compute_kmeans
--------------------------------------------

.. autofunction:: kmeans.compute_kmeans

compute_kmeans fait appel au fichier es.py qui regroupe l'ensemble des
opérations d'écriture, de lecture et d'affichages des :ref:`données <data>`

.. code-block:: python

	population = es.read_kmeans_input()
	dimension = len(population[0].values)

Phase 1 - Initialisation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

		.. code-block:: python


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
			if display:
				es.display(population,None,"Population : ")
			
			#Loop stop condition initialisation:
			stop=False
			

			iteration = 0
			while not stop and iteration < max_iteration:
				iteration+=1

Phase 2 - Affectation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

		.. code-block:: python


			#if display, we print the population and the centroids
			if display:
				es.display(population,centroids,"computing k-means : \
					iteration "+str(iteration))

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



Phase 3 - Calculation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

		.. code-block:: python


			#Compute the new centroids
			for j in range(k):
				centroid = Observation(dimension,type="centroid")
				for i in range(len(population)):
					if affectation[i]==j:
						centroid.add(population[i])
				centroids[j]=centroid



.. code-block:: python

	#write the output files
	es.write_kmeans_output(population,centroids,affectation)

	#if display, we print the population and the centroids
	if display:
		es.display(population,centroids,"K-means computed")






