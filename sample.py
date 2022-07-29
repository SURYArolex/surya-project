#variables
phone_number = 1236
print(phone_number)

#numbers

int = 75, 1001
float = 867.101
salary ='200.7$'
print(salary)
print(type(salary))

a = 45
b = 55
c = a < b   #45 < 55
print(c)

a=25
b=35
c=45
d=55
e=a>b   #25>35
f=c<d    #45<55

g=e and f
print(g)

#srting
stringname = "hello world"
print(stringname)
fruit="apple"    #----index value start from 0 but length is 5
print(fruit[3])

demo = "string is oneamong python's data types' for print the below command"
print(demo)

#string holder or place holder

pgmlang = "python"
print("{} is a great programming language to learn".format(pgmlang))

print('python'," is a great programming language to learn")

string="prakashKUMAR"
print(string.upper())
print(string.lower())

demo1 = 'python is easy'
print(demo1.replace("easy", "powerfull"))


#slice skipping not executing

srting="python prgm is easy"
print(string[0:6])
print(len(string))

#list  -- store collection of object
 # listname = [obj1,obj2,obj3]

favfruits = ['apple', 'mango', 'graphs']
print(favfruits)
print(favfruits[1])
favfruits.append("kiwi")
print(favfruits)
favfruits.insert(1, "Banana")
favfruits.remove("kiwi")
favfruits.sort()
favfruits.reverse()
favfruits.pop()