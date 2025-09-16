

class Employee:
     def __init__(self):
          self.__name = ""
          self.__salary = 0

     def display(self):
          print("Name:", self.__name)
          print("Salary:", self.__salary)

     def setName(self, name):
          self.__name = name

     def getName(self):
          return self.__name

     def setSalary(self, salary):
          self.__salary = salary

     def getSalary(self):
          return self.__salary
     
class SalesOfficer(Employee):
     def __init__(self):
          super().__init__()
          self.__commission = 0

     def display(self):
          print("Name:", self.getName(),", total salary:", self.getSalary() + self.getCommission())

     def setCommission(self, commission):
          self.__commission = commission

     def getCommission(self):
          return self.__commission
     
     
     
if __name__=="__main__":
     emp = Employee()
     emp.setName("John Doe")
     emp.setSalary(50000)
     emp.display()

     print("------------------------------------------------------------")

     sales_emp = SalesOfficer()
     sales_emp.setName("Yuki Ja")
     sales_emp.setSalary(60000)
     sales_emp.setCommission(5000)
     sales_emp.display()