"""
Module de scoring permettant l'affichage et la gestion du score pour une partie de Jeu du Pendu
"""

class Score:
    """Calcule et stocke le score de la session en cours à chaque fin de partie"""
    __isVictoire=True
    __longueurMot=0
    __nombreErreurs=0
    __currentScore=0
    __nbVictoires=0
    __nbDefaites=0

    def __init__(self) -> None:
        """Constructeur de la classe (score = 0)"""
        self.__currentScore = 0

    
    def updateWord(self, longueur, erreurs, vict):
        """Remplace le mot contenu en mémoire par le mot actuel
        - longueur = Longueur du mot actuel
        - erreurs = Nombre de tentatives utilisées pour trouver le mot actuel
        - vict = Booléen indiquant s'il s'agit d'une victoire (true) ou d'une défaite (false)"""
        self.__longueurMot = longueur
        self.__nombreErreurs = erreurs
        self.__isVictoire = vict

    
    def defineDifficulte(self):
        """Génère la difficulté du mot actuel en fonction de sa longueur"""
        if(self.__longueurMot<=4):
            return 1
        if (self.__longueurMot<=6):
            return 2
        if(self.__longueurMot<=8):
            return 3
        return 4

    
    def updateScore(self):
        """Met à jour du score selon le nombre d'erreur, l'issue de la partie, et le nombre de tentatives"""
        if(not self.__isVictoire):
            self.__nbDefaites+=1
            return
        if((self.__longueurMot - self.__nombreErreurs) <=0):
            self.__currentScore+=5
        else:
            self.__currentScore+= (5 + self.defineDifficulte() * (self.__longueurMot - self.__nombreErreurs))
        self.__nbVictoires+=1

    
    def displayScore(self):
        """Affiche le score"""
        self.updateScore()
        print("Votre score actuel est: ", self.__currentScore)
        print(self.__nbVictoires, " Victoires et ", self.__nbDefaites, " Défaites")
