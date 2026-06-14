import math

def square(side_sq):
    return math.ceil(side_sq*side_sq)

side = float(input("Введите сторону квадрата: "))
result = square(side)
print(f"Площадь квадрата со стороной {side}, округленная до целого числа в верх, равна: {result}")