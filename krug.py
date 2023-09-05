radius_1 = input("Введите радиус")
pie_1 = input("Введите число пи")
pie_2 = int(pie_1) # Переводим строку пи в число
radius_2 = int(radius_1) # Переводим строку длины радиуса в число
length = 2 * pie_2 * radius_2 # Применяем формулу длины окружности
square = pie_2 * radius_2 ** 2 # Применяем формулу площади круга
print(length) # Принтим длину
print(square) # и площадь