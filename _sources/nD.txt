.. _random:
Générations aléatoires de données
===========================================================

Le fichier *genData.py* permet de générer des gaussiennes en dimension n, grâce à la commande suivante :

	.. code-block:: html

		python genData.py -type random

La méthode utilisée est alors gen_random_data, qui créé les gaussiennes

.. autofunction:: genData.gen_random_data

Plusieurs configurations de gaussiennes en 2 dimensions sont proposées en exemple.
Il est possible de changer l'exemple générer en utilisant l'option -s :

	.. code-block:: html

		python genData.py -type random -s 1

Il est également possible d'afficher les deux premières coordonnées des données générées avec l'option -d :

	.. code-block:: html

		python genData.py -type random -s 1 -d True
