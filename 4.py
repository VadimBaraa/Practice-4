def has_duplicates(arr):
    seen = set()
    for num in arr:
        if num in seen:
            return True
        seen.add(num)
    return False

# Пример использования
arr = [1, 2, 3, 4, 5, 6, 7]
if has_duplicates(arr):
    print("В массиве есть одинаковые элементы")
else:
    print("Все элементы массива уникальны")