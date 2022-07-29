#conditional Statements
#if--condition
#if--else condition
#if-elif condition

totalmarks = 95
if totalmarks >= 90:
    print("congrats you have securd 'A' greade")

#ELSE

totalmarks = 85
if totalmarks >= 90:
    print("congrats you have securd 'A' grade")
else:
    print("Youn have cleared the exams")

#3 condition

totalmarks = 60
if totalmarks >=90:
    print("congrats you have securd 'A' grade")
elif totalmarks >= 40:
    print("congrats u have cleared the exam")
else:
    print("you have failed the exam")

#nested if condition

totalmarks = 100
if totalmarks >= 90:
     print("congrats you have secured 'A' grade")
if totalmarks == 100:
     print("you have also secure full marks")