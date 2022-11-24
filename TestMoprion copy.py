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
wincpu = False


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
    if (visual[0][2] == visual[xChoix][yChoix] and visual[2][0] == visual[xChoix][yChoix] and visual[1][1] == visual[xChoix][yChoix]):
        return visual[xChoix][yChoix]
    elif (visual[0][0] == visual[xChoix][yChoix] and visual[2][2] == visual[xChoix][yChoix] and visual[1][1] == visual[xChoix][yChoix]):
            return visual[xChoix][yChoix]



def cpuBlock(visual):
    if (visual[1][1]=='X' and visual[2][2]=='X' or visual[1][0]=='X' and visual[2][0]=='X' or visual[0][1]=='X' and visual[0][2]=='X' ) and visual[0][0]== " ":

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
cpu = {"prenom" : "", "symbole" : "O"}

while winplayer1 ==False and wincpu == False and (restart == 'O'or'o'):
    player1['prenom'] = input("Entrez le prénom du joueur 1 : ")


    count = 0

    breaker()

    print(player1['prenom'],"tu joueras les X")
    print(cpu['prenom'],"tu joueras les O")
    print("Un tirage au sort va désigner le premier joueur...")
    turnPlayer = random.choice([player1, cpu])

    breaker()

    while winplayer1 ==False and wincpu == False:
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
                if (count == 1 and visual[1][1] == 'X'): #si le cpu commence ou joue en deuxieme et le joueur vient de jouer au milieu
                    count +=1
                    print("au tour de l'IA - Tour numero " + str(count) + "\n")
                    #assigner a choixCpu, un nombre entre 1 et 9
                    choixCpu = str(random.randint(1,9))
                    x,y = case(choixCpu)
                    #jouer sur un des 4 coins
                    while (case(choixCpu) != (0, 0)) and (case(choixCpu) != (0, 2)) and (case(choixCpu) != (2, 0)) and (case(choixCpu) != (2, 2)) and visual[x][y]!=" ":
                        choixCpu = str(random.randint(1,9))
                        x,y = case(choixCpu)
                    visual[x][y] = 'O'
                    print("Le CPU a joué sur la case " + choixCpu + "\n" )
                    affichervisual()
                    cpuFirst = False
                    

                else: #sinon
                    count +=1
                    print("au tour de l'IA - Tour numero " + str(count) + "\n")
                    if cpuWin(visual) != "NO": #si le CPU a 2 ronds alignés
                        choixCpu = cpuWin(visual)
                        x,y = case(choixCpu)
                        visual[x][y] = 'O'
                        print("Le CPU a joué sur la case " + choixCpu + "\n" )
                        affichervisual()
                    elif cpuBlock(visual) != "NO": #si le joueur a 2 croix alignés
                        choixCpu = cpuBlock(visual)
                        x,y = case(choixCpu)
                        visual[x][y] = 'O'
                        print("Le CPU a joué sur la case " + choixCpu + "\n" )
                        affichervisual()
                    else: #sinon
                        if visual[1][1] != 'X':    #si X ne joue pas au milieu
                            if count == 2 or count == 5: #si X ne joue pas au milieu au deuxieme et cinquieme tour
                                visual[1][1] = 'O'
                                print("Le CPU a joué sur la case 5\n" )
                                affichervisual()
                            elif count == 3: #si X ne joue pas au milieu au troisieme tour
                                choixCpu = str(random.randint(1,9))
                                x,y = case(choixCpu)
                                while visual[x][y] != 'O' :
                                    choixCpu = str(random.randint(1,9))
                                    x,y = case(choixCpu)
                                if x == 0 and y == 0:
                                    if visual[0][1] == 'X':
                                        choixCpu = str(random.choice([7,9]))
                                        x,y = case(choixCpu)   
                                    elif visual[1][0] == 'X':
                                        choixCpu = str(random.choice([1,9]))
                                        x,y = case(choixCpu)
                                    else:
                                        choixCpu = str(random.randint(1,9))
                                        x,y = case(choixCpu)
                                        while (case(choixCpu) == (0, 0)) and (case(choixCpu) == (0, 2)) and (case(choixCpu) == (2, 0)) and (case(choixCpu) == (2, 2) and visual[x][y] != ' '):
                                            choixCpu = str(random.randint(1,9))
                                            x,y = case(choixCpu)
                                elif x == 2 and y == 0:
                                    if visual[2][1] == 'X':
                                        choixCpu = str(random.choice([1,3]))
                                        x,y = case(choixCpu)
                                    elif visual[1][0] == 'X':
                                        choixCpu = str(random.choice([3,9]))
                                        x,y = case(choixCpu)
                                    else:
                                        choixCpu = str(random.randint(1,9))
                                        x,y = case(choixCpu)
                                        while (case(choixCpu) == (0, 0)) and (case(choixCpu) == (0, 2)) and (case(choixCpu) == (2, 0)) and (case(choixCpu) == (2, 2) and visual[x][y] != ' '):
                                            choixCpu = str(random.randint(1,9))
                                            x,y = case(choixCpu)
                                elif x == 0 and y == 2:
                                    if visual[0][1] == 'X':
                                        choixCpu = str(random.choice([7,9]))
                                        x,y = case(choixCpu)
                                    elif visual[1][2] == 'X':
                                        choixCpu = str(random.choice([1,7]))
                                        x,y = case(choixCpu)
                                    else:
                                        choixCpu = str(random.randint(1,9))
                                        x,y = case(choixCpu)
                                        while (case(choixCpu) == (0, 0)) and (case(choixCpu) == (0, 2)) and (case(choixCpu) == (2, 0)) and (case(choixCpu) == (2, 2) or visual[x][y] != ' '):
                                            choixCpu = str(random.randint(1,9))
                                            x,y = case(choixCpu)
                                elif x == 2 and y == 2:
                                    if visual[2][1] == 'X':
                                        choixCpu = str(random.choice([1,3]))
                                        x,y = case(choixCpu)                            
                                    elif visual[1][2] == 'X':
                                        choixCpu = str(random.choice([1,7]))
                                        x,y = case(choixCpu)  
                                    else:
                                        choixCpu = str(random.randint(1,9))
                                        x,y = case(choixCpu)
                                        while (case(choixCpu) == (0, 0)) and (case(choixCpu) == (0, 2)) and (case(choixCpu) == (2, 0)) and (case(choixCpu) == (2, 2) or visual[x][y] != ' '):
                                            choixCpu = str(random.randint(1,9))
                                            x,y = case(choixCpu)
                                else:
                                    choixCpu = str(random.randint(1,9))
                                    x,y = case(choixCpu)
                                    while (case(choixCpu) != (0, 0)) and (case(choixCpu) != (0, 2)) and (case(choixCpu) != (2, 0)) and (case(choixCpu) != (2, 2)) or visual[x][y] != ' ':
                                            choixCpu = str(random.randint(1,9))
                                            x,y = case(choixCpu)
                                visual[x][y] = 'O'
                                print("Le CPU a joué sur la case " + choixCpu + "\n" )
                                affichervisual()       
                            else: #sinon = si 'x' ne joue pas au milieu au 2/3/5 eme tour
                                if visual[1][1] == 'X':
                                    choixCpu = str(random.randint(1,9))
                                    x,y = case(choixCpu)
                                    while (case(choixCpu) != (0, 0)) and (case(choixCpu) != (0, 2)) and (case(choixCpu) != (2, 0)) and (case(choixCpu) != (2, 2) ):
                                        choixCpu = str(random.randint(1,9))
                                        x,y = case(choixCpu)
                                    visual[x][y] = 'O'
                                else: 
                                    choixCpu = str(random.randint(1,9))
                                    x,y = case(choixCpu)
                                    while (visual[x][y] == 'X') and (visual[x][y] == 'O') or case == ValueError:
                                        choixCpu = str(random.randint(1,9))
                                        x,y = case(choixCpu)
                                    visual[x][y] = 'O'
                                print("Le CPU a joué sur la case " + choixCpu + "\n" )
                                affichervisual()
                        elif visual[1][1] == 'X': #si X joue au milieu 
                            if  count == 3: #si X joue au milieu au 3eme tour
                                x,y = case(str(10 - int(choixCpu))) #jouer sur le coin opposé
                                visual[x][y] = 'O'
                                print("Le CPU a joué sur la case " + (str(10 - int(choixCpu))) + "\n" )
                                affichervisual()
                            else:
                                choixCpu = str(random.randint(1,9))
                                x,y = case(choixCpu)
                                while (visual[x][y] == 'X') and (visual[x][y] == 'O') or case == ValueError:
                                    choixCpu = str(random.randint(1,9))
                                    x,y = case(choixCpu)
                                visual[x][y] = 'O'
                                print("Le CPU a joué sur la case " + choixCpu + "\n" )
                                affichervisual()
        
                while visual[x][y]!=" ":
                    print("\nCette case est deja prise")
                    choixCpu = str(random.randint(1,9))
                    x,y=case(choixCpu)   
            breakertwo()
            affichergrille()
            breakertwo()
            affichervisual()  
              
              
            if winCondition(visual, x ,y) == 'O':
                print("Bravo ! " +turnPlayer["prenom"]+ " Tu as gagné !")
                wincpu = True
                break
            if count == 9:
                print("égaliter")
                wincpu = True
                break


            if turnPlayer == player1:
                turnPlayer = cpu
            else:
                turnPlayer = player1

    restart = " "
    while restart not in ["O" or "o", "N" or "n"]:
        breaker()
        restart = input("Souhaitez-vous restart ? [O/N] ")
        wincpu = False
        winplayer1 = False
        player1 = {"prenom" : "", "symbole" : "X"}
        cpu = {"prenom" : "", "symbole" : "O"}
        visual = []
        visual.append([" ", " ", " "])
        visual.append([" ", " ", " "])
        visual.append([" ", " ", " "])

    if restart == ("N"or"n"):
        break

breaker()
print("Merci d'avoir joué !")