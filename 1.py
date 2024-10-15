import numpy as np

# Функция для нахождения суммы и произведения элементов массива
def sum_and_product(arr):
    total_sum = np.sum(arr)
    total_product = np.prod(arr)
    return total_sum, total_product

arr = [2, 3, 4, 5]
total_sum, total_product = sum_and_product(arr)

print(f"Сумма элементов: {total_sum}")
print(f"Произведение элементов: {total_product}")
