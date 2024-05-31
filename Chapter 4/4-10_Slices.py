#4-10

alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']

print('The first three items in the last are:')
print(alphabet[:3])

print('Three items from the middle of the list are:')
print(alphabet[2:6])

print('The last three items in the last are:')
print(alphabet[-3:])

#4-11

pizzas = ['Neapolitan', 'Sicilian', 'Detroit', 'New York', 'Margherita', 'Roman','St.Louis']

friend_pizzas = pizzas[:]

pizzas.append('New')
friend_pizzas.append('Another')

print("My favorite pizzas are:")
for pizza in pizzas:
  print(pizza)

print("My friend's favorite pizzas are:")
for pizza in friend_pizzas:
  print(pizza)


#4-12 eazy

