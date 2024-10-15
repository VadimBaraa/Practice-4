import numpy as np

# Создаем случайный одномерный массив
array = np.random.randint(1, 101, size=10)

# Находим минимальный и максимальный элементы
min_element = np.min(array)
max_element = np.max(array)

# Вычисляем их разность
difference = max_element - min_element

print(array, min_element, max_element, difference)
