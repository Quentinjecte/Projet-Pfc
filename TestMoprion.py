import random

grille = []
grille.append([7, 8, 9])
grille.append([4, 5, 6])
grille.append([1, 2, 3])

visual = []
visual.append([" ", " ", " "])
visual.append([" ", " ", " "])
visual.append([" ", " ", " "])

winplayer1 = False
winplayer2 = False


def case(choix):
    if choix =='1':
        x = 2
        y = 0
        return x,y
    elif choix =='2':
        x = 2
        y = 1
        return x,y
    elif choix =='3':
        x = 2
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
        x = 0
        y = 0
        return x,y
    elif choix =='8':
        x = 0
        y = 1
        return x,y
    elif choix =='9':
        x = 0
        y = 2
        return x,y

def winCondition(visual, xChoix, yChoix):
    #test en ligne
    if yChoix == 0:
        if (visual[xChoix][yChoix + 1] == visual[xChoix][yChoix])and (visual[xChoix][yChoix + 2] == visual[xChoix][yChoix]) :
            return visual[xChoix][yChoix]
    elif yChoix == 1:
        if (visual[xChoix][yChoix - 1] == visual[xChoix][yChoix])and (visual[xChoix][yChoix + 1] == visual[xChoix][yChoix]) :
            return visual[xChoix][yChoix]
    elif yChoix == 2:
        if (visual[xChoix][yChoix - 2] == visual[xChoix][yChoix])and (visual[xChoix][yChoix - 1] == visual[xChoix][yChoix]) :
            return visual[xChoix][yChoix]
    #test en colonne 
    if xChoix == 0:
        if (visual[xChoix + 1][yChoix] == visual[xChoix][yChoix])and (visual[xChoix + 2][yChoix] == visual[xChoix][yChoix]) :
            return visual[xChoix][yChoix]
    elif xChoix == 1:
        if (visual[xChoix - 1][yChoix ] == visual[xChoix][yChoix])and (visual[xChoix  + 1][yChoix] == visual[xChoix][yChoix]) :
            return visual[xChoix][yChoix]
    elif xChoix == 2:
        if (visual[xChoix - 2][yChoix] == visual[xChoix][yChoix])and (visual[xChoix - 1][yChoix] == visual[xChoix][yChoix]) :
            return visual[xChoix][yChoix]
    #test en diagonale
    if xChoix == 1 and yChoix == 1:
        return None
    elif (visual[0][2] == visual[xChoix][yChoix] and visual[2][0] == visual[xChoix][yChoix] and visual[1][1] == visual[xChoix][yChoix]):
        return visual[xChoix][yChoix]
    elif (visual[0][0] == visual[xChoix][yChoix] and visual[2][2] == visual[xChoix][yChoix] and visual[1][1] == visual[xChoix][yChoix]):
            return visual[xChoix][yChoix]



def cpuBlock(visual):
    if (visual[1][1]=='X' and visual[2][2]=='X' or visual[1][0]=='X' and visual[2][0]=='X' or visual[0][1]=='X' and visual[0][2]=='X') and visual[0][0]== " ":

      return '7'

    elif (visual[0][0]=='X' and visual[0][2]=='X' or visual[1][1]=='X' and visual[2][1]=='X') and visual[0][1]== " ":

      return '8'

    elif (visual[0][0]=='X' and visual[0][1]=='X' or visual[1][1]=='X' and visual[2][0]=='X' or visual[1][2]=='X' and visual[2][2]=='X') and visual[0][2]== " ":

      return '9'

    elif (visual[0][0]=='X' and visual[2][0]=='X' or visual[1][1]=='X' and visual[1][2]=='X') and visual[1][0]== " ":

      return '4'

    elif (visual[0][0]=='X' and visual[2][2]=='X' or visual[1][0]=='X' and visual[1][2]=='X' or visual[0][1]=='X' and visual[2][1]=='X' or visual[2][0]=='X' and visual[0][2]=='X') and visual[1][1]== " ":

      return '5'

    elif (visual[1][0]=='X' and visual[1][2]=='X' or visual[0][2]=='X' and visual[2][2]=='X') and visual[1][2]== " ":

      return '6'

    elif (visual[0][0]=='X' and visual[1][0]=='X' or visual[1][1]=='X' and visual[0][2]=='X' or visual[2][1]=='X' and visual[2][2]=='X') and visual[2][0]== " ":

      return '1'

    elif (visual[2][1]=='X' and visual[2][2]=='X' or visual[1][1]=='X' and visual[0][1]=='X') and visual[2][1]== " ":

      return '2'

    elif (visual[0][0]=='X' and visual[1][1]=='X' or visual[2][0]=='X' and visual[2][1]=='X' or visual[0][2]=='X' and visual[1][2]=='X') and visual[2][2]== " ":

      return '3'

    else:
        return "NO"

def cpuWin(visual):
    if (visual[1][1]=='O' and visual[2][2]=='O' or visual[1][0]=='O' and visual[2][0]=='O' or visual[0][1]=='O' and visual[0][2]=='O') and visual[0][0]== " ":

      return '7'

    elif (visual[0][0]=='O' and visual[0][2]=='O' or visual[1][1]=='O' and visual[2][1]=='O') and visual[0][1]== " ":

      return '8'

    elif (visual[0][0]=='O' and visual[0][1]=='O' or visual[1][1]=='O' and visual[2][0]=='O' or visual[1][2]=='O' and visual[2][2]=='O') and visual[0][2]== " ":

      return '9'

    elif (visual[0][0]=='O' and visual[2][0]=='O' or visual[1][1]=='O' and visual[1][2]=='O') and visual[1][0]== " ":

      return '4'

    elif (visual[0][0]=='O' and visual[2][2]=='O' or visual[1][0]=='O' and visual[1][2]=='O' or visual[0][1]=='O' and visual[2][1]=='O' or visual[2][0]=='O' and visual[0][2]=='O') and visual[1][1]== " ":

      return '5'

    elif (visual[1][0]=='O' and visual[1][2]=='O' or visual[0][2]=='O' and visual[2][2]=='O') and visual[1][2]== " ":

      return '6'

    elif (visual[0][0]=='O' and visual[1][0]=='O' or visual[1][1]=='O' and visual[0][2]=='O' or visual[2][1]=='O' and visual[2][2]=='O') and visual[2][0]== " ":
 
      return '1'

    elif (visual[2][1]=='O' and visual[2][2]=='O' or visual[1][1]=='O' and visual[0][1]=='O') and visual[2][1]== " ":

      return '2'

    elif (visual[0][0]=='O' and visual[1][1]=='O' or visual[2][0]=='O' and visual[2][1]=='O' or visual[0][2]=='O' and visual[1][2]=='O') and visual[2][2]== " ":

      return '3'

    else:
        return "NO"



def affichergrille():

    for i in range(0, len(grille)):
        print(" | ".join(str(e) for e in grille[i]))


def affichervisual():

    for i in range(0, len(visual)):
        print(" | ".join(str(e) for e in visual[i]))


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
      "  - Voici la reference du visualleau")
affichergrille()
breaker()

restart = 'O'
player1 = {"prenom" : "", "symbole" : "X"}
player2 = {"prenom" : "", "symbole" : "O"}

while winplayer1 ==False and winplayer2 == False and (restart == 'O'or'o'):
    player1['prenom'] = input("Entrez le prénom du joueur 1 : ")
    player2['prenom'] = input("Entrez le prénom du joueur 2 : ")

    count = 0

    breaker()

    print(player1['prenom'],"tu joueras les X")
    print(player2['prenom'],"tu joueras les O")
    print("Un tirage au sort va désigner le premier joueur...")
    turnPlayer = random.choice([player1, player2])

    breaker()

    while winplayer1 ==False and winplayer2 == False:
        print("Reference du visualleau\n")
        affichergrille()
        breakertwo()
        print(turnPlayer['prenom']," à ton tour !")
        breakertwo()
        affichervisual()

        while True :
            
            if turnPlayer == player1:
                choix = str(input("\nQuelle case souhaites-tu jouer ? "))
                x,y=case(choix)

                while visual[x][y]!=" ":
                    print("\nCette case est deja prise")
                    choix = str(input("\nQuelle case souhaites-tu jouer ? "))
                    x,y=case(choix)
                visual[x][y]='X'
                count +=1
                breakertwo()
                affichergrille()
                breakertwo()
                affichervisual()

                if winCondition(visual, x ,y) == 'X':
                    print("Bravo! " +turnPlayer["prenom"]+ " Tu as gagné !")
                    winplayer1 = True
                    break
                if count == 9:
                    print("égaliter")
                    winplayer1 = True
                    break

            else:
              if cpuWin !="NO":
                choixCpu=cpuWin(visual)
                x,y=case(choixCpu)
                visual[x][y]='O'
                

              elif cpuBlock !="NO":
                choixCpu=cpuBlock(visual)
                x,y=case(choixCpu)
                visual[x][y]='O'
          

              if count == 0:
                choixCpu=str(random.randint(5))
                x,y=case(choixCpu)
                visual[x][y]='O'
                count +=1
       
                
              elif count == 1 and visual[1][1] =="X":
                choixCpu=str(random.randint(1,3,7,9))
                x,y=case(choixCpu)
                visual[x][y]='O'
                count +=1

              # elif :
              #   choixCpu=str(random.randint(5))
              #   x,y=case(choixCpu)
              #   visual[x][y]='O'


              while visual[x][y]!=" ":
                  print("\nCette case est deja prise")
                  choixCpu = str(random.randint(1,9))
                  x,y=case(choixCpu)   
              visual[x][y]='O'
              breakertwo()
              affichergrille()
              breakertwo()
              affichervisual()  

              if winCondition(visual, x ,y) == 'O':
                    print("Bravo ! " +turnPlayer["prenom"]+ " Tu as gagné !")
                    winplayer2 = True
                    break
              if count == 9:
                    print("égaliter")
                    winplayer2 = True
                    break



            if turnPlayer == player1:
                turnPlayer = player2
            else:
                turnPlayer = player1

    restart = " "
    while restart not in ["O" or "o", "N" or "n"]:
        breaker()
        restart = input("Souhaitez-vous restart ? [O/N] ")
        winplayer2 = False
        winplayer1 = False
        player1 = {"prenom" : "", "symbole" : "X"}
        player2 = {"prenom" : "", "symbole" : "O"}
        visual = []
        visual.append([" ", " ", " "])
        visual.append([" ", " ", " "])
        visual.append([" ", " ", " "])

    if restart == ("N"or"n"):
        break

breaker()
print("Merci d'avoir joué !")