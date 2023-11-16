from turtle import Turtle, Screen

# Creare un oggetto Screen
screen = Screen()

# Creare un oggetto Turtle
sam_turtle = Turtle()

# Aggiungere del codice per disegnare qualcosa, ad esempio un quadrato
for _ in range(4):
    sam_turtle.forward(100)
    sam_turtle.left(90)

# Chiudere la finestra facendo clic su di essa
screen.exitonclick()
