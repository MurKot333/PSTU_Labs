import math

x = float(input("Введите значение переменной x: "))
y = float(input("Введите значение переменной y: "))
z = float(input("Введите значение переменной z: "))

a = math.sqrt((x**3)/2) - math.sin(y)
print(f"Получено значение функции a={a}")
b = (math.exp(1)**2)/3 - math.cos(y) + z + math.log(y,math.exp(1))
print(f"Получено значение функции b={b}")


