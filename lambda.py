#lambda function------

x =  lambda a,b : a+b
print(x(2,5))

def myfunc(n):
      return lambda a : a * n
mytripler = myfunc(3)
mydoubler = myfunc(2)
print(mydoubler(10))
print(mytripler(11))