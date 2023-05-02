import unittest
import calc

class TestCalc(unittest.TestCase):

    def test_add(self):
        self.assertEqual(calc.add(10, 5), 15)
        self.assertEqual(calc.add(10, 5), 15)
        self.assertEqual(calc.add(-1, 5), 4)
        self.assertEqual(calc.add(-10, 5), -5)

    def test_subtract(self):
        self.assertEqual(calc.subtract(10, 5), 5)
        self.assertEqual(calc.subtract(10, 5), 5)
        self.assertEqual(calc.subtract(10, 0), 10)
        self.assertEqual(calc.subtract(-8, -2), -6)

    def test_multiply(self):
        self.assertEqual(calc.multiply(1, 1), 1)
        self.assertEqual(calc.multiply(10, 9), 90)
        self.assertEqual(calc.multiply(7, 2), 14)
        self.assertEqual(calc.multiply(2, 5), 10)

    def test_devide(self):
        self.assertEqual(calc.devide(8, 4), 2)
        self.assertRaises(ValueError, calc.devide, 10, 0)   #Cach 1
        with self.assertRaises(ValueError):                 #Cach 2
            calc.devide(10,0)
        self.assertEqual(calc.devide(100, 20), 5)
        self.assertEqual(calc.devide(24, 8), 3)


if __name__ == '__main__':
    unittest.main()



