import random
numbers1 = {random.randint(0,10) for _ in range(10)}
numbers2 = {random.randint(0,10) for _ in range(10)}
print(f"Первый набор: {numbers1}")
print(f"Второй набор: {numbers2}")
print(f"Элементы, которые входят в оба набора: {numbers1.intersection(numbers2)}")
print(f"Элементы, которые входят только в первый: {numbers1.difference(numbers2)}")
print(f"Элементы, которые входят только во второй: {numbers2.difference(numbers1)}")
print(f"Элементы, которые не входят в пересечение наборов: {numbers1.symmetric_difference(numbers2)}")