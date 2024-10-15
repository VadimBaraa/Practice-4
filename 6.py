def selection_sort(arr):
    n = len(arr)
    # Проходим по массиву от последнего элемента к первому
    for j in range(n-1, 0, -1):
        # Ищем индекс максимального элемента в диапазоне от 0 до j
        max_index = 0
        for i in range(1, j+1):
            if arr[i] > arr[max_index]:
                max_index = i
        # Меняем местами максимальный элемент с элементом на позиции j
        arr[max_index], arr[j] = arr[j], arr[max_index]

# Пример использования
arr = [64, 225, 12, 22, 11, 1]
selection_sort(arr)
print("Отсортированный массив:", arr)