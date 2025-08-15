import math

x1 = float(input("Digite a variável x1: "))
y1 = float(input("Digite a variável y1: "))
x2 = float(input("Digite a variável x2: "))
y2 = float(input("Digite a variável y2: "))

d = math.sqrt((x1 - x2)**2 + (y1 -y2)**2)

if (d >= 10):
    print("longe")
else:
    print("perto")
    
      