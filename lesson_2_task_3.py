import math

def square(side):
    area = side * side
    
    if isinstance(side, int):
        return area
    else:
        return math.ceil(area)

side1 = 5
result1 = square(side1)
print(f"Сторона: {side1}, Площадь: {result1}")

side2 = 4.3
result2 = square(side2)
print(f"Сторона: {side2}, Площадь: {result2}")

side3 = 7.8
result3 = square(side3)
print(f"Сторона: {side3}, Площадь: {result3}")

side4 = 3
result4 = square(side4)
print(f"Сторона: {side4}, Площадь: {result4}")