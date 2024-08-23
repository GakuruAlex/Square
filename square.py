from turtle import Turtle, Screen

def move_and_turn_right(turtle):
    for _ in range (4):
        turtle.forward(120)
        turtle.right(90)
def square():
    my_turtle = Turtle()
    my_turtle.shape("turtle")
    my_turtle.color("blue")


    move_and_turn_right(my_turtle)

    screen = Screen()
    screen.exitonclick()

if __name__ == "__main__":
    square()