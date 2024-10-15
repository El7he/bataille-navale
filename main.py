# Projet par Louis-Théo WIRTH, création du doc. 15/10/24 15:30.

def afficher_grille(grille):
    '''Transforme la grille en entrée en grille de type string.

    Entrée:
        grille (array): liste contenant des string en fonction du type de case
                            _ - Case vide
                            O - Case bateau
                            X - Case vide attaquée
                            @ - Case bateau attaquée

    Sortie:
        grille_str (string): string clair et printable.'''
    
    grille_str = "[_]"
    for i in range(len(grille[0])): # Ajouter le numéro de colonne
        grille_str += "["+chr(65+i)+"]"
    grille_str += "\n" # Retour à la ligne

    for i in range(len(grille)): # Parcourrir le tableau
        grille_str += "["+str(i+1)+"]" # Ajouter le numéro de ligne
        for j in range(len(grille[i])): # Parcourrir la ligne
            grille_str += "["+grille[i][j]+"]" # Ajouter la valeur de la case entre crochets
        grille_str += "\n" # Retour à la ligne une fois la colonne finie
    return grille_str

def generer_grille(l,h):
    '''Génère une grille de la taille l x h.
    
    Entrée:
        l (int): longeur
        h (int): largeur
        
    Sortie:
        grille (array): matrice remplie de _.'''
     
    grille = []
    for i in range(l):
        temp = [] # création/réinitialisation d'une variable temporaire
        for j in range(h): # obligé de recommencer à chaque fois car sinon les cases partageront le même espace mémoire. Voir pb1.png, une seule case changée dans les deux cas testés.
            temp.append("_") # ajout des cases vides
        grille.append(temp) # ajout des listes
    return grille

grille = generer_grille(10,10)
grille[1][2] = "X"
print(afficher_grille(grille))    