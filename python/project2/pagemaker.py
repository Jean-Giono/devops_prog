#Jean-Giono
#11/08/2022
import os
import csv
import webbrowser

# cette fonction n'étant pas spécifique à la classe PageMaker, elle est en dehors de cette dernière
# ainsi, elle est réutilisable via un import en dehors de ce fichier
def readCSVFile(file_path: str) -> list:
    # file_path : lien du fichier (avec son extension)
    
    if not os.path.exists(file_path):
        print("Aucun fichier nommé %s n'existe dans notre base!\nVeuillez revoir cela, puis réessayez!\n" % file_path)
        exit()
    else:
        rows = []
        with open(file_path,'r') as fl:
            csvreader = csv.reader(fl)
            header = next(csvreader)
            for row in csvreader:
                rows.append(row)
    return rows


class PageMaker:
    def __init__(self,file_path):
        self.filep = file_path

    def generate_html(self, html_temp, file_location):
        '''
            but : remplace les tags par les éléments correspondants dans le template html
                    puis génère un fichier html dans un dossier spécifié
                    tout ce traitement est effectué pour chaque ligne du fichier csv
            entrée : html_temp : le chemin vers le template html
                    file_location : le chemin où sera enregistré le fichier html
                    ex:
                        html_temp : "template.html"
                        file_location : "/tmp/" ou "/htmls/"
            modification : création d'une page html à l'emplacement du chemin stipulé
            retour : cette fonction ne retourne aucun élément, elle fait juste des modifications
        '''

        list_of_elements = readCSVFile(self.filep)

        try:
            with open(html_temp, 'r') as fhtml:
                current_html_content = fhtml.read()
        except NameError:
            print("Nom de fichier invalide!\nIl s'agit du fichier : %s\nVeuillez revoir cela, puis réessayez!\n" % html_temp)

        if not os.path.isdir(file_location):
            print("Le chemin de dossier que, vous avez fourni est erroné!\nIl s'agit de: %s\n" % file_location)
            print("Veuillez revoir cela, puis réessayez!\n")
            exit()
        
        
        nb_movie = 0
        for elm in list_of_elements:
            fyear, fscore = elm[0].strip(), elm[1].strip()
            ftitle = elm[2].strip('" "').strip()

            next_html_content = current_html_content
            elm_to_replace = {"[Title]":ftitle, "[Year]":fyear, "[Score]":fscore}

            for k, val in elm_to_replace.items():
                next_html_content = next_html_content.replace(k, val)
                
            nb_movie += 1
            new_html_name = file_location+"movie"+str(nb_movie)+"_"+fyear+"_"+fscore+".html"
           
            with open(new_html_name, 'w') as nfhtml:
                nfhtml.write(next_html_content)
        
        print("[+] Tous vos fichiers hmtl ont bien été créés!\n")
    
    def display_html(self, page_url):
        '''
            affiche une page web dans votre navigateur
            page_url : le nom complet (avec l'extension) de votre fichier (.hmtl, etc.)
            ex :
                page_url='thisistheinternet.html"
                page_url='htmls/thisistheinternet.html'
        '''
        
        url_path_name = os.path.abspath(page_url)

        if not os.path.exists(url_path_name):
            print("Le chemin vers votre page web est introuvable!")
            print("\tCela veut dire que le Page Maker basé sur les données du fichier %s n'a pas créé un tel fichier" % self.filep)
            print("\tVeuillez revoir cela, puis réessayez!\n")
            exit()
        else:
            webbrowser.open('file://' + url_path_name)
            print("Bravo à toi quidam :)\nAu revoir!\n")
        


deniro_file = "deniro.csv"
pm = PageMaker(deniro_file)

html_temp = "template.html"
#html_files_location = "/tmp/"
html_files_location = "htmls/"
pm.generate_html(html_temp, html_files_location)

#url_to_display = "htmls/movie1_1968_86.html"
#url_to_display = "htmls/movie2_1970_17.html"
url_to_display = "htmls/movie79_2013_46.html"
pm.display_html(url_to_display)