# Functions - can have multiple statements, a name , can be reused and documented


def mySimpleFunction():
    return "simple function invoked"


# Lambdas - are limited to a single expression. typically used for short , simple operations

# 1. Add two numbers

print("Lambdas example")
add = lambda x, y: x + y

print(add(4,7))

numbers = [1, 2, 3, 4, 5, 6]
evens = list(filter(lambda x: x % 2 == 0, numbers))

for val in evens:
    print(val)

pairs=[(1,3),(2,2),(4,1)]
print("pairs sorted using lambda",sorted(pairs,key= lambda x:x[1]))

