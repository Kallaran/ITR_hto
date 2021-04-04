# Rapport TP3 ITR

Jean Derieux - Alexys Guerin

## QuickStart 

Il faut installer svgwrite : pip3 install svgwrite

python3 script.py : permet d'avoir les WCET de nos fonctions de detection/navigation.

python3 main.py : permet d'obtenir une illustration d'ordonnanceur Rate Monotonic ou Early Deadline First (Choix en commentant/décommentant dans le code : lignes 36/37 fichier main.py). 

## Heptane 

Heptane est un outil donné par nos encadrants. Il nous a permis d'analyser le programme que l'on donnait au robot.
Il est séparé en 2 commandes : 

* La première commande "HeptaneExtract" permet d'extraire les différents graphes de flot de contrôle que compose notre programme (fonction, loop, table de symbole,...) et les enregistrer dans un fichier XML sous la forme d'un arbre selon un fichier configuration Xml donné en entrée (Dans notre cas, par nos encadrants).

* La deuxième commande "HeptaneAnalysis" elle aussi permet d'obtenir les différents CFG selon une configuration donnée mais va en plus ajouter les pires temps d'exécution (Worst Case Execution Time = WCET). Ces WCET sont des informations que nous utiliserons dans nos ordonnanceurs Rate Monotonic(RM) et Early Deadline First (EDF).

## Dans notre TP

Nous avons d'abord voulu tester notre RM et EDF avec les valeurs de Ci, Pi, Di du cours pour vérifier les résultats.
> EDF du cours 
![](https://i.imgur.com/XDUPPqP.png)

> RM du cours
![](https://i.imgur.com/4y2yhJy.png)

Les schémas étant bien les résultats attendus. On a voulu tester avec nos valeurs mais l'un de nos WCET était beaucoup trop grand: 

![](https://i.imgur.com/DXmLhqi.png)

Nous avons donc récupéré une valeur de WCET de la tâche navigation d'un camarade. Et pour s'adapter à notre méthode d'illustration, nous avons aussi dû diviser par 10 toutes nos valeurs et avons considéré que DI=PI.

[Navigation, contact,distance]
Di = [20,10,30] 
Ci = [3,3,3]
Pi = [20,10,30]

On obtient au final un même schéma pour RM et EDF.

Et dans cette configuration toutes les deadlines sont respectées.
(Dans le cas contraire un message est print dans le terminal pour spécifier à quel(s) instant(s) les échéances ont été dépassées.)

![](https://i.imgur.com/7toG0PV.png)


