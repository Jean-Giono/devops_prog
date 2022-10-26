"""Module permettant la génération d'un dictionnaire pour le Jeu du Pendu en utilisant un fichier texte"""
import random

class WordDict:
    """Dictionnaire de mots"""
    __wordList=""

    def __init__(self) -> None:
        """Constructeur de la classe (lecture du fichier texte)"""
        #my_file = open("dict.txt", "r")
        with open("dict.txt", "r", encoding='utf-8') as my_file:
            data = my_file.read()

        self.__wordList = data.split("\n")

    
    def getWordList(self):
        """Renvoie la liste des mots"""
        return self.__wordList

    
    def getOneWord(self):
        """Renvoie un mot au hasard dans la liste"""
        return self.__wordList[random.randint(0, self.__wordList.__len__()-1)]