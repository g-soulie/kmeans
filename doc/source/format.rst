.. _format:
Format des données
================================

Les formats suivants de fichiers sont à respecter :


Le fichier des données d’entrée
--------------------------------------------
./input/input.csv doit respecter le format suivant :

	.. code-block:: html

		# no_observation,attribut_1,attribut_2,...,attribut_p
		1,0.1,0.8,0.4,0.3
		2,0.3,0.7,0.5,0.2
		3,0.9,0.6,0.7,0.1
		4,0.4,0.2,0.8,0.3


Le fichier des données affectées
--------------------------------------------
./output/affectation.csv respecte le format suivant :

	.. code-block:: html

		# no_observation,attribut_1,attribut_2,...,attribut_p,no_classe
		1,0.1,0.8,0.4,0.3,3
		2,0.3,0.7,0.5,0.2,2
		3,0.9,0.6,0.7,0.1,1
		4,0.4,0.2,0.8,0.3,3


Le fichier des centres
-------------------------------------------
./output/centroid.csv respecte le format suivant :

	.. code-block:: html

		# no_centre,attribut_1,attribut_2,...,attribut_p
		1,0.2,0.3,0.4,0.5
		2,0.3,0.2,0.6,0.4
		3,0.1,0.9,0.5,0.3