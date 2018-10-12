#name = input("what is your name")
#age = int(input("what is your age"))

#if 76 > age > 17:
 #   print("I can drive")
#elif age > 76:
 #   print("your old")
#elif age < 16:
 #   print("your to young")
#else:
#    print("how could this happen?")

#Matthew Walker
#sept 27

num1 = input("enter a number")
num2 = input("enter a second number")

if num1.isdigit() and num2.isdigit():
    print("you passed my test. ")
elif num1.isdigit():
    print("you are half right num1 is",num1)
elif num2.isdigit():
    print("you are half right num2 is",num2)
else:
    print("you halve to enter numbers")
