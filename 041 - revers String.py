import unittest

def reverse_string(string):
    return string[::-1]

class TestReverseString(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(reverse_string(""), "")

    def test_single_character_string(self):
        self.assertEqual(reverse_string("a"), "a")

    def test_normal_string(self):
        self.assertEqual(reverse_string("hello"), "olleh")

    def test_string_with_special_characters(self):
        self.assertEqual(reverse_string("!@#"), "#@!")

    def test_string_with_numbers(self):
        self.assertEqual(reverse_string("12345"), "54321")

    def test_string_with_spaces(self):
        self.assertEqual(reverse_string("hello world"), "dlrow olleh")

if __name__ == '__main__':
    unittest.main()