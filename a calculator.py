#Matthew Walker
#10/3
#calculator

#creating a function for getting input
def getIntInput(message):
    x = 0
    while x == 0:
        num1 = input(message)
        if num1.isdigit():
            num1 = int(num1)
            x = 1
            return num1
        else:
            print("that wasn't a digit")
       
def getSymbolInput(message):
    x = 0
    while x == 0:
        symbols = "+","-","*","/","%"
        symbol = input(message)
        if symbol.isalnum():
            print("that wasn't a symbol")
        elif symbol not in symbols:
            print ("that is not a recognized symbol")
        else:
            x = 1
            return symbol

def calculate(num1,num2,symbol):
    print(type(num1))
    if type(num1) == int and type(num2) == int:
        if symbol == "+":
            answer = num1+num2
            return answer
        elif symbol == "-":
            answer = num1-num2
            return answer
        elif symbol == "*":
            answer = num1*num2
            return answer
        elif symbol == "/":
            if num1 == 0:
                num1 = getIntInput("you cant divide by 0 try again")
            else:
                answer = num1/num2
                return answer
        elif symbol == "%":
            if num1 == 0:
                num1 = getIntInput("you cant divide by 0 try again")
            else:
                answer = num1%num2
                return answer
    else:
        print("those are not ints we cant use them")

def doubleCalculate(num1,num2,symbol):
    if symbol == "+":
        answer2 = num1+num2
    elif symbol == "-":
        answer2 = num1-num2
    elif symbol == "*":
        answer2 = num1*num2
    elif symbol == "/":
        if num1 == 0:
            num1 = getIntInput("you cant divide by 0 try again")
        else:
            answer = num1/num2
    elif symbol == "%":
        if num1 == 0:
            num1 = getIntInput("you cant divide by 0 try again")
        else:
            answer = num1%num2
    return answer2

def main():
    num1 = getIntInput("enter a digit")
    num2 = getIntInput("enter another digit")
    symbol = getSymbolInput("enter a mathmatical symbol")
    answer = calculate(num1,num2,symbol)
    answer2 = doubleCalculate(num1,num2,symbol
    if answer == answer2
        print("after a double check your answer is",answer)
    else:
        print(answer)

main()
