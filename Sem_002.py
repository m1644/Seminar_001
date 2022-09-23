# Задача 2. Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них. 

numbers = []
for i in 1, 2, 3, 4, 5:
    numbers.append(int(input()))
print(numbers)
max = numbers[0]
for i in numbers:
    if max < i: max = i
print(max)
