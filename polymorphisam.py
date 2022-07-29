#polymorphism------ Different conditions different acts.

class employee:
    def setnumberofworkinghours(self):
     self.numberofworkinghours = 40
    def displaythenumberworkinghours(self):
        print(self.numberofworkinghours)


class trainee(employee):
    def setnumberofworkinghours(self):
       self.numberofworkinghours = 45

employee = employee()
employee.setnumberofworkinghours()
print("number of working hours of the employee:", end=' ')
employee.displaythenumberworkinghours()


class Employee:
    def setnumberofworkinghours(self):
     self.numberofworkinghours = 40
    def displaythenumberofworkinghours(self):
        print(self.numberofworkinghours)


class Trainee(Employee):
    def setnumberofworkinghours(self):
       self.numberofworkinghours = 45
    def resetnumberofworkinghours(self):
        super().setnumberofworkinghours()

employee = Employee()
employee.setnumberofworkinghours()
print("number of working hours of the employee:", end=' ')
employee.displaythenumberofworkinghours()

trainee = Trainee()
trainee.setnumberofworkinghours()
print("number of working hours of the employee:", end=' ')
trainee.displaythenumberofworkinghours()
trainee.resetnumberofworkinghours()
print("number of working hours has been reset:",end=' ')
trainee.displaythenumberofworkinghours()