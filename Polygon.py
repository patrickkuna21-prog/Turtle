import turtle
turtle.Screen().bgcolor("orange")
turtle.Screen().setup(300,400)
polygon=turtle.Turtle()
number_sides=6
sides_lenght=70
angles=360/number_sides
for i in range(number_sides):
    polygon.forward(sides_lenght)
    polygon.right(angles)
turtle.done()