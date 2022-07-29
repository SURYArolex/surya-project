#break
number = 1
for number in range(1,11):
    if number == 5:
       break
    print(number)
else:
  print(number)

# continue

for number in range(1,11):
    if number == 5:
       continue
    print(number)