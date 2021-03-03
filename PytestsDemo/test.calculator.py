import unittest
import calculator

class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(calculator.add(10,5),15)
        self.assertEqual(calculator.add(1, -1), 0)
        self.assertEqual(calculator.add(2, 5), 7)
       # result =calculator.add(10,5)
        #self.assertEqual(result,15)




    def test_sub(self):
        self.assertEqual(calculator.sub(10, 5), 5)
        self.assertEqual(calculator.sub(5, 5), 0)
        self.assertEqual(calculator.sub(15, 5), 10)
        #result = calculator.sub(10, 5)



    def test_div(self):
        self.assertEqual(calculator.div(10, 5), 2)
        self.assertEqual(calculator.div(15, 5), 3)
        self.assertEqual(calculator.div(20, 5), 4)
        #result = calculator.div(10, 5)

        with self.assertRaises(ValueError): # this is the context manager
            calculator.div(15, 0)

    def test_multi(self):
        self.assertEqual(calculator.multi(10, 5), 50)
        self.assertEqual(calculator.multi(10, 20), 200)
        self.assertEqual(calculator.multi(10, 14), 140)
        #result = calculator.mult(10, 5)


if __name__ == "__main__":
        unittest.main()

