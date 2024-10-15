def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        # Флаг для оптимизации: если за проход не было обменов, значит массив отсортирован
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                # Меняем элементы местами
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        # Если не было обменов, то массив уже отсортирован
        if not swapped:
            break

# Пример использования
arr = [64, 34, 25, 122, 22, 113, 90]
bubble_sort(arr)
print("Отсортированный массив:", arr)