import turtle 

sides = input ("Number of Sides: ")
length = input ("Length of Each Side: ")
sides = int(sides)
length = int(length)

pen = turtle.Turtle()
pen.color("red")

window = turtle.Screen()


for s in range(sides):
    pen.forward(length)
    pen.right (360/sides)
    
window.exitonclick()