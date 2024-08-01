from turtle import *
from random import randint
from time import time, sleep

def catch(x,y):
    ran = randint(40,180)
    t1.left(ran)

def catch1(x,y):
    ran = randint(40,180)
    t2.left(ran)

def catch2(x,y):
    ran = randint(40,180)
    t3.left(ran)

def game_over():
    if abs(t1.xcor()) > MAX_X or abs(t1.ycor()) > MAX_Y:
        return False
    if abs(t2.xcor()) > MAX_X or abs(t2.ycor()) > MAX_Y:
        return False
    if abs(t3.xcor()) > MAX_X or abs(t3.ycor()) > MAX_Y:
        return False
    return True
    

MAX_X = 300
MAX_Y = 300

t1 = Turtle()
t2 = Turtle()
t3 = Turtle()

t1.color("grey")
t1.shape("turtle")
t1.pensize(11)
t1.onclick(catch)

t2.color("lime")
t2.shape("turtle")
t2.pensize(11)
t2.left(120)
t2.onclick(catch1)

t3.color("crimson")
t3.shape("turtle")
t3.pensize(11)
t3.left(240)
t3.onclick(catch2)

t1.penup()
t1.goto(-MAX_X,-MAX_Y)
t1.pendown()
for i in range(4):
    t1.forward(MAX_X*2)
    t1.left(90)
t1.penup()
t1.goto(0,0)
t1.pendown()

all_time = time()
return_time = 0
while return_time <= 10 and game_over() != False:
    sleep(0.2)
    t1.forward(30)
    t2.forward(30)
    t3.forward(30)
    return_time = time() - all_time

if game_over() == False:
    t1.write("Ты проиграл", font=("SegoeUI",25, "normal"))
else:
    t1.write("Ты выиграл", font=("SegoeUI",25, "normal"))
done()