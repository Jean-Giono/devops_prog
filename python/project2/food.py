#Jean-Giono
#16/08/2022

import csv
from bs4 import BeautifulSoup
import requests as req

URL = "https://www.infocalories.fr/"

class Food:
    """ class food """
    __name = None
    __calories = None
    __fat = None
    __carbs = None
    __proteins = None

    def get_name(self):
        """ function : get the food name """
        return self.__name

    def set_name(self,name):
        """ function : set the food name """
        self.__name = name

    def get_calories(self):
        """ function : get the property named calories of the food """
        return self.__calories

    def set_calories(self,calories):
        """ function : set the property named calories of the food """
        self.__calories = calories

    def get_fat(self):
        """ function : get the property named fat of the food """
        return self.__fat

    def set_fat(self,fat):
        """ function : set the property named fat of the food """
        self.__fat = fat

    def get_carbs(self):
        """ function : get the property named carbs of the food """
        return self.__carbs

    def set_carbs(self,carbs):
        """ function : set the property named carbs of the food """
        self.__carbs = carbs

    def get_proteins(self):
        """ function : get the property named proteins of the food """
        return self.__proteins
    def set_proteins(self,proteins):
        """ function : get the property named proteins of the food """
        self.__proteins = proteins

    def retrieve_food_infos(self,food_name):
        """ function : scrap the properties of the food from a website """
        #urlformat : https://www.infocalories.fr/calories/calories-sirop-erable.php
        food_url = URL+"calories/calories-"+food_name+".php"
        req_text = req.get(food_url).text

        if not req_text.startswith('File not found.'):
            bf_soup = BeautifulSoup(req_text, 'html.parser')
            all_infos = bf_soup.find("div", attrs={'id': 'diva'}).find_all("b")

            food_infos = []
            for food in all_infos:
                food_infos.append(''.join(c for c in food.text if (c.isdigit() or c ==',')))

            self.set_calories(float(food_infos[0]))
            self.set_proteins(float(food_infos[1].replace(',', '.')))
            self.set_carbs(float(food_infos[2].replace(',', '.')))
            self.set_fat(float(food_infos[3].replace(',', '.')))
            self.set_name(food_name)
        else:
            raise ValueError('Sorry, your food name does not exist! Check it out and try again!')

    def display_food_infos(self):
        """ function : display the properties of the food """
        print("------------------------------------------------")
        if "-" in self.get_name():
            print("name\t\tcalories\tfat\tcarbs\tproteins")
        else:
            print("name\tcalories\tfat\tcarbs\tproteins")
        print("%s\t%s\t\t%s\t%s\t%s" % (self.get_name(),self.get_calories(),self.get_fat(),self.get_carbs(),self.get_proteins()))
        print("------------------------------------------------")

    def save_to_csv_file(self, file_name):
        """ function : save the properties of the food in a csv file """
        with open(file_name, 'w', encoding="utf-8") as outfile:
            wrt_file = csv.writer(outfile)
            wrt_file.writerow(['name', 'calories', 'fat', 'carbs', 'proteins'])
            wrt_file.writerow([self.get_name(),self.get_calories(),self.get_fat(),self.get_carbs(),self.get_proteins()])

    def is_fat(self):
        """ function : return true or false whether the food has more than 20% of fat """
        return self.__fat > 20.0
