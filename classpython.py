# ********* class **********
class Student:
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course


print("students details:")

student1 = ("surya", 21, "bca")
student2 = ("tamil", 22, "bba")
student3 = ("karthick", 24, "bcom")
print(student2[1])


# 2 exaple
class calc:
    num = 100
    def getdata(self,c,d):
        self.firstnumber = c
        self.secondnumber = d
        print("Hi in function")
    def summation(self):
        return self.firstnumber +self.secondnumber + calc.num
obj = calc()
obj.getdata(40,40)
print(obj.summation())

obj1 = calc()
obj1.getdata(50,50)
print(obj1.summation())