import unittest
from main import add, subtract, divide, multiply

class CalculatorTests(unittest.TestCase):
    def test_add(self): self.assertEqual(add(2, 4), 6)
    def test_subtract(self): self.assertEqual(subtract(9, 4), 5)
    def test_divide(self): self.assertEqual(divide(8, 2), 4)
    def test_zero(self):
        with self.assertRaises(ZeroDivisionError): divide(1, 0)
    def test_multiply(self): self.assertEqual(multiply(3, 4), 12)



class ModuloTests(unittest.TestCase):
    def test_remainder(self):
        from main import modulo
        self.assertEqual(modulo(11, 4), 3)
    def test_zero_divisor(self):
        from main import modulo
        with self.assertRaises(ZeroDivisionError): modulo(1, 0)

if __name__ == '__main__': unittest.main()
