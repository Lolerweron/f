import random
import sys
Teamrusków = ["Feron","Driver","Sandał","Berdzio","Jubi","Bartek","Loler","Raku","Semered","Jaca"]

def matchmaker(lista):
    random.shuffle(lista)
    dlugosclisty = len(lista)
    pol = dlugosclisty // 2
    Proplayers = lista[ : pol ]
    Nubz = lista[ pol : ]
    return Proplayers, Nubz
print(matchmaker(sys.argv[1:]))