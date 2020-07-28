# assignment 3
# task 1

# reduce function


def myreduce(function, seq):
    it = iter(seq)
    value = next(it)
    for element in it:
        value = function(value, element)
    return value

# custom sum function


def mysum(a, b):
    value = a+b
    return value


seq = (1, 2, 3, 5, 6, 7, 8)

value = myreduce(mysum, seq)
print(value)

# Task 2
# filter function


def my_filter(func, sequence):
    res = []
    for variable in sequence:
        if func(variable):
            res.append(variable)
    return res

# function to check even number


def is_even(item):
    item = int(item)
    if item % 2 == 0:
        return True
    else:
        return False


seq = ['2', '3', '6', '456', '56', '9', '10', '77', '11', '22', '44', '66']

print(my_filter(is_even, seq))

# task 3
letters = ['x','y', 'z']
lst = [a*i for a in letters for i in range(1, 6)]
print(lst)

lst2 = [a*i for i in range(1, 6) for a in letters]
print(lst2)

lst3 = [[a+i] for i in range(1, 4) for a in range(1, 4)]
print(lst3)

number = [1, 2, 3, 4]
lst4 = [list(map(lambda x: x + k, number)) for k in range(1, 5)]
print(lst4)

lst5 = [(a, i) for i in range(1, 4) for a in range(1, 4)]
print(lst5)
