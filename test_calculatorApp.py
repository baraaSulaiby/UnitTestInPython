from asyncio.windows_events import NULL
from decimal import DivisionByZero
import unittest
from unittest import mock
from unittest.mock import patch

from importlib_metadata import NullFinder
from calculatorApp import *
import calculatorApp

## assertEqual used to ensure that the returned results are as expected.
class TestCalculate(unittest.TestCase):
    def setUp(self):
        print("Setup .. ")

    def test_AddPass(self):
        self.assertEqual(add(5, 2), 7)  


    def test_substraction(self):
        self.assertEqual(subtract(10, 8),2)


    def test_multiplication(self):
        self.assertEqual(multiply(2,2), 4)


    
    def test_division(self):
        self.assertRaises(ZeroDivisionError,divide, 5,0)
        self.assertEqual(divide(0, 8), 0)
        self.assertEqual(divide(10, 5),2)

    
    def test_isExist(self):
        self.assertEqual(isExit("no"), True)
        self.assertEqual(isExit("yes"), False)
        self.assertRaises(ValueError,isExit,"w")

    def test_calculate(self):
        self.assertRaises(ValueError,calculate,1,NULL,5)
        self.assertRaises(Exception,calculate,5,7,3)
        with mock.patch('calculatorApp.add', return_value = 10):
            result = calculate('1',5,5)
        self.assertEqual(result, 10)
        with mock.patch('calculatorApp.subtract', return_value = -1):
            result = calculate('2',7,8)
        self.assertEqual(result, -1)
        with mock.patch('calculatorApp.multiply', return_value = 25):
            result = calculate('3',5,5)
        self.assertEqual(result, (5,'*',5,'=',25))
        with mock.patch('calculatorApp.divide', return_value = 2):
            result = calculate('4',12,6)
        self.assertEqual(result, (12,'/',6,'=',2))
        self.assertRaises(ZeroDivisionError,calculate,"4",1,"0")

    def test_user_input(self):
        self.assertRaises(ValueError,check_user_input,"")
        self.assertRaises(ValueError,check_user_input,"w")
        self.assertEqual(check_user_input("8"), 8)
        self.assertEqual(check_user_input("8.0"), 8.0)




if __name__ == '__main__':
    unittest.main()