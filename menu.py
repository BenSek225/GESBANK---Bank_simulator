import numpy as np
from operation import menu, retour, creer, solde, versement, retrait

OP = 0            #pour le choix principal
choix2 = 0       #pour choisir de quitter ou de continuer dans l'option retour


while OP != 5 or choix2 != 2:
    OP = menu()  #le programme princilal lance menu()
    
    match OP:
        case 1: creer()
            
        case 2: retrait()
        
        case 3: versement()

        case 4: solde()
        
        case 5:
            print("   ")
            print(" ~~~~~~ Merci d'avoir souscrit a GESBANK ~~~~~~ ")
            print("     ~~~~~~ Aurevoir et a bientôt ! ~~~~~~ ")
            break        
    retour()  
    choix2 = int(input("  Votre choix..."))
    match choix2:
        case 1: OP
        case 2:
            print("   ")
            print(" ~~~~~~ Merci d'avoir souscrit a GESBANK ~~~~~~ ")
            print("     ~~~~~~ Aurevoir et a bientôt ! ~~~~~~ ")
            break
