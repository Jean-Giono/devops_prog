import unittest
#import main
from pendu import get_letter_correspondance

class TestPendu(unittest.TestCase):
    def test_letter_correspondance(self):
        let1 = 'A'
        corresp1= "AÀÄÂÆ"
        let2 = 'E'
        corresp2 = "EÊÈÉËÆŒ"
        let3 = 'I'
        corresp3 = "IÎÏ"
        
        self.assertEqual(get_letter_correspondance(let1), corresp1)
        self.assertEqual(get_letter_correspondance(let2), corresp2)
        self.assertEqual(get_letter_correspondance(let3), corresp3)


if __name__ == '__main__':
    unittest.main()