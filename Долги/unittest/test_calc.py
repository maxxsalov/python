import unittest
from Calculator_class import Calculator


class MyTestCase(unittest.TestCase):
    def test_add(self):
        """проверка сложения, введены цифры"""
        test_res = Calculator(5, 7).addition()
        self.assertEqual(test_res, 12)

    def test_add_not_numbers(self):
        """проверка сложения, введены не цифры"""
        test_res = Calculator("QWE", "RTY").addition()
        self.assertEqual(test_res, "QWERTY")

    def test_add_empty_symbol(self):
        """проверка сложения, пустой символ"""
        test_res = Calculator("", "").addition()
        self.assertEqual(test_res, "")

    def test_sub(self):
        """проверка вычитания, введены цифры"""
        test_res = Calculator(12, 7).subtraction()
        self.assertEqual(test_res, 5)

    def test_sub_not_numbers(self):
        """проверка вычитания, введены не цифры"""
        with self.assertRaises(TypeError):
            Calculator("QWERTY", "RTY").subtraction()

    def test_sub_empty_symbol(self):
        """проверка вычитания, пустой символ"""
        with self.assertRaises(TypeError):
            Calculator("", "").subtraction()

    def test_multi(self):
        """проверка умножения, введены цифры"""
        test_res = Calculator(5, 7).multiplication()
        self.assertEqual(test_res, 35)

    def test_multi_not_numbers(self):
        """проверка умножения, введены не цифры"""
        with self.assertRaises(TypeError):
            Calculator("QWERTY", "RTY").multiplication()

    def test_multi_empty_symbol(self):
        """проверка умножения, пустой символ"""
        with self.assertRaises(TypeError):
            Calculator("", "").multiplication()

    def test_div(self):
        """проверка деления, введены цифры"""
        test_res = Calculator(35, 7).division()
        self.assertEqual(test_res, 5)

    def test_div_zero(self):
        test_res = Calculator(5, 0).division()
        self.assertEqual(test_res, None)

    def test_div_not_numbers(self):
        """проверка деления, введены не цифры"""
        with self.assertRaises(TypeError):
            Calculator("QWERTY", "RTY").division()

    def test_division3(self):
        """проверка деления, пустой символ"""
        with self.assertRaises(TypeError):
            Calculator("", "").division()


if __name__ == '__main__':
    unittest.main()
