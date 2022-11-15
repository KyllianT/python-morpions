def ecriture_possible(grille,chaine):
    pos = False
    lig = int(chaine[0])
    col = int(chaine[1])
    if grille[lig][col] == ' ':
        pos = True
    return pos

def ecriture(grille,chaine,symbole):
    ligne = int(chaine[0])
    colonne=int(chaine[1])
    grille[ligne][colonne]=symbole
    return grille

def alignement_ligne(grille):
    aligne = 0
    for i in range(3):
        somme = 0
        for j in range(3):
            symbole = grille[i][j]
            somme = somme + valeur[symbole]
        if somme == 15 or somme == 9 :
            aligne = 1
    return aligne

def alignement_colonne(grille):
    aligne = 0
    for j in range(3):
        somme = 0
        for i in range(3):
            symbole = grille[i][j]
            somme = somme + valeur[symbole]
        if somme == 15 or somme == 9 :
            aligne = 1
    return aligne

def alignement_diag1(grille):
    aligne = 0
    somme = 0
    for i in range(3):
        symbole = grille[i][i]
        somme = somme + valeur[symbole]
    if somme == 15 or somme == 9 :
        aligne = 1
    return aligne

def alignement_diag2(grille):
    aligne = 0
    somme = 0
    for i in range(3):
        symbole = grille[i][2-i]
        somme = somme + valeur[symbole]
    if somme == 15 or somme == 9 :
        aligne = 1
    return aligne

def alignement(grille):
    aligne = alignement_ligne(grille)+alignement_colonne(grille)+alignement_diag1(grille)+alignement_diag2(grille)
    if aligne == 1 :
        print("trois symboles alignés! le jeu est fini.")
        return True
    else :
        return False


## corps du programme

#construction d'une grille vide
grille= []
for i in range(3):
    ligne=[]
    for j in range(3):
        ligne.append(' ')
    grille.append(ligne)

#dictionnaire associant une valeur à chaque symbole
valeur = {' ':0,'O':3,'X':5}
joueur = {0:'O',1:'X'}

tour = 0
fin = False
while not fin :
    correct = False
    while not correct :
        rep = input("Quelle case souhaitez-vous cocher ?\n")
        correct = ecriture_possible(grille,rep)
    dessin = joueur[tour]
    grille = ecriture(grille,rep,dessin)
    for i in range(3):
        print(grille[i])
    fin = alignement(grille)
    tour = (tour +1)%2