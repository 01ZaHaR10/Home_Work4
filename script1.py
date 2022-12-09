import random
Arrays = [random.randint(-100, 100) for _ in range(10)]
print(f"Исходный массив: {Arrays}")

def swap(arrays, i, j):
    t = arrays[i]
    arrays[i] = arrays[j]
    arrays[j] = t

def bubbleSort(array):
    for i in range(0, len(array) - 1):
        for j in range(0, len(array) - 1 - i):
            if array[j] > array[j + 1]:
                swap(array, j, j + 1)
    return array

print(f"Отсортированный массив: {bubbleSort(Arrays)}")