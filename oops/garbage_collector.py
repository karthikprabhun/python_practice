#source https://www.tutorialspoint.com/python/python_classes_objects.htm

# Create object <40>
a = 40      
# Increase ref. count  of <40> 
b = a       
# Increase ref. count  of <40> 
c = [b]     

# Decrease ref. count  of <40>
del a       
# Decrease ref. count  of <40>
b = 100      
# Decrease ref. count  of <40>
c[0] = -1 

class Point:
   def __init__( self, x=0, y=0):
      self.x = x
      self.y = y
   def __del__(self):
      class_name = self.__class__.__name__
      print (class_name, "destroyed")

pt1 = Point()
pt2 = pt1
pt3 = pt1
# prints the ids of the obejcts
print (id(pt1), id(pt2), id(pt3))
del pt1
del pt2
del pt3
print(" all destroyed")

print(" ------------------- another variation -------------------------")

class Point2:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __del__(self):
        class_name = self.__class__.__name__
        print (class_name, "destroyed")


if __name__ == "__main__":
    p1 = Point2(10, 20)
    p2 = Point2(30, 40)
    print("Created points:", id(p1), id(p2))

    p3 = p1
    p4 = p1
    print("Created points:", id(p3), id(p4))

    del p1
    p2 = Point2(50, 60) # reassigning reference is done, so __del__ invoked
    print("Created point:", id(p2))

    del p3
    del p4
    del p2
    print(" all destroyed")

print(" as you can see del destroy the object and gc will automatically reclaim memory")