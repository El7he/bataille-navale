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
        grille_str += "["+chr(65+i)+"]" # Récupération de la lettre correspondante
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

def convert_case(case):
    '''Transforme un str de case en position utilisable
    
    Entrée:
        case (str): position de la case
        
    Sortie:
        pos (tuple, int): position correspondante dans la grille'''
    x = int(ord(case[0])-65)
    y = int(case[1:])-1
    return (y,x) # y x car coordonées inversées

grille_joueurs = []
grille_joueurs.append(generer_grille(10,10)) # Générer les grilles des joueurs.
grille_joueurs.append(generer_grille(10,10))

placement = True
while placement:
    print(afficher_grille(grille_joueurs[0])) # Afficher la grille vide pour aider le joueur à se repérer.
    case = convert_case(input("Quelle case choisissez vous? Format lettre chiffre (i.e C4 H8)"))
    print(case)
    grille_joueurs[0][case[0]][case[1]] = "X" # Système temporaire selection de cases
    