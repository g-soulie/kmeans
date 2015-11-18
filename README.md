# kmeans

Welcome in this repository about a k-means implementation. 

Please visit the documentation page if you want to have a larger view of this project :

http://g-soulie.github.io/kmeans/

Installation
-----------------

On a linux terminal, you only need to type the following commands to get our code.

    git clone http://github.com/g-soulie/kmeans


Generating datas
-----------------------------
You can start by generate data. Three type of data can easily be genrated :

<b>Random gaussians datas</b>

    python genData.py -type random
  
<b>Iris datas </b>

    python genData.py -type iris
  
<b>Datas from pictures </b> (picture should be placed in the input folder)

    python genData.py -type picture -name name_of_your_picture
    
For each kind of data, you can display the first two coordinate of these by adding the option -d true.
Each of these commands will create a file ./input/input.csv ad hoc.

Computing kmeans
----------------------------
Once you have done it, run

    python kmeans.py

It will compute a k-means algorithms on the file ./input/input.csv
The two output files are ./output/affectation.csv and ./output/centroids.csv

You can set the number of centroids (the k) by adding for example -k 10
Once again, you can display the algorithms with the option -d True

Remeber to visit http://g-soulie.github.io/kmeans/ if you have any question.
