import unittest as unt
import change_text

class TestChangeText(unt.TestCase):

    def test_uppercase(self):
        word="Study"
        result= change_text.all_capitals(word)
        self.assertEqual(result,"STUDY")

if __name__ == '__main__':
    unt.main()
