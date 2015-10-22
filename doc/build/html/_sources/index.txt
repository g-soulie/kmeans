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


Lorsqu'on lance kmeans, les données présentes dans le fichier *./input/input.csv* sont étudiées, et le résultat est écrit dans deux fichiers, *./output/affectation.csv* et *./output/centroids.csv*


Le fichier *genData.py* vous permet de générer un fichier input.csv. Vous pouvez générer différents type de données, à savoir : des :ref:`données aléatoires <random>`, des :ref:`données Iris <iris>` ou encore :ref:`La Bretagne vue du ciel <sky>`. Bien évidemment, vous pouvez utiliser l'algorithme avec un autre jeu de données de votre choix, pourvu que le fichier *input.csv* respecte le bon format (cf :ref:`Format des données <format>`).



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