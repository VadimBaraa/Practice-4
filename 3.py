def find_longest_sequence(arr):
    if not arr:
        return 0, -1  # Если массив пустой

    max_len = 1  # Длина самой длинной последовательности
    max_start_index = 0  # Начальный индекс самой длинной последовательности

    current_len = 1  # Длина текущей последовательности
    current_start_index = 0  # Начальный индекс текущей последовательности

    for i in range(1, len(arr)):
        if arr[i] == arr[i - 1]:
            current_len += 1
        else:
            # Проверяем, является ли текущая последовательность самой длинной
            if current_len > max_len:
                max_len = current_len
                max_start_index = current_start_index
            # Сбрасываем текущую последовательность
            current_len = 1
            current_start_index = i

    # Проверяем последнюю последовательность
    if current_len > max_len:
        max_len = current_len
        max_start_index = current_start_index

    return max_len, max_start_index


# Пример использования
arr = [1, 2, 2, 2, 3, 3, 4, 4, 4, 4, 4, 5]
length, start_index = find_longest_sequence(arr)
print(f"Длина самой длинной последовательности: {length}, начальный индекс: {start_index}")