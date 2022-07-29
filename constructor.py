#CONSTRUCTOR

class calc:
    num = 100
    def getdata(self,c,d):
        self.firstnumber = c
        self.secondnumber = d
        print("Hi in function")
    def summation(self):
        return self.firstnumber +self.secondnumber + self.thirdnumber+self.fourthnumber+ calc.num
    def __init__(self,a,b):
        self.thirdnumber = a
        self.fourthnumber = b
        print("am running first")

obj = calc(20,20)
obj.getdata(40,40)
print(obj.summation())