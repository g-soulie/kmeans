.. K_means documentation master file, created by
   sphinx-quickstart on Tue Oct 20 21:58:03 2015.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Documentation du projet K-means :
===========================================================

L'ensemble des sources de ce projet est disponible sur github_ :


Sous linux, vous pouvez facilement l'importer en tapant : 

	.. code-block:: python

		git clone http://github.com/pikkendorff/kmeans

L'architecture générale du projet est la suivante :


	.. code-block:: html

		  ./kmeans/
			|--doc/
			|--input/
			|    |--input.csv
			|    |--bretagne.jpg
			|    |--.iris.csv
			|--output/
			|    |--affectation.csv
			|    |--centroids.csv
			|--kmeans.py
			|--es.py
			|--genData.py
			|--Observation.py


Le fichier *kmeans.py* vous permet de lancer les algorithmes kmeans et gmeans. Les algorithmes se lancent avec la commande suivante : 

	.. code-block:: html

		python kmeans.py [-options] options

Les options disponibles sont les suivantes : 

	-d 		Si True, illustre l'algorithme à l'écran. Défaut : False.
	-g 		Si False, un simple kmeans est lancé. Défaut True : gmeans est lancé.
	-k 		k de kmeans. Si g-means est lancé, k d'initialisation de gmeans.  Défaut : 1.
	-a 		Significance level of the gaussian test (pour gmeans).


Lorsqu'on lance kmeans, les données présentes dans le fichier *./input/input.csv* sont étudiées, et le résultat est écrit dans deux fichiers, *./output/affectation.csv* et *./output/centroids.csv*


Le fichier *genData.py* vous permet de générer un fichier *input.csvù*. Vous pouvez générer différents type de données, à savoir : des :ref:`données aléatoires <random>`, des :ref:`données Iris <iris>` ou encore :ref:`La Bretagne vue du ciel <sky>`. Bien évidemment, vous pouvez utiliser l'algorithme avec un autre jeu de données de votre choix, pourvu que le fichier *input.csv* respecte le bon format (cf :ref:`Format des données <format>`). La génération se fait grâce à la commande suivante :

	.. code-block:: html

		python genData.py [-options] options

Les options disponibles sont les suivantes : 

	-d 		Si True, illustre les données générées à l'écran. Défaut : False.
	-t 		Type. "random", "iris" ou "picture"
	-n 		Name. Si le type est "picture", va chercher l'image ainsi nommé dans le dossier input.
	-s 		Sample. Si le type est random, permet de générer plusieurs exemples de gaussiennes.


Le fichier *es*.py rassemble l'ensemble des fontions nécessaires au traitement des données, tandis que la classe Observation (*Observation.py*) implémente les observation.





.. toctree::

   introduction
   kmeans
   gmeans
   Observation
   impl
   data
   nD
   iris
   sky


* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

.. _github: http://github.com/pikkendorff/kmeans