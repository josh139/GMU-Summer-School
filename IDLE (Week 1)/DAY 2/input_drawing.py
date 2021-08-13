import turtle

window = turtle.Screen()
pen = turtle.Turtle()

window.title("Input Drawing")

shape = input("What shape would you like to draw? - ")

shape = shape.lower()

if shape == "circle":
    pen.circle(150)
elif shape == "square":
    pen.right(90)
    pen.forward(200)
    pen.right(90)
    pen.forward(200)
    pen.right(90)
    pen.forward(200)
    pen.right(90)
    pen.forward(200)
elif shape == "triangle":
    pen.forward(200)
    pen.left(120)
    pen.forward(200)    
    pen.left(120)
    pen.forward(200)
