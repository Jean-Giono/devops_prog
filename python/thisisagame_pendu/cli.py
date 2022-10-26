"""Module d'affichage du Jeu du Pendu"""
class cli:
    """Ensemble de messages associés à une partie"""
    __beginMessage="-------------------------------------\n  _____  ______ _   _ _____  _    _ \n |  __ \|  ____| \ | |  __ \| |  | |\n | |__) | |__  |  \| | |  | | |  | |\n |  ___/|  __| | . ` | |  | | |  | |\n | |    | |____| |\  | |__| | |__| |\n |_|    |______|_| \_|_____/ \____/ \n--------------------------------------"
    __drawList = ""

    def __init__(self) -> None:
        """Constructeur de la classe (lecture du fichier texte contentant les dessins)"""
        my_file = open("drawing.txt", "r")

        data = my_file.read()

        self.__drawList = data.split("\n")

    
    def printdraw(self, nbErreurs):
        """Affiche le dessin correspondant au nombre d'erreurs nbErreurs"""
        print(str(self.__drawList[nbErreurs].replace('\\n', '\n')))

    
    def beginGame(self):
        """Affiche le message de lancement d'une partie"""
        print(self.__beginMessage)

    
    def maxError(self):
        """Retourne le nombre d'erreurs maximales (défini par le nombre d'étapes dans le dessin)"""
        return self.__drawList.__len__()-1


