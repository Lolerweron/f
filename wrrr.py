import random


playerscore = 0
enemyscore = 0
while playerscore < 3 or enemyscore < 3 :
    lista = ["kamień","papier","nożyce"]
    gra = input("gramy w papier kamień nożyce co wybierasz? ")
    losuj = random.choice(lista)
    if gra == losuj :
        print("wybraliśmy to samo - remis")
    elif gra == "kamień" and losuj == "papier" :
        print("haha wybrałem papier - przegrałeś")
        enemyscore = enemyscore + 1
    elif gra == "papier" and losuj == "nożyce" :
        print("haha wybrałem nożyce - przegrałeś")
        enemyscore = enemyscore + 1
    elif gra == "nożyce" and losuj == "papier" :
        print("wybrałem papier - wygrałeś")
        playerscore = playerscore + 1
    elif gra == "kamień" and losuj == "nożyce" :
        print("wybrałem nożyce - wygrałeś")
        playerscore = playerscore + 1
    else :
        print("nope")


    if enemyscore == 3 :
        print("mam 3 punkty przegrałeś")
    if playerscore == 3 :
        print("masz 3 punkty wygrałeś")
