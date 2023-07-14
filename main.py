"""import pydandic
from pydantic import BaseModel
from pydantic import datetime



class Post(BaseModel):
    date : datetime
    comment : str
    like : int
    smile : int
    heart : int
    reaction : int

#me : 
def reaction_order(posts):
    L=[]
    for i in posts:
        L.append(i)
    L.sort("reaction", reverse=True) #utilisation de "réaction" comme clé comme ça faux, user chat en bas
    return L

def get_reaction(posts):
    return posts[:]["reaction"]


#chat :
def reaction_order(posts):
    posts.sort(key=lambda x: x["reaction"], reverse=True)
    return posts
"""
##me
import csv
import json

chemin = 'C:/Users/SIA-3/Desktop/projets/OdeCloud/ex_post.csv'

def comment_order(chemin):
    chemin.sort(key = lambda x: x["nb_comment"], reverse = True)

def comment_count():
    global nb_com
    nb_com = []
    with open(chemin, 'r') as fichier:
        lecteur_csv = csv.reader(fichier)
        first_line = next(lecteur_csv)
    

    i=0 # initialisation de l'indice pour rechercher "comment" dans la ligne, j'imagine qu'on a les commentaires après le = séparés par des "";"" (exemple : comment = "bienvenu !"" ; "bienvenu nossa" ; "bienvenu parmi nous" ;
    res = first_line[i] #res signifie research
    while res != "comments":
        i += 1
        res = first_line [i]
    s = 0 # on sait ici que le mot comment se trouve en ligne[i]
    for line in lecteur_csv[1:]:
        for element in line[i:]: #element va de ligne[i] à la fin...
            index = element.find(";") # on va compter tous les ";"
            if index != -1:
                s+=1
        nb_com.append(s) #on obtient une colonne contenant le nombre de commentaire de chaque post, dasn le meme ordre que le fichier csv
    return nb_com

comment_count()
print(nb_com)

csv_dict = [] #transformation de ma liste csv en dictionnaire
with open(chemin, 'r') as fichier:
    lecteur_csv = csv.DictReader(fichier)
    i = 0 # indice pour etre en phase avec les éléments de nb_com
    for line in lecteur_csv: #ligne se balade dans fichier converti en fictionnaire (lecture comme si c'était un dict)
        csv_dict.append(dict(line, nb_com = nb_com[i]))
        i += 1 

posts_tries = comment_order(csv_dict)
print(posts_tries)









