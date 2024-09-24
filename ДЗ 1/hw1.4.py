numbers = [i for i in range(1, 60, 2)]
print(numbers)
num = [i for i in numbers if (i % 3 == 0 or i % 5 == 0) and i % 15 != 0]
print(num)
print(num[-1])