import sys

class Calculator:
    def __init__(self):
        self.__precio = 10
        self.__tax = 0.08

    def calculate(self, precio, cantidad, estado):
        print('{0}, {1}, {2}'.format(precio, cantidad, estado))
        return self.total(precio, cantidad, estado, self.__tax)

    def subTotal(self, precio, cantidad):
        return float(precio) * float(cantidad)

    def aplicarDcto(self, st, dcto):
        return st * (1 - float(dcto))

    def aplicarTax(self, valor, tax):
        return valor * (1 + float(tax))
    
    def porcentajeDcto(self, subTotal):
        if subTotal > 0 and subTotal >= 1000:
            return 0.03
        
        # elif subTotal >= 5000:
        #     return 0.05
        # elif subTotal >= 7000:
        #     return 0.07
        # elif subTotal >= 10000:
        #     return 0.1
        # elif subTotal >= 50000:
        #     return 0.15
        return 0

    def total(self, precio, cantidad, estado, tax):
        subtotal = self.subTotal(precio, cantidad)
        dct = self.porcentajeDcto(subtotal)
        sst = self.aplicarDcto(subtotal, 0) 
        return self.aplicarTax(sst, tax)
        

# calculator = Calculator()

# print(calculator.calculate(sys.argv[1], sys.argv[2], sys.argv[3]))

