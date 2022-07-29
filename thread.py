# Example 1
import threading
t = threading.current_thread()                  # return the current thread object
print("current thread:",t)                      # print the thread name,insetifier and status
print("thread name:",t.name)
print("thread identifier:",t.ident)
print("is the thread alive:",t.is_alive())
t.name='Mythread'
print("After name change:",t.name)


# Example 2

import threading
def fun1():
    print("function 1")
def fun2():
    print("function 2")
th1= threading.Thread(name="MY first Thread",target = fun1)
th2= threading.Thread(target=fun2)

th1.start()
th2.start()


# Example 3

import time
def display(x,s,name):
    for i in range(x):
        time.sleep(s)
        print(name, "")
t = threading.Thread(target = display, args = (5, 1, "thread start",))
t.start()
t1 = threading.Thread(target = display, args = (5, 1, "thread end"))
t1.start()