# DEBUT
# définir une fonction règles avec comme pramètre rules
    # afficher "Bienvenue dans ce jeu Pierre, Feuille, Ciseau."
    # afficher "Voici les regles"
    # afficher "Vous allez devoir choisir entre pierre, papier ou ciseaux.(pas de ptn de puit)"
    # afficher "la pierre casse les ciseaux, la papier cache la pierre et les ciseaux coupe le papier" 

#initialiser resultatJoueur a 0 
#initialiser resultatOrdinateur a 0

#definir la fonction Tour:

    #si choix joueur est égale à 0
        #si choixOrdinateur egal a 0
            #alors resultat = "egalité"
        #si choixOrdinateur egal a 1 
            #alors resultat = "perdu"
        #si choixOrdinateur = 2
            #alors resultat ="gagnée"

    #si choix joueur est égale à 1
        #si choixOrdinateur egal a 0
            #alors resultat = "gagnée"
        #si choixOrdinateur egal a 1 
            #alors resultat = "egalité"
        #si choixOrdinateur = 2
            #alors resultat ="perdu"
            
    #si choix joueur est égale à 2
        #si choixOrdinateur egal a 0
            #alors resultat = "perdu"
        #si choixOrdinateur egal a 1 
            #alors resultat = "gagnée"
        #si choixOrdinateur = 2
            #alors resultat ="egalité"
    
    #retourner resultat
       
#tant que resultatJoueur et resultatOrdinateur sont inferieur a 3
    #Initialiser choixOrdinateur puis assigner le valeur retourner de random(0,2)
    #Initialiser choixJoueur puis assigner le valeur input( la valeur doit etre, 0,1 ou 2)
    #Initialiser resultatTour puis assigner la valeur retourner de Tour()

    #si choixJoueur egal a 0
        #alors afficher = "le joueur a fait pierre"
    #si choixJoueur egal a 1 
        #alors afficher = "le joueur a fait feuille"
    #si choixOrdinateur egal a 2
        #alors afficher ="le joueur a fait ciseau"

    #si choixOrdinateur egal a 0
        #alors afficher "l'ordinateur a fait pierre"
    #si choixOrdinateur egal a 1 
        #alors afficher "l'ordinateur a fait feuille"
    #si choixOrdinateur a 2
        #alors afficher "l'ordinateur a fait ciseau"

    #si resultat Tour est egal a gagnée 
        #alors incrementer resultatJoueur de 1
        #afficher "Tour gagnant"
    #sinon si resultat Tour est egal a perdu
        #alors incrementer resultatOrdinateur de 1
        #afficher "Tour perdant"
    #sinon si resultat Tour est egal a egalité
        #alors incrementer 0
        #afficher "Tour egalité"
    
    #afficher resultatJoueur et resultatOrdinateur
    
    #si resultatJoueur egal a 3
        #alors afficher "bravo, vous avez battu windows XP"

    #sinon si resultatOrdinateur egal a 3
        #alors afficher "...,bravo"
    
