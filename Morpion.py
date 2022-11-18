import random

grille=[]
grille.append([1,2,3])
grille.append([4,5,6])
grille.append([7,8,9])

visual=[]
visual.append([" "," "," "])
visual.append([" "," "," "])
visual.append([" "," "," "])

def affichergrille():

    for i in range(0,len(grille)):
        print(" | ".join(str(e) for e in grille[i]))

affichergrille()

print("C'est au joueur X")


def afficher_visual():

    for i in range(0,len(visual)):
        print(" | ".join(str(e) for e in visual[i]))

afficher_visual()

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


while visual[x][y] =='X' or visual [x][y] =='O':
    print("La case est deja rempli")
    choix = str(input("entre une case"))
    x,y=case(choix)
    visual[x][y]='X'
    print("tu a joué sur la case" ,choix ,"\n")

    if isWin(visual, x, y) == 'X':
        winUser == True
        print("Bravo, tu as gagné\n")
        break

def player():
    return random.randint(0,1)

# def game(player):
#     if player == 1:
#         visual=["👌"]
#     elif player == 0:
#         visual=["🤞"]

# def winCondition(visual):
#     if (visual[0]==visual[1]) and (visual[0]==visual[2]) and (visual[0]!=" "):
#         return 1
#     elif (visual[3]==visual[4]) and (visual[3]==visual[5]) and (visual[3]!=" "):
#         return 1
#     elif (visual[6]==visual[7]) and (visual[6]==visual[8]) and (visual[6]!=" "):
#         return 1
#     elif (visual[0]==visual[3]) and (visual[0]==visual[6]) and (visual[0]!=" "):
#         return 1
#     elif (visual[1]==visual[4]) and (visual[1]==visual[7]) and (visual[1]!=" "):
#         return 1
#     elif (visual[2]==visual[5]) and (visual[2]==visual[8]) and (visual[2]!=" "):
#         return 1
#     elif (visual[0]==visual[4]) and (visual[0]==visual[8]) and (visual[0]!=" "):
#         return 1
#     elif (visual[2]==visual[4]) and (visual[2]==visual[6]) and (visual[2]!=" "):
#         return 1