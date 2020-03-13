import turtle
import winsound

window = turtle.Screen()
window.title("prueba de pong")
window.bgcolor("black")
window.setup(width=800,height=600)
window.tracer(0)

#puntuacion
puntos_d = 0
puntos_i = 0

#raqueta derecha
raqueta_d = turtle.Turtle()
raqueta_d.speed(0)
raqueta_d.shape("square")
raqueta_d.color("white")
raqueta_d.shapesize(stretch_wid=5,stretch_len=1)
raqueta_d.penup()
raqueta_d.goto(-350,0)


#raqueta izquierda
raqueta_i = turtle.Turtle()
raqueta_i.speed(0)
raqueta_i.shape("square")
raqueta_i.color("white")
raqueta_i.shapesize(stretch_wid=5,stretch_len=1)
raqueta_i.penup()
raqueta_i.goto(350,0)


#pelota
pelota = turtle.Turtle()
pelota.speed(0)
pelota.shape("square")
pelota.color("white")
pelota.penup()
pelota.goto(0,0)
#velocidad de movimiento de pelota
pelota.dx = .17
pelota.dy = -.17

#puntuacion
puntuacion = turtle.Turtle()
puntuacion.speed(0)
puntuacion.color("white")
puntuacion.penup()
puntuacion.hideturtle()
puntuacion.goto(0,260)
puntuacion.write("Jugador1 : 0     Jugador2 : 0", align="center", font=("Courrier", 20, "normal"))


#Movimiento de raqueta
def raqueta_d_arriba():
    y = raqueta_d.ycor()
    y += 30
    raqueta_d.sety(y)

def raqueta_d_abajo():
    y = raqueta_d.ycor()
    y -= 30
    raqueta_d.sety(y)

def raqueta_i_arriba():
    y = raqueta_i.ycor()
    y += 30
    raqueta_i.sety(y)

def raqueta_i_abajo():
    y = raqueta_i.ycor()
    y -= 30
    raqueta_i.sety(y)

#Movimiento de pelota


#controles de raqueta
window.listen()
window.onkeypress(raqueta_d_arriba, "w")
window.onkeypress(raqueta_d_abajo, "s")
window.onkeypress(raqueta_i_arriba, "e")
window.onkeypress(raqueta_i_abajo, "d")
#loop del juego
while True:
    window.update()

    #pelota en movimiento
    pelota.setx(pelota.xcor() + pelota.dx)
    pelota.sety(pelota.ycor() + pelota.dy)

    #colisión de bordes
    if pelota.ycor() > 290:
        pelota.sety(290)
        pelota.dy *= -1
        winsound.PlaySound("bounce", winsound.SND_FILENAME | winsound.SND_ASYNC)

    if pelota.ycor() < -290:
        pelota.sety(-290)
        pelota.dy *= -1
        winsound.PlaySound("bounce", winsound.SND_FILENAME | winsound.SND_ASYNC)
    if pelota.xcor() > 390:
        pelota.goto(0,0)
        pelota.dx *= -1
        puntos_d += 1
        puntuacion.clear()
        puntuacion.write("Jugador1 : {}     Jugador2 : {}".format(puntos_d, puntos_i), align="center", font=("Courrier", 20, "normal"))
        winsound.PlaySound("point", winsound.SND_FILENAME | winsound.SND_ASYNC)

    if pelota.xcor() < -390:
        pelota.goto(0,0)
        pelota.dx *= -1
        puntos_i += 1
        puntuacion.clear()
        puntuacion.write("Jugador1 : {}     Jugador2 : {}".format(puntos_d, puntos_i), align="center", font=("Courrier", 20, "normal"))
        winsound.PlaySound("point", winsound.SND_FILENAME | winsound.SND_ASYNC)

    #colision de raqueta
    if (pelota.xcor() > 340) and (pelota.xcor() < 350) and (pelota.ycor() < raqueta_i.ycor() + 42) and (pelota.ycor() > raqueta_i.ycor() -42):
        pelota.setx(340)
        pelota.dx *= -1
        winsound.PlaySound("hit", winsound.SND_FILENAME | winsound.SND_ASYNC)
    if (pelota.xcor() < -340) and (pelota.xcor() > -350) and (pelota.ycor() < raqueta_d.ycor() +42) and (pelota.ycor() > raqueta_d.ycor() -42):
            pelota.setx(-340)
            pelota.dx *= -1
            winsound.PlaySound("hit", winsound.SND_FILENAME | winsound.SND_ASYNC)
