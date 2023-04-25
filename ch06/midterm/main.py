import turtle as t
import random 

#Global Space
fantasy = int(input("How many circular hats do you WANT Mr. Susmeister to Have? Enter a number: "))
reality  = int(input("How many circular hats should he realistically have? Enter a number: "))

def optimalhats(fantasy, reality):
    ''' 
    This function averages together what your creative side craves and what your logical side accepts is appropriate for the quantity of hats for Mr. Susmeister.
    Args: (int) any 2 integers
    Returns: (int) average of the 2 values as an integer without remainder 
    '''
    return fantasy * reality // 2  

def main(): 
    pen = t.Turtle()
    pen.color('black', 'orange')
    screen = t.Screen()

    #face
    pen.begin_fill()
    pen.circle(100)
    pen.end_fill()
    pen.penup()

    #eyes 
    xcors = [-35,35]
    for _ in range(1):
        for i in xcors:
            i = int(i)
            pen.goto(i, 140)
            pen.pendown()
            pen.circle(20)
            pen.penup()
    #mouth 
    pen.width(15)
    pen.goto(-70,70)
    pen.pendown()
    pen.setheading(-70)
    pen.circle(80, 140) 
    pen.penup()

    #big ole tooth 
    pen.width(20)
    pen.goto(0,0)
    pen.pendown()
    pen.begin_fill()
    for r in range(4):
        pen.left(90)
        pen.forward(50)
    pen.end_fill()
    pen.penup()
    
    #hat
    colors = ['red','green','blue', 'purple', 'pink']
    optimal = optimalhats(fantasy, reality)
    for i in range(optimal):
        pen.goto(50,230) 
        pen.pendown()
        pen.color(random.choice(colors))
        pen.circle(50) 
        pen.pendown()
    screen.exitonclick() 

main()