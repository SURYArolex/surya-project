fruits = ["apple", "mango", "orange", "strawberry"]
print(fruits)
for fruit in fruits:
    print(fruit)


# range()
for number in range(1, 10):
    print(number)

#while loop
temp = 77

# 68 - 77 deg f
while temp >= 68 and temp <= 77:
    print("room temp is maintained at {} deg f".format(temp))
    temp = temp - 1
number = 1
for row in range(1, 4):
    for column in range(1, 4):
        print(number, end='  ')
        number = number + 1
    print()