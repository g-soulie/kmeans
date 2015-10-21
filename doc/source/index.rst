.. K_means documentation master file, created by
   sphinx-quickstart on Tue Oct 20 21:58:03 2015.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Documentation du projet K-means :
===========================================================

L'ensemble des sources de ce projet est disponible sur github_ :


Sous linux, vous pouvez facilement l'importer en tapant : 

	.. code-block:: python

		mkdir kmeans/
		cd kmeans
		git init
		git remote http://github.com/pikkendorff/kmeans master

L'architecture générale du projet est la suivante :


	.. code-block:: html

		  ./kmeans/
			|--doc/
			|--input/
			|    |--input.csv
			|    |--bretagne.jpg
			|    |--genInput.py
			|    |--genAleatoire.py
			|    |--genIris.py
			|    |--genPicture.py
			|--output/
			|    |--affectation.csv
			|    |--centroids.csv
			|--kmeans.py
			|--es.py
			|--Observation.py


Lorsqu'on lance kmeans, les données présentes dans le fichier *./input/input.csv* sont étudiées, et le résultat est écrit dans deux fichiers, *./output/affectation.csv* et *./output/centroids.csv*


Les fichiers *{genAleatoire*, *genIris* et *genPicture}.py* vous permettent de générer un fichier input.csv corrsespondant respectivement aux sections :ref:`Données aléatoires <random>`, :ref:`Données Iris <iris>` et :ref:`La Bretagne vue du ciel <sky>`. Bien évidemment, vous pouvez utiliser l'algorithme avec un autre jeu de données de votre choix, pourvu que le fichier *input.csv* respecte le bon format (cf :ref:`Format des données <format>`).



Table des matières
====================================

.. toctree::


   introduction
   kmeans
   impl
   format
   nD
   iris
   sky




* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

.. _github: http://github.com/pikkendorff/kmeans