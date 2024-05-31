for value in range(1, 6):
  print(value)
  
for value in range(6):
  print(value)
  
numbers = list(range(1,6))
print(numbers)

# even numbers

even_numbers = list(range(2, 11, 2))
print(even_numbers)

# squares of numbers
squares = []
for value in range(1, 11):
  #square = value ** 2
  squares.append(value**2)
  
print(squares)

# min max sum
digits = list(range(0, 10))
print(digits)
print(min(digits))
print(max(digits))
print(sum(digits))