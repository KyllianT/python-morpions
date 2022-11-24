#importer la bibliothéque time

#dictionnaire associant une valeur à chaque symbole

#definir la fonction ecriture_possible qui retourne comme parametre grille et cha
    # assigner pos a Faux
    # assigner lig a int qui contient le tableu chaine avec l'index 0
    # assigner col a int qui contient le tableu chaine avec l'index 1
    # Si le tableau grille contenant lig et col est egale a aucune valeur
        #Alors pos est egale a VR
        #retourné pos

#definir la fonction ecriture qui retourne comme parametre grille,chaine et symbole 
    # assigner lig a int qui contient le tableu chaine avec l'index 0
    # assigner col a int qui contient le tableu chaine avec l'index 1
    #Assigne le tableau grille contenant ligne et colonne a symbole 
    #Retourné le tableau grille 

#definir la fonction alignement_ligne qui retourne comme parametre grille
    # Assigner aligne a la valeur 0 
    # Pour chaque i ranger en 3 
        #assigier somme a la valeur 0
        #Pour chaque J ranger en 3 
            #assigner symbole aux tableau grille avec ses parametre i et J
            #assigner somme a somme plus au tableau valeur avec symbole dedans 
        #SI somme est egale a la valeur 15 ou a la valeur 9 
            #alors assigne alige a la valeur 1 
    #retourné align

#definir alignement_colonne qui vas retoiurné comme parametre grille
    #alors assigne alige a la valeur 0
    #Pour chaque J ranger en 3
        #assigne somme a la valeur 0 
        #pour chaque i ranger en 3 
            #assigner symbole aux tableau grille avec ses parametre i et J
            #assigner somme a somme plus au tableau valeur avec symbole dedans 
        #SI somme est egale a la valeur 15 ou a la valeur 9 
            #alors assigne alige a la valeur 1 
    #retourné aligne 

#definir alignement_diag1 qui vas retoiurné comme parametre grille
    #Assigner aligne a la valeur 0 
    #Assigier somme a la valeur 0
    #pour chaque i ranger en 3 
        #assigner symbole aux tableau grille avec ses parametre i et i
        #assigner somme a somme plus au tableau valeur avec symbole dedans 
    #SI somme est egale a la valeur 15 ou a la valeur 9 
        #alors assigne alige a la valeur 1 
    #retourné aligne 

#definir alignement_diag1 qui vas retoiurné comme parametre grille
    #Assigner aligne a la valeur 0 
    #Assigier somme a la valeur 0
    #pour chaque i ranger en 3 
        #assigner symbole aux tableau grille avec ses parametre i et 2 - i
        #assigner somme a somme plus au tableau valeur avec symbole dedans 
    #SI somme est egale a la valeur 15 ou a la valeur 9 
        #alors assigne alige a la valeur 1 
    #retourné aligne 

#definir alignement qui vas retoiurné comme parametre grille
    # assigner aligne a alignement_ligne + alignement_colonne
    # + alignement_diag1 + alignement_diag2 qui possède tous le parametre grille
    #SI aligne est egale a 1 
        #alors afficher message  "trois symboles alignés! le jeu est fini."
        #retourné VRAI 
    #Sinon
        #retourné Faux

    #################################################    corps du programme    #################################################

    #construction d'une grille vide
    #pour chaque i ranger en 3 
        #inisialiser ligne au tabeau
        #pour chaque j ranger en 3 
            #ajouté append a ligne qui retourne rien
        #ajouté append a grille qui retourne ligne
    # assigner le joueurs a chaque symbole


    #assigner tour a la valeur 0
    # fin est egale Faux
    #Tant que c'est pas egale a fin 
        #alors correct est egale a FAUX
        #Tant que c'est pas egale a correct :
            # assigner a la variable rep le retour de l'éxécution de la fonction input avec le message "Quelle case souhaitez-vous cocher ?\n"
                # assigner la valeur correct a la fonctionecriture_possible qui retourne grille et rep  
        # assigner dessin aux parametre joueur qui retourne "tour"
        # assigner grille a la fonction ecriture qui retourne "grille, rep et dessin"
        #pour chaque i ranger en 3 
            #afficher le message du parametre grille i
        # assigner a la variable fin a la fonction alignement qui retourne "grille"
        #ajouté +1 a tour
        #ajouté +1 a comptetour 
        #Si compteTour est egale a 9 
            #alors affiché message : egalité 
            #appeler la fonction exit
            
#Definir la fonction JcIA
    #assiger J a la valeur -1
    #assiger IA a la valeur +1
    #affiché un tableau nommé board ,

    #definir la focton evaluate qui retourne comme parametre state
        #Si la fonction wins prend les parametre state et la valeur IA 
            #alors assiger la variable score a la valeur +1 
        #Sinon Si la fonction wins prend les parametre state et J
            #alors assiger la variable score a la valeur -1
        #Sinon 
            #alors la variable score est egale a 0 
        #retouré la variable score 

    #definir la fonction wins qui retourne comme parametre state et player 
        # affiché une liste nommé win_state
        #
            #alors retourne 
        #sinon
            #alors retourné faux 

    #definir la fonction game_over qui prent comme parametre state
        #retourné la fonction wins qui prent comme parametre state et J ou la fonction wins qui prent comme parametre state et IA

    #definir la fonction empty_cells qui prent comme parametre state
        
        #pour chaque x et row dans la fonction enumerate qui prend comme parametre state
            #pour chaque y et cell dans la fonction enumerate qui prend comme parametre row 
                #Si cell est égale a 0 
                    #alors appeler cells append([x, y]))

        #retourné cells 

    #definir la fonction valid_move qui a pour parametre x et y 
        #Si la liste x et y est dans la foction empty_cells qui a comme parametre board 
            #alors retourné vrai 
        #sinon
            #alors retourné faux 

    #definir la fonction set_move qui prend comme parametre x, y et player
        #Si la fonction valid_move a pour parametre x et y 
            #alors on assigne le tableau board x y a la variable player
            #retourné vrai 
        #sinon 
            #retourné fau

    #definir la fonction minimax qui prend comme parametre state, depth et player
        #Si player est egale a l'IA 
            #alors assiger la liste best [-1, -1, -infinity]
        #Sinon
            #alors assiger la liste best [-1, -1, +infinity]
        #Si depth est égale a la valeur 0 ou a la fonction game_over qui retourne comme parametre state 
            #alors score est égales evaluate(state) 
            #retourné la liste [-1, -1, score]
        #pour chaque celle dans la fonction 
            #x et y est égale a cell[0], cell[1]
            # assigner player aux paramètre state [x][y]
            #assigne score a la foction minimax qui prens comme parametre state, depth - 1 et -player
            # assigne state[x][y] a la valeur 0
            #score[0] et scrore[1] est egale a x, y

            #si player est egale a IA : 
                #si scrore[2] est suprérieur a best[2]
                    #alors best est égale a score   # max value
            #sinon 
                #Si score[2] est supérieur a best[2]
                    #alors best est égale a score  # min value
        #retourné best 

    #definir la fonction clean()
        #os_name est egale a platform.system().lower()
        #Si windows est dans la variable os_name
            #alors apeler la fonction system qui retourne le message 'cls'
            #sinon
            #alors apeler la fonction system qui retourne le message 'clear'
            
    #definir la fonction render (state, c_choice)
        #chars est egale a une liste h_choice, c_choice et ''.

        #affiché un message ('\n' + str_line)
        #pour chaque row dans state 
            #pour chaque cell danns row 
                #assiger symbole a chars[cell
    #definir la fonction ia_turn qui prend comme parametre c_choice, h_choice
        #assigner depth a la fonction len qui prend comme parametre empty_cells(board)
        #si  depth est egale a 0 or a game_over avec les parametre board
            #retourné la fonction 

        #appeler la fonction clean()
        #affiché message f'IA Joue [{c_choice}]'
        #appeler la fonction render avec les parametres board, c_choice et h_choice

        #si depth est egale a la valeur 9 
            #alors x est egale a la fonction choice avec les valeurs [0, 1, 2]
            #alors y est egale a la fonction choice avec les valeurs [0, 1, 2]
        #sinon
            #assiger move a minimax avec les parametre board, depth et l'IA
            #assiger x, y a move [0] et move[1]
        #appeler la fonction set_move avec les parametres x, y et IA
        #ajouté 1 a time.sleep

    #definir la fonction human_turn qui prend comme parametre c_choice et  h_choice
        #assiger depth a la fonction len qui retoune comme parmetre la fonction empty_cells(board)
        #si depth est égale a 0 ou a la fonction game_over qui retourne les parametre board
            #alros retourne la fonction 

        # ajouté un Dictionaire des moves possibl
        #appeler la fonction clean()
        #affiché message "A vous de jouer [{c_choice}]"
        #appeler la fonction render avec les parametres board, c_choice et h_choice

        #tant que mouve est inferieur a 1 ou supérieur a 9 
            #alors 
                #assiger mouve a int qui a comme parametre la fonction input et un message 'numéro ? (1..9): '
                #assiger coord a mouves[move]
                #assigner can_mouve a la fonction set_move avec les parametre (coord[0], coord[1] et J)

                #Si c'est pas égale a la variavle can_move 
                    #alors affiche un message 'mauvaise saisis'
                    #assigne move a la valeur -1 
            #appeler la fonction except qui prent comme parametre EOFError et KeyboardInterrupt
                #affiche message 'adieu'
                #fermé la fonction 
            #appeler la fonction except qui prent comme parametre KeyError et ValueError
                #affiche message 'Mauvais choix'

    #definir la fonction main
        #appeler la fonction clean()  # X or O  # X or O # if human is the first

        #tant que h_choice est non egale aux message 'O' et non egale aux message 'X'
            #alors
                #affiche aucun message 
                #assigne h_choice aux retoure de l'execution de la fonction input 'Choisit X ou O\nChoix : ' avec la fonction upper()
            # appeler la fonction except qui prent comme parametre EOFError et KeyboardInterrupt
                #affiche message 'adieu'
                #fermé la fonction 
            #appeler la fonction except qui prent comme parametre KeyError et ValueError
                #affiche message 'Mauvais choix'
                
        #Si h_choice est égale a X,
            #alors c_choice est égale a O
            #sinon
            #c_choice est egale a X

        #appeler la fonction clean()
        #tant que la variable first est non egale a'Y' et est non egale a N
            #alors 
                #assigner la variable first aux retour de l'execution dela fonction input qui retoure le message 'Tu veux commencer ?[y/n]: ' avec la fonction upper()
            # appeler la fonction except qui prent comme parametre EOFError et KeyboardInterrupt
                #affiche message 'adieu'
                #fermé la fonction 
            #appeler la fonction except qui prent comme parametre KeyError et ValueError
                #affiche message 'Mauvais choix'

        #tant que len avec ses parametre empty_cells(board) est supérieur a 0 et non a game_over(board)
            #si first est égale a N
                #alors appeller la foncion ia_turn avecles parametres c_choice, h_choice
                #assigner first a rien 

            #appeller la foncion human_turn avec les parametres c_choice et h_choice
            #appeller la foncion ia_turn avec les parametres c_choice et h_choice

        # Game over message
        #Si la fonction wins a pour parametres board et J
            #Alors #appeler la fonction clean()
            #affiché le message 'A toi de jouer[{h_choice}]'
            #appeler la foncton render qui a comme parametres board, c_choice et  h_choice
            #affiché le message 'TU AS GAGNER!'
        #sinon si la fonction wins a pour parametres board et IA
            #alors #appeler la fonction clean()
            #affiché le message 'IA joue [{c_choice}]'
            #appeler la foncton render qui a comme parametres board, c_choice et  h_choice
            #affiché le message 'TU AS PERDU !'
        #sinon
            #alors #appeler la fonction clean()
            #appeler la foncton render qui a comme parametres board, c_choice et  h_choice
            #affiché le message 'egalité !'
        #fermé la fonction




#################################################    Regle du morpion    ################################################# 

#definir la fonction regle_morpion
    #affiché message "Bienvenue sur ce Morpion de qualité !\n"
    #affiché un espace 
    # affiché message "Je suis Morpious votre serviteur et guide sur ce morpion. Pour commencer, ce morpion fut créé par Kyllian et William. Mes 2 géniaux créateur.
    # Ce Morpion vous propose une version joueur contre joueur et une version contre moi ! (attention je suis imbattable à ce jeu).\n"
    #affiché un espace 
    #affiché message "Les règles sont simple : \n"
    #affiché message "Le tableau est diviser un 9 cases. Ces 9 cases sont présentes sur des lignes et des colonnes nominées de 0 à 2.
    #Pour afficher l’un de vos symboles ( X ou O) vous devrais mettre votre réponses sous cette forme: ligne – colonne (sans le tiré). \n"
    #affiché message "Par exemple si vous souhaité mettre votre symbole au milieux vous devrait taper : 11 (1 = ligne, 1 = colonne)\n"
    #affiché message "Si vous souhaité mettre votre symbole en haut a droite vous devrait taper : 02 (0 = ligne, 2 = colonne)\n"
    #affiché message "/!\  Aucune triche n’est autorisé de ta part  /!\ \n"
    #affiché message "Le premier à aligner 3 symboles gagne la partie ! \n"
    #affiché un espace
    #affiché message " Tu es prés ?\n"
    #assiger mode au retoure de la fonction input qui affiche le message " Appuis envoie donc 1 pour jouer en Joueur contre Joueur ou 2 pour jouer contre Moi (IA)\n"
    #Si mode est égale a 1 
        #Alors affiché message "Félicitation vous avez choisi de jouer entre vous j'espere qu'apres cette partie votre amitié sera toujours intacte <3 "
        #ajouté 2 a time.sleep
        #appeler la fonction JcJ()
    #sinon si mode est egale a 2
        #alors affiché message "Félicitation vous avez choisi de jouer contre moi je vais te briser ! "
        #ajouté 2 a time.sleep
        #appeler la fonction JcIA()
#appeler la fonction regles_morpon()
