import numpy as np
import json

def menu():
        print("        ")
        print(" -_-_-_- PROGRAMME_GESBANK -_-_-_-")
        print("                   ")
        print("       1- Creer un compte   ")
        print("       2- Retrait   ")
        print("       3- Versement  ")
        print("       4- Consultation  ")
        print("       5- Quitter  ")
        print("        ")
        choix = obtenir_entree_numerique("  Veuillez faire un choix:  ")
        return(choix)


def obtenir_entree_numerique(message):
    while True:
        try:
            entree = int(input(message))
            return entree
        except ValueError:
            print("Veuillez saisir un nombre valide.")
            

def retour():   #S'affiche a la fin de chaque fonction !
        print("        ")
        print("       1- Retour au menu")
        print("       2- Quitter")


def creer():
        print("        ")
        print(" -_-_-_- Creer_un_compte -_-_-_- ")
        print("               ")
        nom = input(" Entrez votre nom d'utilisateur:  ")
        MP = input(" Creer un mot de passe:  ")
        solde = 0+0+0
        utilisateur = {"Nom": nom, "MP": MP, "Solde": solde}
                     # Sauvegarde des informations dans un fichier JSON
        client = str ( int(np.random.random() * 1e8) ) #nombre aleatoire
        with open(client + ".txt", "w") as fichier:     # 'w' == creation + ecriture
                fichier.write( str (utilisateur) )
                print("                     ")
        print("       Votre numero de compte est:", client)
        print("                            Veuillez bien le noter !")
        print("  Soyez le bienvenue a GESBANK, ", nom)


def solde():
        print("        ")
        print(" -_-_-_- Consultation_de_solde -_-_-_- ")
        print("     ")
        compteS = input(" Entrez votre numero de compte:  ")
        nomS = input(" Entrez votre nom d'utilisateur:  ")
        MPS = input (" Entrez votre mot de passe:  ")

        try:
          with open(compteS + ".txt", "r") as fiche:  # 'r' == ouvre en lecture
            info = eval(fiche.read()) #eval() pour verifier les info du fichier

            if (nomS == info['Nom']) and (MPS == info['MP']):
                print("~~~~~~ Connection réussie ! ~~~~~~")
                print("       ")
                print("Bienvenue,", info['Nom'])
                print("       Votre solde actuel est de ~", info['Solde'], "~")
            else:
                print("~~~~~~ Nom d'utilisateur ou Mot de passe incorrect ! ~~~~~~")
                print("       ~~~~~~ Veuillez réessayer. ~~~~~~")
        except FileNotFoundError:
          print(" Le numéro de compte ~", compteS ,"~ n'existe pas. ")


def versement():
        print("       ")
        print(" -_-_-_- Versement -_-_-_- ")
        print("       ")
        compteV = input(" Entrez votre numero de compte:  ")
        nomV = input(" Entrez votre nom d'utilisateur:  ")
        MPV = input(" Entrez votre mot de passe:  ")

        try:
          with open(compteV + ".txt", "r+") as fiche:  # ouvre en mode lecture et ecriture "r+"
            info = eval(fiche.read())

            if (nomV == info['Nom']) and (MPV == info['MP']):
                print("~~~~~~ Connection réussie ! ~~~~~~")
                print("     Bienvenue a vous, ", info['Nom'])
                montant = int(input(" Entrez la somme du versement: "))

                if (montant <= 0):
                    print("       ")
                    print("~~~~~~ Transaction IMPOSSIBLE ! ~~~~~~")
                    print("          Veillez reessayer !       ")
                else:
                    solde = int(info['Solde']) + montant
                    info['Solde'] = solde

                    versement = {'Type': 'Versement', 'Montant': montant}
                    if 'Transactions' in info:
                        info['Transactions'].append(versement)
                    else:
                        info['Transactions'] = [versement]
                    fiche.write("\n" + str(versement))
                    
                    fiche.seek(0)  #pour commencer a ecrire au debut du fichier
                    fiche.write(str(info))
                    
                    print("       ")
                    print("~~~~~~ Versement_effectuer_avec_success_! ~~~~~~")
                    print("                     Votre nouveau solde est de, ", info['Solde'])
            else:
                print("       ")
                print("~~~~~~ Nom d'utilisateur ou Mot de passe incorrect ! ~~~~~~")
                print("                     ~~~~~~ Veuillez réessayer ! ~~~~~~")
        except FileNotFoundError: 
            print("       ")
            print(" Le numéro de compte ~", compteV, "~ n'existe pas.")



def retrait():
        print("       ")
        print(" -_-_-_- Retrait -_-_-_- ")
        print("       ")
        compteR = input(" Entrez votre numero de compte:  ")
        nomR = input(" Entrez votre nom d'utilisateur:  ")
        MPR = input(" Entrez votre mot de passe:  ")

        try:
            with open(compteR + ".txt", "r+") as fiche:
                info = eval(fiche.read())
                
                if (nomR == info['Nom']) and (MPR == info['MP']):
                    print("       ")
                    print("~~~~~~ Connection réussie ! ~~~~~~")
                    print("                Bienvenue a vous, ", info['Nom'])
                    retrait = int(input(" Entrez la somme de retrait: ")) 

                    if(retrait > int(info['Solde'])) or (retrait <= 0):
                        print("       ")
                        print("~~~~~~ Solde INSUFFISANT ou Transaction IMPOSSIBLE ! ~~~~~~ ")
                        print("                         ~~~~~~ Veillez reessayer ! ~~~~~~")
                    elif(retrait <= int(info['Solde'])):

                        solde = int(info['Solde']) - retrait
                        info['Solde'] = solde

                        retrait = {'Type': 'Retrait', 'Montant': retrait}
                        if 'Transactions' in info:
                                info['Transactions'].append(retrait)
                        else:
                            info['Transactions'] = [retrait]
                            fiche.write("\n" + str(retrait))
                    
                        fiche.seek(0) 
                        fiche.write(str(info))
                        print("       ")
                        print("~~~~~~ Retrait effectuer avec success ! ~~~~~~ ")
                        print("                 Votre nouveau solde est de, ", info['Solde'])
                else:
                    print("       ")
                    print("~~~~~~ Nom d'utilisateur ou Mot de passe incorrect ! ~~~~~~")
                    print("                            ~~~~~~ Veuillez réessayer ! ~~~~~~")
        except FileNotFoundError:
                print("       ")
                print(" Le numéro de compte ~", compteR, "~ n'existe pas.")



