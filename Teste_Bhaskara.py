####Função Bhaskara refatorada com retornos ao invés de prints e orientado a objetos####

import math

class Bhaskara:

        def delta(self, a, b, c):
            return (b**2 - 4*a*c)

        def main(self):
            a_digitado = float(input("Digite a variável a: "))
            b_digitado = float(input("Digite a variável b: "))
            c_digitado = float(input("Digite a variável c: "))
            print(self.calcula_raizes(a_digitado,b_digitado,c_digitado))


        def calcula_raizes(self, a,b,c):
            d = self.delta(a,b,c)
            if d < 0 :
                return 0
            else:     
                if d == 0:
                    x = (-b / (2*a))
                    return 1, x   
                else:
                    x1 = (-b + math.sqrt(d)) / (2*a)
                    x2 = (-b - math.sqrt(d)) / (2*a)
                    return 2, x1, x2
                    
     
