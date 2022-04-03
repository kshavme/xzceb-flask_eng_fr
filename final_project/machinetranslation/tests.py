import unittest

from translator import english_to_french, french_to_english

class TestEnglishToFrench(unittest.TestCase): 
    def test1(self):
        """Unit Test for English to French Translation"""
        self.assertEqual(english_to_french('Hello'), 'Bonjour') # test when Hello is given as input the output is Bonjour.
        self.assertEqual(english_to_french('Welcome'), 'Bienvenue')  # test when Welcome is given as input the output is Bienvenue.
        self.assertNotEqual(english_to_french(0),0)  #test for null input for english to french translation.

class TestFrenchToEnglish(unittest.TestCase): 
    def test1(self): 
        """Unit Test for French to English Translation"""
        self.assertEqual(french_to_english('Bonjour'), 'Hello') # test when Bonjour is given as input the output is Hello.
        self.assertEqual(french_to_english('Bienvenue'), 'Welcome')  # test when Bienvenue is given as input the output is Welcome.
        self.assertNotEqual(french_to_english(0),0) #test for null input for french to english translation.

unittest.main()
