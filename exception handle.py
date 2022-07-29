#EXCEPTION HANDLING

try:
    length = 10
    width =  0
    length/width
except:
      print("Division by zero is invalid kindly change your input")

try:
    length = 10
    width =  0
    length/width
except ZeroDivisionError:
      print("Division by zero is invalid kindly change your input")
      length = 10
      area=length/width
print(area)

try:
    length = 10
    length/width
except NameError:
      print("variable has been used before defining it")
except ZeroDivisionError:
      print("Division by Zero is Invalid kindly change ur input")
except Exception:
      print("New error has occured")
finally:
      print("i will be executed atleast one")