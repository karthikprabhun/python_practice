
from abc import ABC, abstractmethod


class demoInterface(ABC):
    @abstractmethod
    def demo_method1(self):
        pass

    def demo_method2(self):
        pass

class concreteclass(demoInterface):
    def demo_method1(self):
        print("Implementation of demo_method1")

    def demo_method2(self):
        print("Implementation of demo_method2")

obj = concreteclass()
obj.demo_method1()
obj.demo_method2()

print("-------------- Informal interface - without abstract methods ------")

class demoInterface2:
    def demo_method1(self):
        pass

class concreteclassForDemoInterface2(demoInterface2):
    def demo_method1(self):
        print("Implementation of demo_method1 in concreteclassForDemoInterface2")

obj2 = concreteclassForDemoInterface2()
obj2.demo_method1()

print(type(obj))