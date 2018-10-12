#Matthew Walker
#sept 21
#change sorter

def change():
    #1 get input from user how much change
    totalChange = int(input("how much change do you have on you?"))
    #2 calculate total for d q n d p
    dollar = totalChange // 100
    whatsLeft = totalChange % 100
    quarters = totalChange // 25
    whatsLeft = totalChange % 25
    dimes = whatsLeft //10
    whatsLeft = whatsLeft % 10
    nickles = whatsLeft // 5
    whatsLeft = whatsLeft % 5
    penneys = whatsLeft
    #3 display it back to user
    print("Quarters: ",quarters,"\nDimes:",dimes,"\nNickles:",nickles,"\npenneys",penneys)
    input("press enter")


change()

def change2(totalChange):
    #1 get input from user how much change
    totalChange = totalChange
    #2 calculate total for d q n d p
    dollar = totalChange // 100
    whatsLeft = totalChange % 100
    quarters = whatsLeft // 25
    whatsLeft = whatsLeft % 25
    dimes = whatsLeft //10
    whatsLeft = whatsLeft % 10
    nickles = whatsLeft // 5
    whatsLeft = whatsLeft % 5
    penneys = whatsLeft
    #3 return value
    return dollar, quarters, dimes, nickles, penneys

totalChange = int(input("how much change do you have on you?"))
dollar, quarters, dimes, nickles, penneys = change2(totalChange)
print("Dollar:",dollar,"\nQuarters: ",quarters,"\nDimes:",dimes,"\nNickles:",nickles,"\npenneys",penneys)
