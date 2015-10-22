.. _iris:
Les données Iris
==========================

Le fichier *genData.py* permet de générer les données iris, grâce à la commande suivante :

	.. code-block:: html

		python genData.py -t iris

La méthode utilisée est alors gen_iris_data, qui récupére en fait le fichier iris.csv déjà créé.

.. autofunction:: genData.gen_iris_data


Il est également possible d'afficher les deux premières coordonnées des données générées avec l'option -d :

	.. code-block:: html

		python genData.py -t iris -d True