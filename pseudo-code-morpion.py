#importer la bibliothéque time

#dictionnaire associant une valeur à chaque symbole


#definir la fonction ecriture_possible qui retourne comme parametre grille et chaine

    # assigner pos a Faux
    
    # assigner lig a int qui contient le tableu chaine avec l'index 0
   
    # assigner col a int qui contient le tableu chaine avec l'index 1
 
    # Si le tableau grille contenant lig et col est egale a aucune valeur

        #Alors pos est egale a VRAI 

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

    #retourné aligne 


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

#definir JcJ


    #construction d'une grille vide

    #pour chaque i ranger en 3 

        #inisialiser ligne au tabeau

        #pour chaque j ranger en 3 

            #ajouté append a ligne qui retourne rien

        #ajouté append a grille qui retourne ligne
  
    # assigner le joueurs a chaque symbole



    #assigner tour a la valeur 0


    # fin est egale Faux


        #alors correct est egale a FAUX

        #Tant que c'est pas egale a correct :

            # assigner a la variable rep le retour de l'éxécution de la fonction input avec le message "Quelle case souhaitez-vous cocher ?\n"
     
            #si rep n'est pas une valeur recevable : ["00","01","02","10","11","12","20","21","22"]
        
                #alors ecrire "veuillez ressaisir la demande"

            #sinon si rep n'est toujours pas une valeur recevable : ["00","01","02","10","11","12","20","21","22"]
      
                # assigner la valeur correct a la fonctionecriture_possible qui retourne grille et rep
              
        # assigner dessin aux parametre joueur qui retourne "tour"
 
        # assigner grille a la fonction ecriture qui retourne "grille, rep et dessin"

        #pour chaque i ranger en 3 

            #afficher le message du parametre grille i

        # assigner a la variable fin a la fonction alignement qui retourne "grille"

        #ajouté +1 a tour
        
        #si comptour == 9
            #alors ecrire "egalité"

#definir JcIA (en cours)




#################################################    Regle du morpion    ################################################# 

#definir la fonction regle_morpion

    #ecrire "Bienvenue sur ce Morpion de qualité !"

     #sauter une ligne

     #ecrire "Je suis Morpious votre serviteur et guide sur ce morpion. Pour commencer, ce morpion fut créé par Kyllian et William. Mes 2 géniaux créateur. Ce Morpion vous propose une version joueur contre joueur et une version contre moi ! (attention je suis imbattable à ce jeu).
    
     #sauter une ligne

     #ecrire "Les règles sont simple :"
 
     #ecrire "Le tableau est diviser un 9 cases. Ces 9 cases sont présentes sur des lignes et des colonnes nominées de 0 à 2. Pour 	afficher l’un de vos symboles ( X ou O) vous devrais mettre votre réponses sous cette forme: ligne – colonne (sans le tiré).
    
     #ecrire "Par exemple si vous souhaité mettre votre symbole au milieux vous devrait taper : 11 (1 = ligne, 1 = colonne)"
    
     #ecrire "Si vous souhaité mettre votre symbole en haut a droite vous devrait taper : 02 (0 = ligne, 2 = colonne)"

     #ecrire "/!\  Aucune triche n’est autorisé de ta part  /!\"

     #ecrire "Le premier à aligner 3 symboles gagne la partie !"

     #sauter une ligne

     #ecrire

    #mode = input avec dans inpute le texte " Appuis envoie donc 1 pour jouer en Joueur contre Joueur ou 2 pour jouer contre Moi (IA)"

    #Si mode == 1

        #alors ecrire "Félicitation vous avez choisi de jouer entre vous j'espere qu'apres cette partie votre amitié sera toujours intacte <3 "
        
        #attendre 2 secondes

        #rediriger vers JcJ

    #Sinon si mode == 2 

        #alors ecrire "Félicitation vous avez choisi de jouer contre moi je vais te briser ! "
     
       #attendre 2 secondes

       #rediriger vers JcIA

#Appeller les regle du morpion 

