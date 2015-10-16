# kmeans
exemple de commentaire :
      """
      	This function is used to determine the index the index of a list of floats
      	@type	tab: list<float>
      	@param	tab: tableau de float quelconque
      	@rtype: int
      	@return:	the index of the minimum of the list tab.
      
      	"""

Ind.py : classe individu :
  un individu, c'est un objet ac une fonction distance et avec lequel on peut calculer des barycentres.
  typiquement, c'est ici en vecteur $values de taille $length
  la norme utilisée pour la distance est la norme 2
  il est initialisé aléatoirement, mais on peut en changer les valeurs grâce à set_values()
  
Bary.py : classe barycentre :
  permet de computer un barycentre d'individus
  possède une fonction init qui l'init et une fonction add, qui permet d'ajouter un $ind à barycentrer.
  
kmeans.py : fichier principal
  index_min(tab) : renvoie l'index du minimum d'un tableau $tab
  afficher(population,G,titre) : afficher (en 2D) une population (en bleue), des barycentres (en rouge) ac le titre $titre
  main : 
    initalise la population aléatoirement (gaussiennes autours de centroids)
    initalise les barycentres : sous ensemble aléatoire de la population à k individus
    reaffectation : affecte les individus aux barycentres les plus proches
    recalculation : recalcule les barycentres
  
    le critère d'arrèt concerne le changement des barycentres : 
      la variable $stop reste à true lorsque tous les barycentres ne changent pas lors de la phase de reaffectation.
      
