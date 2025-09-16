# class attributes - instance vs class attributes
#instance - attributes defined with in __init__ , they are unique to each instance
#class attributes - defined outside the constructor, belongs to class and share across object.
     
class Course:
    # class attribute
    course_name = "Python Programming"

    def __init__(self, instructor):
        # instance attribute
        self.instructor = instructor

if __name__ == "__main__":
    course1 = Course("Alice")
    course2 = Course("Bob")
    print("Course Name:", Course.course_name)
    print("Instructor for Course 1:", course1.instructor)
    print("Instructor for Course 2:", course2.instructor)

    # Accessing class attribute using object name
    print("Course Name (from instance):", course1.course_name)
    print("Course Name (from instance):", course2.course_name)

    # Check instance
    print("isinstance(course1, Course):", isinstance(course1, Course))
    print("isinstance(course2, Course):", isinstance(course2, Course))
