#Jean-Giono
#16/08/2022

from food import Food
import argparse

parser = argparse.ArgumentParser("Food Informations")
parser.add_argument('-f', '--food', help="your food name", default='tomate')
args = parser.parse_args()
food_name = args.food

#myfood.setName(food_name)
#myfood.setCarbs(34)
#myfood.setProteins(23)
#myfood.setFat(3)
#myfood.setCalories(12)

myfood = Food()
myfood.retrieve_food_infos(food_name)
myfood.display_food_infos()
#myfood.save_to_csv_file('myfood.csv')
#print(myfood.is_fat())
