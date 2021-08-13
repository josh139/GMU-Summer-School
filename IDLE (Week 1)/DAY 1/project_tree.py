import turtle

window = turtle.Screen()
pen = turtle.Turtle()

window.title("Tree")

pen.pensize(5)
pen.color("brown")
pen.fillcolor("brown")
pen.begin_fill()

pen.up()
pen.left(180)
pen.forward(50)
pen.right(90)
pen.down()

pen.right(90)
pen.forward(100)
pen.right(90)
pen.forward(200)
pen.right(90)
pen.forward(100)
pen.right(90)
pen.forward(200)

pen.end_fill()

pen.color("green")
pen.fillcolor("green")
pen.begin_fill()

pen.circle(50)
pen.end_fill()

pen.up()
pen.right(90)
pen.forward(100)
pen.right(90)
pen.down()

pen.fillcolor("green")
pen.begin_fill()
pen.circle(50)
pen.end_fill()

pen.up()
pen.left(180)
pen.right(60)
pen.down()

pen.fillcolor("green")
pen.begin_fill()
pen.circle(100)
pen.end_fill()
