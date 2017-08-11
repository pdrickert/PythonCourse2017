items = [1, 2, 3, 4, 5]

squared = list(map(lambda x: x**2, items))

def multiply(x):
    return (x*x)

def add(x):
    return (x+x)

funcs = [multiply, add]
for i in range(5):
    value = list(map(lambda x: x(i), funcs))
    print(value)


my_list = ['apple', 'banana', 'grapes', 'pear']
for c, value in enumerate(my_list, 1):
    print(c, value)

my_list2 =



###

number_list = range(-5, 4)
less_than_zero = list(filter(lambda x: x < 0, number_list))
print(less_than_zero)

product = 1
mylist = [1, 2, 3, 4]
for num in mylist:
    product = product * num

from functools import reduce
product = reduce((lambda x, y: x * y), [1, 2, 3, 4])
product = reduce((lambda x, y: x**2 + y**2), [1, 2, 3, 4])
