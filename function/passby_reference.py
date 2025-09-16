def testFunction1(arg):
    print("Value received:", id(arg))
    arg += 5
    print("Value after modification:", id(arg))

def testFunction2(arg):
    print("Value received:", id(arg), " of type ", type(arg))
    arg.append("Lion")
    print("Value after modification:", id(arg))

def testFunction3(arg):
    print("Value received:", id(arg), " of type ", type(arg))
    arg.update({"peacock": 4})
    print("Value after modification:", id(arg))

if __name__ == "__main__":
    print("demo passing immutable variables string and number")
    val=10
    print(f"id before passing the variable value {val}: with id {id(val)}")
    testFunction1(val)
    val='yuki'
    print(f"id before passing the variable value {val}: with id {id(val)}")
    print('-------------------------------------')

    print("Demo passing mutable variables - list and dict")
    animals = ["cat", "dog", "rabbit"]
    print(f"id before passing the variable value {animals}: with id {id(animals)}")
    testFunction2(animals)
    print(f"id after passing the variable value {animals}: with id {id(animals)}")

    dict_birds = {"sparrow": 1, "eagle": 2, "parrot": 3}
    print(f"id before passing the variable value {dict_birds}: with id {id(dict_birds)}")
    testFunction3(dict_birds)
    print(f"id after passing the variable value {dict_birds}: with id {id(dict_birds)}")


# The behavior also depends on whether the passed object is mutable or immutable.
#  Python numeric object is immutable. 
# When a numeric object is passed, and then the function changes the value of the formal argument, it actually creates a new object in the memory, leaving the original variable unchanged.

#But in case of mutable objects like lists or dictionaries, the behavior is different. If the function modifies the contents of the object (like adding or removing elements), those changes will be reflected in the original object outside the function.
