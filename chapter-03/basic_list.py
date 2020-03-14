#   3-1. Names
names = ['himel', 'fariya', 'inteser']
print(names[0])
print(names[1])
print(names[2])

#   3-2. Greetings
print(f"Hi there, {names[0].title()}")
print(f"Hi there, {names[1].title()}")
print(f"Hi there, {names[2].title()}")

#   3-3
# same as before

#   3-4. Guest List

#   3-5. Changing Guest List


cars = []
cars.append('bike')
cars.append('motor')
cars.insert(0, 'bokati')
print(cars)
cars.remove('motor')
print(f"Size = {len(cars)}")
print(cars)

#   Basic operation in List
books = ['python', 'c', 'c++']
print(len(books))
removed_book = books.pop()
print(removed_book)
print(books)

#   Pop & Del
books = ['python', 'c', 'c++']
print(len(books))
removed_book = books.pop()
print(removed_book)
print(books)

del books[0]
print(books)


#   sort & reverse


frouits = ['apple', 'orange', 'mango', 'pineapple']
frouits.sort()  # normal sort
print(frouits)
frouits.sort(reverse=True)  # reverse
print(frouits)
