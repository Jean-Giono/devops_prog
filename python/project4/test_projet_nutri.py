#Jean-Giono
#16/08/2022

import unittest
from food import Food

class TestFood(unittest.TestCase):
    """ class test food"""
    def test_get_name(self):
        """ test_get_name """
        print('test_get_name')
        food_one = Food()
        food_two = Food()

        food_two.set_name('coconut')

        self.assertEqual(food_one.get_name() , None)
        self.assertEqual(food_two.get_name() , 'coconut')

    def test_is_fat(self):
        """ test_is_fast """
        print('test_is_fat')
        food_one = Food()
        food_two = Food()
        food_three = Food()

        food_one.set_fat(8.3)
        food_two.set_fat(20.0)
        food_three.set_fat(23.1)

        self.assertEqual(food_one.is_fat() , False)
        self.assertEqual(food_two.is_fat(), False)
        self.assertEqual(food_three.is_fat(), True)


if __name__ == '__main__':
    unittest.main()
