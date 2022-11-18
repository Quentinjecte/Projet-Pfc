import random

grille = []
grille.append([7, 8, 9])
grille.append([4, 5, 6])
grille.append([1, 2, 3])

visual = []
visual.append([" ", " ", " "])
visual.append([" ", " ", " "])
visual.append([" ", " ", " "])

def case(choix):
    if choix =='1':
        x = 0
        y = 0
        return x,y
    elif choix =='2':
        x = 0
        y = 1
        return x,y
    elif choix =='3':
        x = 0
        y = 2
        return x,y
    elif choix =='4':
        x = 1
        y = 0
        return x,y
    elif choix =='5':
        x = 1
        y = 1
        return x,y
    elif choix =='6':
        x = 1
        y = 2
        return x,y
    elif choix =='7':
        x = 2
        y = 0
        return x,y
    elif choix =='8':
        x = 2
        y = 1
        return x,y
    elif choix =='9':
        x = 2
        y = 2
        return x,y

def affichergrille():

    for i in range(0, len(grille)):
        print(" | ".join(str(e) for e in grille[i]))


def affichervisual():

    for i in range(0, len(visual)):
        print(" | ".join(str(e) for e in visual[i]))


# def caseSymbol(grille, symbol):
#     visual[grille] == symbol
#     listCaseEmpty.remove((grille))

# def ifCaseEmpty(grille):
#     if(visual[grille])==" ":
#         return True
#     return False

def breaker():
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")

def breakertwo():
    print(" ")

breaker()
print("Bienvenue dans le jeu du morpion !\n"
      "Règles du jeu :\n"
      "Pour gagner, il faut que vous aligner trois de vos symboles :\n"
      "  - Sur une même ligne\n"
      "  - Sur une même colonne\n"
      "  - Sur une même diagonale\n\n"
      "  - Voici la reference du tableau")
affichergrille()
breaker()


replay = 'O'
player1 = {"prenom" : "", "symbole" : "X"}
player2 = {"prenom" : "", "symbole" : "O"}

while replay == 'O':
    player1['prenom'] = input("Entrez le prénom du joueur 1 : ")
    player2['prenom'] = input("Entrez le prénom du joueur 2 : ")

    breaker()

    print(player1['prenom'],"tu joueras les X")
    print(player2['prenom'],"tu joueras les O")
    print("Un tirage au sort va désigner le premier joueur...")
    turnPlayer = random.choice([player1, player2])

    breaker()

    while True:
        print("Reference du tableau\n")
        affichergrille()
        breakertwo()
        print(turnPlayer["prenom"]," à ton tour !")
        breakertwo()
        affichervisual()
        while True :
            while True :
                line = int(input("Quelle case souhaites-tu jouer ? "))







































# def winCondition(symbol):
#     for i in grille:
#         if i ==[symbol for _ in range(0, len(visual))]:
#             return True
    
#     for i in range(0, len(visual)):
#         list = []
#         for k in grille:
#              list.append(k[i])
#         if list == [symbol for _ in range(0, len(visual))]:
#             return True

#     if visual(grille[1]) == visual(grille[5]) == visual(grille[9]) == symbol\
#         or visual(grille[3])== visual(grille[5])== visual(grille[7]) == symbol:
#         return True
#     return False



# breaker()
