# today we make a flower using turtle graphics
import turtle
import colorsys

# know  we make a function to draw a flower
def flower():
    screen = turtle.Screen()
    screen.bgcolor("black")
    flower = turtle.Turtle()
    flower.speed(100)  # Set the speed of the turtle
    flower.width(2)
    flower.hideturtle()
    n_petals = 180
    n_colors = 100
    radius = 300
    hue = 0
    for i in range(n_petals):
        color = colorsys.hsv_to_rgb(hue, 1, 1)
        flower.color(color)
        flower.circle(radius, 60)  # Draw a curve (part of a circle)
        flower.left(120)
        flower.circle(radius, 60)
        flower.left(120)
        flower.circle(radius, 60)
        flower.left(120 + 360 / n_petals)
        hue += 1 / n_colors
    turtle.done()
 # now we call the function to draw a flower
if __name__ == "__main__":
    flower()
# now we make a function to draw a flower
