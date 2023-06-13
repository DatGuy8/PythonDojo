num1 = 42       # variable declaration,numbers 
num2 = 2.3      # variable declaration, numbers
boolean = True      # variable declaration, boolean
string = 'Hello World'      #variable declatrion, string
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives']       #variable declatrion list intialize
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} #variable declatrion dictionay intialize
fruit = ('blueberry', 'strawberry', 'banana')   #variable declatrion, tuples intialize
print(type(fruit))    #tuples, access value
print(pizza_toppings[1])     #access value list
pizza_toppings.append('Mushrooms')     #add value list
print(person['name'])   #access value dictionary
person['name'] = 'George'   #change value dictionary
person['eye_color'] = 'blue'    # add value dictionary
print(fruit[2])         #access value tuples

if num1 > 45:                          
    print("It's greater")
else:
    print("It's lower")                  '''conditional if'''

if len(string) < 5:                 
    print("It's a short word!")
elif len(string) > 15:
    print("It's a long word!")
else:
    print("Just right!")                '''else if'''

for x in range(5):              '''FOR LOOP START'''
    print(x)
for x in range(2,5):            ''''''
    print(x)
for x in range(2,10,3):
    print(x)
x = 0
while(x < 5):
    print(x)
    x += 1

pizza_toppings.pop()
pizza_toppings.pop(1)

print(person)
person.pop('eye_color')
print(person)

for topping in pizza_toppings:
    if topping == 'Pepperoni':
        continue
    print('After 1st if statement')
    if topping == 'Olives':
        break

def print_hello_ten_times():
    for num in range(10):
        print('Hello')

print_hello_ten_times()

def print_hello_x_times(x):
    for num in range(x):
        print('Hello')

print_hello_x_times(4)

def print_hello_x_or_ten_times(x = 10):
    for num in range(x):
        print('Hello')

print_hello_x_or_ten_times()
print_hello_x_or_ten_times(4)


"""
Bonus section
"""

# print(num3)
# num3 = 72
# fruit[0] = 'cranberry'
# print(person['favorite_team'])
# print(pizza_toppings[7])
#   print(boolean)
# fruit.append('raspberry')
# fruit.pop(1)