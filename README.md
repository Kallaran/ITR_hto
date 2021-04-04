# Rapport TP3 ITR

Jean Derieux - Alexys Guerin

## QuickStart 

script.py permet d'avoir les WCET de nos fonctions de detection/navigation.

main.py permet d'obtenir une illustration d'ordonnanceur Rate Monotonic ou Eerly Deadline First.

## Heptane 

Heptane est un outil donnée par nos encadrants. Il nous a permit d'analyser le programme que l'on donnait au robot.
Il est séparé en 2 commandes : 

* La première commande "HeptaneExtract" permet d'extraire les différents graphe de flot de contrôle que compose notre programme (fonction, loop, table de symbole,...) et les enregistrer dans un fichier XML sous la forme d'un arbre selon un fichier configuration Xml donné en entré (Dans notre cas, par nos encadrants).

* La deuxième commande "HeptaneAnalysis" elle aussi permet d'obtenir les différents CFG selon une configuration donnée mais va en plus ajouter les pires temps d'exécution (Worst Case Execution Time = WCET). Ces WCET sont des informations que nous utiliserons dans nos ordonnanceurs Rate Monotonic(RM) et Early Deadline First (EDF).

