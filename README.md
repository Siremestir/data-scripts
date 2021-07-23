# Scripts Data

**Auteur** : Swan Sauvegrain

**Date** : 23/07/2021

**Licence** : Libre d'utilisation à condition de crédit.

---

## Utilisation
L'écriture du script en lui-même se fait dans main.py. Ce fichier contient un exemple de script.
Les fichiers grid_lib, files_lib et instances sont des bibliothèques fournissant des fonctions utiles.
Chaque fonction est documentée, et commentée au besoin.
Cette bibliothèque ne supporte pour l'instant que la division 2/3 1/3 pour l'écriture de fichiers d'instance MOCA-I.

## grid_lib
Une "grille" est une liste de listes.
grid_lib contient 4 fonctions utiles pour travailler avec des listes ou des grilles. Ces fonctions sont :
 - normalize : normalise entre 1 et 0 toutes les valeurs de la liste à partir de l'index 1 ou 0.
 - uniformize : classifie certains individus d'une grille en une seule catégorie.
 - make_intervals : crée des intervalles utiles à la discrétisation de données.
 - discretize : discrétise les données quantitatives d'une grille selon un nombre de quantiles donné.

## files_lib
Cette bibliothèque fournit des fonctions pour importer et écrire des fichiers.
Certaines fonctions peuvent être utile en-dehors de MOCA-I, spécifiquement import_csv, write_csv ou import_tsv.
Les autres, write_test et write_training, servent spécifiquement à écrire des instances de rulemining pour MOCA-I.

IMPORTANT : write_test et write_training sont à utiliser en tandem, et dans un ordre précis.
write_training renvoie le tiers de données qu'il n'utilise pas, qui doit ensuite être passé en paramètre à write_test.
Si vous avez un doute, fiez-vous à l'example dans main.py.

## instances
Cette bibliothèque ne contient que des fonctions spécifiques à MOCA-I.
WARNING : instances ne permet pour l'instant de travailler qu'avec des tsv.
Il y a 4 fonctions :
 - parse_tsv_bin : parse un fichier tsv contenant des informations binaires (1 ou 0) dans une grille.
 - parse_tsv_quant : parse un fichier tsv contenant des informations quantitatives dans une grille, les normalise et les discrètise par ligne.
 - parse_tsv_bin_desc : parse un fichier tsv contenant des informations binaires (1 ou 0) et crée un fichier desc avec ces informations.
 - parse_tsv_quant_desc : parse un fichier tsv contenant des informations quantitatives, les normalise et les discrètise par ligne, et crée un fichier desc avec ces informations.