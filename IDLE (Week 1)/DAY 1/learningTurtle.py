import turtle

window = turtle.Screen()
pen = turtle.Turtle()
 
window.title("Drawing Graphics")

pen.pensize(15)
pen.color("orange")
pen.fillcolor("orange")
pen.begin_fill()

pen.forward(300)
pen.left(90)

pen.forward(300)
pen.left(90)

pen.forward(300)
pen.left(90)

pen.forward(300)
pen.left(90)

pen.end_fill()

pen.pensize(20)
pen.color("green")

pen.up()
pen.forward(270)
pen.left(90)
pen.forward(150)
pen.down()

pen.circle(120)
