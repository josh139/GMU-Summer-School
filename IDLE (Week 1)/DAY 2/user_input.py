import turtle
 
w = turtle.Screen()
t = turtle.Turtle()
 
w.title("Draw a rectangle/square")
 
#Get user input for color
selectedColor = input("What color would you like your rectangle to be ? ")
t.color(selectedColor)
 
#Get user input for top & bottom
top_bottom = int(input("How big is the top and bottom of your rectangle? "))
t.forward(top_bottom)
t.right(90)

#Get user input for sides
sides = int(input("How big are the sides of your rectangle? "))
t.forward(sides)

#Other side
t.right(90)
t.forward(top_bottom)

#Other bottom
t.right(90)
t.forward(sides)
