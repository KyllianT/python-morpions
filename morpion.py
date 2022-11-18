import time

#dictionnaire associant une valeur à chaque symbole
valeur = {' ':0,'O':3,'X':5}

#definir la fonction ecriture_possible qui retourne comme parametre grille et chaine
def ecriture_possible(grille,chaine):
    # assigner pos a Faux
    pos = False
    # assigner lig a int qui contient le tableu chaine avec l'index 0
    lig = int(chaine[0])
    # assigner col a int qui contient le tableu chaine avec l'index 1
    col = int(chaine[1])
    # Si le tableau grille contenant lig et col est egale a aucune valeur
    if grille[lig][col] == ' ':
        #Alors pos est egale a VRAI 
        pos = True
        #retourné pos
    return pos

#definir la fonction ecriture qui retourne comme parametre grille,chaine et symbole 
def ecriture(grille,chaine,symbole):
    # assigner lig a int qui contient le tableu chaine avec l'index 0
    ligne = int(chaine[0])
    # assigner col a int qui contient le tableu chaine avec l'index 1
    colonne=int(chaine[1])
    #Assigne le tableau grille contenant ligne et colonne a symbole 
    grille[ligne][colonne]=symbole
    #Retourné le tableau grille 
    return grille

#definir la fonction alignement_ligne qui retourne comme parametre grille
def alignement_ligne(grille):
    # Assigner aligne a la valeur 0 
    aligne = 0
    # Pour chaque i ranger en 3 
    for i in range(3):
        #assigier somme a la valeur 0
        somme = 0
        #Pour chaque J ranger en 3 
        for j in range(3):
            #assigner symbole aux tableau grille avec ses parametre i et J
            symbole = grille[i][j]
            #assigner somme a somme plus au tableau valeur avec symbole dedans 
            somme = somme + valeur[symbole]
        #SI somme est egale a la valeur 15 ou a la valeur 9 
        if somme == 15 or somme == 9 :
            #alors assigne alige a la valeur 1 
            aligne = 1
    #retourné aligne 
    return aligne

#definir alignement_colonne qui vas retoiurné comme parametre grille
def alignement_colonne(grille):
    #alors assigne alige a la valeur 0
    aligne = 0
    #Pour chaque J ranger en 3
    for j in range(3):
        #assigne somme a la valeur 0 
        somme = 0
        #pour chaque i ranger en 3 
        for i in range(3):
            #assigner symbole aux tableau grille avec ses parametre i et J
            symbole = grille[i][j]
            #assigner somme a somme plus au tableau valeur avec symbole dedans 
            somme = somme + valeur[symbole]
        #SI somme est egale a la valeur 15 ou a la valeur 9 
        if somme == 15 or somme == 9 :
            #alors assigne alige a la valeur 1 
            aligne = 1
    #retourné aligne 
    return aligne

#definir alignement_diag1 qui vas retoiurné comme parametre grille
def alignement_diag1(grille):
    #Assigner aligne a la valeur 0 
    aligne = 0
    #Assigier somme a la valeur 0
    somme = 0
    #pour chaque i ranger en 3 
    for i in range(3):
        #assigner symbole aux tableau grille avec ses parametre i et i
        symbole = grille[i][i]
        #assigner somme a somme plus au tableau valeur avec symbole dedans 
        somme = somme + valeur[symbole]
    #SI somme est egale a la valeur 15 ou a la valeur 9 
    if somme == 15 or somme == 9 :
        #alors assigne alige a la valeur 1 
        aligne = 1
    #retourné aligne 
    return aligne

#definir alignement_diag1 qui vas retoiurné comme parametre grille
def alignement_diag2(grille):
    #Assigner aligne a la valeur 0 
    aligne = 0
    #Assigier somme a la valeur 0
    somme = 0
    #pour chaque i ranger en 3 
    for i in range(3):
        #assigner symbole aux tableau grille avec ses parametre i et 2 - i
        symbole = grille[i][2-i]
        #assigner somme a somme plus au tableau valeur avec symbole dedans 
        somme = somme + valeur[symbole]
    #SI somme est egale a la valeur 15 ou a la valeur 9 
    if somme == 15 or somme == 9 :
        #alors assigne alige a la valeur 1 
        aligne = 1
    #retourné aligne 
    return aligne

#definir alignement qui vas retoiurné comme parametre grille
def alignement(grille):
    # assigner aligne a alignement_ligne + alignement_colonne
    # + alignement_diag1 + alignement_diag2 qui possède tous le parametre grille
    aligne = alignement_ligne(grille)+alignement_colonne(grille)+alignement_diag1(grille)+alignement_diag2(grille)
    #SI aligne est egale a 1 
    if aligne == 1 :
        #alors afficher message  "trois symboles alignés! le jeu est fini."
        print("trois symboles alignés! le jeu est fini.")
        #retourné VRAI 
        return True
    #Sinon
    else :
        #retourné Faux 
        return False


    #################################################    corps du programme    #################################################
def JcJ():

    #construction d'une grille vide
    grille= []
    #pour chaque i ranger en 3 
    for i in range(3):
        #inisialiser ligne au tabeau
        ligne=[]
        #pour chaque j ranger en 3 
        for j in range(3):
            #ajouté append a ligne qui retourne rien
            ligne.append(' ')
        #ajouté append a grille qui retourne ligne
        grille.append(ligne)
    # assigner le joueurs a chaque symbole
    joueur = {0:'O',1:'X'}


    #assigner tour a la valeur 0
    tour = 0
    compteTour = 0
    # fin est egale Faux
    fin = False
    #Tant que c'est pas egale a fin 
    while not fin :
        #alors correct est egale a FAUX
        correct = False
        #Tant que c'est pas egale a correct :
        while not correct :
            # assigner a la variable rep le retour de l'éxécution de la fonction input avec le message "Quelle case souhaitez-vous cocher ?\n"
            rep = input("Quelle case souhaitez-vous cocher ?\n")
            if not rep in ["00","01","02","10","11","12","20","21","22"]:
                print("veuillez ressaisir la demande")
            elif rep in ["00","01","02","10","11","12","20","21","22"]:
                # assigner la valeur correct a la fonctionecriture_possible qui retourne grille et rep
                correct = ecriture_possible(grille,rep)     
        # assigner dessin aux parametre joueur qui retourne "tour"
        dessin = joueur[tour]
        # assigner grille a la fonction ecriture qui retourne "grille, rep et dessin"
        grille = ecriture(grille,rep,dessin)
        #pour chaque i ranger en 3 
        for i in range(3):
            #afficher le message du parametre grille i
            print(grille[i])
        # assigner a la variable fin a la fonction alignement qui retourne "grille"
        fin = alignement(grille)
        #ajouté +1 a tour
        tour = (tour + 1)%2
        compteTour = compteTour + 1
        
        if compteTour == 9 :
            print("égalité")
            exit()

def JcIA():
    print("eifjgyehf")
    



#################################################    Regle du morpion    ################################################# 

#definir la fonction regle_morpion
def regle_morpion() :
    print("Bienvenue sur ce Morpion de qualité !\n")
    print(" \n")
    print("Je suis Morpious votre serviteur et guide sur ce morpion. Pour commencer, ce morpion fut créé par Kyllian et William. Mes 2 géniaux créateur. Ce Morpion vous propose une version joueur contre joueur et une version contre moi ! (attention je suis imbattable à ce jeu).\n")
    print(" \n")
    print("Les règles sont simple : \n")
    print("Le tableau est diviser un 9 cases. Ces 9 cases sont présentes sur des lignes et des colonnes nominées de 0 à 2. Pour 	afficher l’un de vos symboles ( X ou O) vous devrais mettre votre réponses sous cette forme: ligne – colonne (sans le tiré). \n")
    print("Par exemple si vous souhaité mettre votre symbole au milieux vous devrait taper : 11 (1 = ligne, 1 = colonne)\n")
    print("Si vous souhaité mettre votre symbole en haut a droite vous devrait taper : 02 (0 = ligne, 2 = colonne)\n")
    print("/!\  Aucune triche n’est autorisé de ta part  /!\ \n")
    print("Le premier à aligner 3 symboles gagne la partie ! \n")
    print(" \n")
    print(" Tu es prés ?\n")
    mode = input(" Appuis envoie donc 1 pour jouer en Joueur contre Joueur ou 2 pour jouer contre Moi (IA)\n")
    if mode == "1":
        print ("Félicitation vous avez choisi de jouer entre vous j'espere qu'apres cette partie votre amitié sera toujours intacte <3 ")
        time.sleep (2)
        JcJ()
    elif mode == "2":
       print ("Félicitation vous avez choisi de jouer contre moi je vais te briser ! ")
       time.sleep (2)
       JcIA()


regle_morpion()
