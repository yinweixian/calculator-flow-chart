#Matthew Walker
#9/18
#get name function
#def get_name():


    #ask user for name
    #name = input("what is your name?")
    #verify name
    #check = input = ("did you enter",name)


    #display name
    #print("the name you entered was",name)

#print("this is our function")
#get_name()


#def areaOfCircle():
    #PI=3.14159265
#1 get a radius
    #radius = input("what is the radius")
    #radius=float(radius)
#2 get the area
    #area=radius*radius*pi
#3 display iformation
    #print("the area of the circle is:",area)
#areaOfCircle()
#square
import turtle
#def square(side):
    #for i in range(4):
        #turtle.fd(side)
        #turtle.left(90)
#main
#size = int(input("Lets draw a square. how longe do you want the sides?"))
#square(size)
#input("press a key to quit.")

def draw_square(some_turtle):
    for i in range(1,5):
        some_turtle.forward(100)
        some_turtle.right(93)

def draw_art():
    window = turtle.Screen()
    window.bgcolor("red")
    #create the turtle brad - draws a square
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("yellow")
    brad.speed(1000)
    for i in range(1,5):
        draw_square(brad)
        brad.right(10)
    #create the turtle angie - draws a circle
    #angie

    window.exitonclick()

draw_art()













































