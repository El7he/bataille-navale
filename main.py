# Projet par Louis-Théo WIRTH, création du doc. 15/10/24 15:30.

def afficher_grille(grille, cacher=False):
    '''Transforme la grille en entrée en grille de type string.

    Entrée:
        grille (array): liste contenant des string en fonction du type de case
                            _ - Case vide
                            O - Case bateau
                            X - Case vide attaquée
                            @ - Case bateau attaquée
        cacher (boolean): affiche ou non les cases bateau non attaquées

    Sortie:
        grille_str (string): string clair et printable.'''
    
    grille_str = "[_]"
    for i in range(len(grille[0])): # Ajouter le numéro de colonne
        grille_str += "["+chr(65+i)+"]" # Récupération de la lettre correspondante
    grille_str += "\n" # Retour à la ligne

    for i in range(len(grille)): # Parcourrir le tableau
        grille_str += "["+str(i+1)+"]" # Ajouter le numéro de ligne
        for j in range(len(grille[i])): # Parcourrir la ligne
            if cacher != True: # Si il est nécessaire de cacher les bateaux ou non
                grille_str += "["+grille[i][j]+"]" # Ajouter la valeur de la case entre crochets
            else:
                if grille[i][j] == "O":
                    grille_str += "["+"_"+"]" # Ajouter la valeur de la case entre crochets
                else:
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
    if (y>-1 and y<10) and (x>-1 and x<10):
        return (y,x) # y x car coordonées inversées
    else:
        return (-1,-1)
    
def signe(nb):
    '''Renvoie le signe d'un entier
    
    Entrée:
        nb (int): nombre
        
    Sortie:
        signe (int): 1 ou -1'''
    if nb!=0:
        return int(nb/abs(nb))
    else:
        return
    
def demander_case(str,annulable=False):
    nom_case = input(str)
    if annulable == True:
        if nom_case == "Annuler": return "Annuler"

    case = convert_case(nom_case)

    while (case[0]<0 or case[0]>10) or (case[1]<0 or case[1]>10):
        nom_case = input(str)
        case = convert_case(nom_case)
        print("Impossible, coordonée en dehors de la grille.")
    return nom_case

grille_joueurs = []
grille_joueurs.append(generer_grille(10,10)) # Générer les grilles des joueurs.
grille_joueurs.append(generer_grille(10,10))

placement = True
for joueur in range(2):
    print(afficher_grille(grille_joueurs[joueur])) # Afficher la grille vide pour aider le joueur à se repérer.

    print("Placement des bateaux")
    for h in range(2,7):
        if h <4:
            i = h
        else:
            i = h-1
        print(afficher_grille(grille_joueurs[joueur]))
        print("Placement du bateau de taille ",i) # Indique la taille du bateau à placer
        
        # Demande la première case de placement du bateau
        nom_case = demander_case("Position 1 : Quelle case choisissez vous? Format lettre chiffre (i.e C4 H8)")
        case = convert_case(nom_case) # Convertit l'entrée de la case en coordonnées (i.e. C4 -> (2, 3))
        while grille_joueurs[joueur][case[0]][case[1]] != "_":
            nom_case = demander_case("Position 1 : Quelle case choisissez vous? Format lettre chiffre (i.e C4 H8)")
            case = convert_case(nom_case)

        grille_joueurs[joueur][(case[0])][(case[1])] = "O" # Marque la première case choisie avec un "O" pour indiquer la présence d'un bateau
        continuer = False # Indique si le joueur peut continuer le placement ou s'il doit encore ajuster 

        while continuer == False: # Boucle jusqu'à ce que le placement du bateau soit valide
            print(afficher_grille(grille_joueurs[joueur]))
            # Boucle pour gérer la deuxième position ou annuler
            while True:
                nom_case = demander_case(f"Position 2 : Quelle case choisissez-vous? Format lettre chiffre (i.e C4 H8), Espacée de {i} cases par rapport à {nom_case} ('Annuler' pour repositionner la 1ere case).",True)

                if nom_case == "Annuler":
                    # Réinitialise la première case et redemande la saisie
                    grille_joueurs[joueur][case[0]][case[1]] = "_"  # Remet la première case à "_"
                    nom_case = demander_case("Position 1 : Quelle case choisissez-vous? Format lettre chiffre (i.e C4 H8)")
                    case = convert_case(nom_case)

                    # Vérifie que la case est valide et vide
                    while grille_joueurs[joueur][case[0]][case[1]] != "_":
                        nom_case = demander_case("Position 1 : Quelle case choisissez-vous? Format lettre chiffre (i.e C4 H8)")
                        case = convert_case(nom_case)

                    # Marque la case comme occupée
                    grille_joueurs[joueur][case[0]][case[1]] = "O"
                    print(afficher_grille(grille_joueurs[joueur]))

                else:
                    # Convertit la deuxième case si elle est valide
                    case2 = convert_case(nom_case)
                    break  # Sort de la boucle si la deuxième case est valide

            d = [(case[0]-case2[0]),(case[1]-case2[1])]  # Calcule la différence entre les deux cases choisies pour s'assurer que l'espacement est correct
            if d[1] == 0: # Vérifie si le bateau est placé verticalement (d[1] == 0)
                if abs(d[0])==i-1: # Vérifie si la distance entre les deux cases correspond à la taille du bateau
                    for j in range(i): # Remplit toutes les cases entre la case1 et case2 avec "O"
                        grille_joueurs[joueur][(case[0]-j*signe(d[0]))][(case[1])] = "O" 
                    continuer = True # Placement valide, sortie de la boucle
            elif d[0] == 0: # Vérifie si le bateau est placé horizontalement (d[0] == 0)
                if abs(d[1])==i-1: # Vérifie si la distance entre les deux cases correspond à la taille du bateau
                    for j in range(i): # Remplit toutes les cases entre la case1 et case2 avec "O"
                        grille_joueurs[joueur][(case[0])][(case[1]-j*signe(d[1]))] = "O" 
                    continuer = True # Placement valide, sortie de la boucle
            else:
                print("Placement invalide.")
print("\n\n\n\n\n\n\n\n\n\nDebut de partie!")
