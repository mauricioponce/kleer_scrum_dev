import unittest
from saludador import Calculator

# print('dcto: {0}'.format(calculator.aplicarDcto(10, 0))
# print('tax: {0}'.format(calculator.aplicarTax(10, 0.08)))
# print('dcto: {0}'.format(calculator.porcentajeDcto(5001)))

class SaludadorTest(unittest.TestCase):
    def test_calculate(self):
        c = Calculator()  

        s = c.calculate(10, 1, 'ca')
        self.assertEqual(10.8, s) 

    def test_subTotal_isCorrect(self):
        c = Calculator()

        st = c.subTotal(10, 1)
        self.assertEqual(10, st) 

    def test_subTotal_withDecimal_isCorrect(self):
        c = Calculator()

        st = c.subTotal(10.1, 1.1)
        self.assertAlmostEqual(11.1, st, 1) 
