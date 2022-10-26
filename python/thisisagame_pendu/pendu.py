"""Module principal qui permet de lancer l'application"""
from operator import le
from webbrowser import get
import dictGen
import cli
import sys
import scoring
from itertools import chain

# réduire la profondeur de la pile d'erreur à 0
# affiche simplement l'erreur et une suggestion pour la palier
sys.tracebacklimit = 0

score = scoring.Score()

def get_rng_ascii():
    """Module permettant la génération d'un dictionnaire pour le Jeu du Pendu en utilisant un fichier texte"""
    r1 = range(65,91)
    r2 = range(97,123)
    r3 = range(128,155)

    rng_ascii = list(chain(r1,r2,r3))

    return rng_ascii

def underscore(mot , L=[]):
    """Fonction  : prend en entrée un mot et une liste de lettres, puis retourne le mot contenant uniquement les lettres présentes dans la liste et en commun avec le mot.
    Le reste des lettres est remplacé par un underscore (tiret du 8)."""
    r = ''
    for i in mot:
        if i in L:
            r += i + ' '
        else:
            r += '_ '
            
    return r[:-1]

def saisir_lettre():
    """Fonction  : permet à l'utilisateur de saisir une lettre à l'écran"""
    rng_ascii = get_rng_ascii()
    lettre = input('Entrez une lettre : ')
    while len(lettre) < 1:
        lettre = input("Vous n'avez rien saisi!\nVeuillez saisir une lettre et une seule à la fois!")
    if len(lettre) > 1 or ord(lettre) not in rng_ascii:
        return saisir_lettre()
    else:
        return lettre.upper()

def get_letter_correspondance(aletter):
    """Fonction  : retourne les lettres accentuées dérivées d'une lettre sans accent fournie en entrée"""
    correspondances_lettres = {
    'A': 'AÀÄÂÆ',
    'C': 'CÇ',
    'E': 'EÊÈÉËÆŒ',
    'I': 'IÎÏ',
    'O': 'OÔÖŒ',
    'U': 'UÙÜÛ' }

    if aletter in correspondances_lettres:
        return str(correspondances_lettres[aletter])

def get_NbMots():
    """Fonction  : permet à l'utlisateur de saisir le nombre de mots qu'il souhaite trouver dans une partie de jeu"""
    nb_mots=""

    while len(nb_mots) < 1 or not nb_mots.isdigit():
        nb_mots = str(input('Veuillez saisir un nombre de mots que vous souhaitez trouver!\nExemple: 4, 5, 8, etc.\n'))

    nb_mots = int(nb_mots)
    if nb_mots > 10 or nb_mots < 1:
        print("Le nombre de mots doit être non nul et inférieur ou égal à 10.\n")
        get_NbMots()

    return nb_mots

if __name__ == '__main__':
    compteurParties = 0
    liste_mots = []
    nb_mots = get_NbMots()

    while(compteurParties<nb_mots):
        my_dict = dictGen.WordDict()
        my_cli = cli.cli()
        my_cli.beginGame()
        
        """Génération d'un nouveau mot de façon aléatoire à l'aide d'un dictionnaire. On s'assure également qu'un même mot ne soit proposé deux fois au joueur."""
        mot_secret = my_dict.getOneWord().upper()
        while mot_secret in liste_mots:
            mot_secret = my_dict.getOneWord().upper()
        liste_mots.append(mot_secret)

        nbVies = my_cli.maxError()

        lettres_proposees = []
        affichage = underscore(mot_secret)
        print('Mot secret : ' , affichage)
        nb_erreurs = 0

        while '_' in affichage and nb_erreurs < nbVies:
            lettre = saisir_lettre()
            if lettre not in lettres_proposees:
                lettres_proposees += [lettre]
                
                """Gestion de lettres accentuées. Toutes les lettres accentuées sont remplacées automatiquement dans le mot, dès lors que, l'utilisateur saisit une lettre
                non accentuée, dont dérive celles accentuées."""
                lt_cor = get_letter_correspondance(lettre)
                if lt_cor != None:
                    for lt in lt_cor:
                        if lt in mot_secret:
                            lettres_proposees += [lt]
            else:
                print("cette lettre a déjà été proposée!")
                    
            if lettre not in mot_secret:
                nb_erreurs += 1
                my_cli.printdraw(nb_erreurs)

            affichage = underscore(mot_secret , lettres_proposees)
            print('\nMot à deviner : ' , affichage , ' '*(nbVies-1) , 'Nombre d\'erreurs restantes :' , nbVies-nb_erreurs)

        if '_' in affichage:
            print("Vous n'avez pas trouvé le mot %s.\n" % mot_secret)
            score.updateWord(mot_secret.__len__(), nb_erreurs, False)
        else:
            print("Bravo! vous avez trouvé le mot : %s.\n" % mot_secret)
            score.updateWord(mot_secret.__len__(), nb_erreurs, True)
        
        score.displayScore()
        compteurParties+=1
