# Projet par Louis-Théo WIRTH, création du doc. 15/10/24 15:30.

import time, random

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
    '''Demande la case, si elle est en dehors des positions définies, redemande
    
    Entrée:
        str (string): string de la question
        annulable (boolean optional): dit si on peut écrire 'Annuler' pour return annuler
        
    Sortie:
        nom_case (string): Annuler ou position de case'''
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
ia = int(input("Contre qui voulez vous jouer?\n0:Un autre joueur en local\n1:IA aléatoire:"))

placement = True
for joueur in range(2):
    if (ia != 0) and (joueur == 1):  # Si IA est activée (ia != 0) et que c'est le joueur 2 (IA), alors on continue.
        print("Placement des bateaux")  # Indique le début du placement des bateaux pour l'IA.
        for h in range(2,7):  # Parcourt les tailles de bateaux : 2, 3, 3, 4, 5.
            if h < 4:
                i = h  # Les bateaux de taille 2 ou 3.
            else:
                i = h-1  # Les bateaux de taille 3, 4, ou 5 (car deux bateaux de taille 3).
            
            condition_break = False  # Indicateur de sortie de la boucle de placement.
            dir = random.randint(0, 1)  # Direction aléatoire du bateau : 0 = horizontal, 1 = vertical.
            while True:  # Boucle infinie pour trouver une position valide pour placer le bateau.
                # Sélectionne une case de départ aléatoire sur la grille en fonction de la taille du bateau.
                case = (random.randint(0, 9-i+1), random.randint(0, 9-i+1))
                
                # Vérifie si la case de départ est libre (valeur "_").
                if grille_joueurs[joueur][case[0]][case[1]] == "_":
                    condition_break = True
                    for j in range(i):  # Vérifie si toutes les cases adjacentes pour le bateau sont libres.
                        if grille_joueurs[joueur][case[0]+j*dir][case[1]+j*(1-dir)] == "O":
                            condition_break = False  # Si une case est libre, on sort de la boucle de vérification.
                            break  # Sort de la boucle si une case est validée.
                if condition_break == True:  # Si une position valide est trouvée, on sort de la boucle while.
                    break

            # Place le bateau en remplissant les cases avec "O".
            for j in range(i):  # Remplit chaque case de la taille du bateau avec "O".
                grille_joueurs[joueur][case[0]+j*dir][case[1]+j*(1-dir)] = "O"  # Place "O" pour chaque case du bateau.
        print(afficher_grille(grille_joueurs[joueur]))
    else:

        print("Placement des bateaux")
        for h in range(2,7): # Pour avoir les tailles de bateaux : 2,3,3,4,5
            if h <4:
                i = h # 2, 3
            else:
                i = h-1 # 3, 4, 5
            print(afficher_grille(grille_joueurs[joueur])) # Afficher la grille vide pour aider le joueur à se repérer.
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
                    nom_case2 = demander_case(f"Position 2 : Quelle case choisissez-vous? Format lettre chiffre (i.e C4 H8), Espacée de {i-1} cases par rapport à {nom_case} ('Annuler' pour repositionner la 1ere case).",True)

                    if nom_case2 == "Annuler":
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
                        case2 = convert_case(nom_case2)
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
            # print(afficher_grille(grille_joueurs[joueur]))
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nAutre joueur!")

print("\n\n\n\n\n\n\n\n\n\nDebut de partie!")

joueur = 0
continuer = True # Variable de contrôle pour la boucle principale, qui permet de continuer le jeu
while continuer: # Boucle principale du jeu qui continue tant que 'continuer' est True
    print('Tour du joueur '+str(joueur+1)+'!')
    time.sleep(0.5)
    while True: # Boucle qui demande au joueur de choisir une case valide pour attaquer
        print(afficher_grille(grille_joueurs[1-joueur],True)) # Affiche la grille de l'adversaire (1-joueur) en masquant les informations cachées (True)
        if (ia != 0) and (joueur == 1):  # Si IA est activée (ia != 0) et que c'est le joueur 1 (IA), alors on continue.
            if ia == 1:  # Si l'IA est de niveau 1.
                while True: # Boucle pour s'assurer que la case est valable.
                    case = (random.randint(0,9),random.randint(0,9))
                    if (grille_joueurs[1-joueur][case[0]][case[1]] == 'O') or (grille_joueurs[1-joueur][case[0]][case[1]] == '_'): # Condition pour sortir de la boucle.
                        break
        else:
            nom_case = demander_case(f"Quelle case choisissez-vous d'attaquer? Format lettre chiffre (i.e C4 H8)")
            case = convert_case(nom_case)

        if grille_joueurs[1-joueur][case[0]][case[1]] == "O": # Si la case contient un "O" (cela signifie qu'un bateau est présent)
            grille_joueurs[1-joueur][case[0]][case[1]] = "@" # Marque la case comme touchée avec "@"
            print(afficher_grille(grille_joueurs[1-joueur],True))
            print("Touché!") # Indique au joueur que le coup a touché un bateau
            time.sleep(1) # Pause de 1 seconde pour donner du temps au joueur avant de continuer


            sum = 0 # Initialise la variable `sum` à 0 pour compter les cases restantes contenant "O" (non touchées)
            for i in range(len(grille_joueurs[1-joueur])): # Parcourt la grille du joueur pour vérifier s'il reste des cases contenant "O" (bateaux non touchés)
                for j in range(len(grille_joueurs[1-joueur][i])):
                    if grille_joueurs[1-joueur][i][j] == 'O': # Si une case contient encore "O", cela signifie qu'il reste un bateau
                        sum +=1
                        
            if sum == 0: # Si `sum` est égal à 0, cela signifie qu'il n'y a plus de cases "O" (tous les bateaux sont coulés)
                vainqueur = joueur # i pour avoir l'index du joueur. (affiche le joueur 1 à chaque fois, à régler)
                continuer = 0 # Met fin à la partie en réglant la variable `continuer` à 0 (faux)
            break # Sort de la boucle interne après un coup réussi (le joueur a touché un bateau)

        elif grille_joueurs[1-joueur][case[0]][case[1]] == "_": # Si la case contient un "_", cela signifie que c'est une case vide (coup manqué)
            grille_joueurs[1-joueur][case[0]][case[1]] = "X" # Marque la case comme manquée avec "X"
            print(afficher_grille(grille_joueurs[1-joueur],True)) # Affiche la grille de l'adversaire mise à jour après le coup manqué
            print("Manqué...") # Indique au joueur que le coup a manqué le bateau
            time.sleep(1) 
            break # Sort de la boucle interne après un coup manqué
        else: # Si la case ne contient ni "O" ni "_", cela signifie qu'elle à déjà attaquée
            print("Position invalide.")
    joueur = 1 - joueur # Pour alterner entre les deux joueurs (joueur 0 et joueur 1)


print("Le joueur "+str(vainqueur+1)+" gagne!")