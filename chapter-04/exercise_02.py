#   4-3. Counting 1-20
for value in range(1, 21):
    print(value)

#   4-4. One million
values = []
for value in list(range(1, 1000001)):
    values.append(value)
print(values)

#   4-5. Summing Million
numbers, sum = [], 0
for num in range(1, 1000001):
    numbers.append(num)

if min(numbers) == 1 and max(numbers) == 1000000:
    for num in range(1, 1000001):
        sum = sum + num
    print(sum)

#   4-6. Odd numbers
odd_nums = list(range(1, 100, 2))
print(f'Odd numbers:\n{odd_nums}')

#   Even numbers
even_nums = list(range(2, 100, 2))
print(f'Even numbers:\n{even_nums}')
