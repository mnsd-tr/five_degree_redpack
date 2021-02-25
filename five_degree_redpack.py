import json
import os
import turtle
from time import sleep


def print_map(i1, j1, i2, j2):
    for i in range(5):
        for j in range(5):
            if i == i1 - 1 and j == j1 - 1:
                print("\033[1;32m", end="")
            elif i == i2 - 1 and j == j2 - 1:
                print("\033[1;31m", end="")
            else:
                print("\033[0;37m", end="")
            print("*\033[0;37m", end=" ")
        print()


with open("./xy_position.txt", "r") as f:
    xy_position = f.read()
t = turtle.Turtle()
t.pensize(3)
t.speed(20)
t.hideturtle()

for i in range(5):
    for j in range(5):
        t.penup()
        t.goto((i+1)*50, (j+1)*(-50))
        t.pendown()
        t.circle(1)

conf = 0
try:
    set_speed = int(input("请输入展示速度，不输入则一步一停："))
    t.speed(set_speed)
except:
    t.speed(2)
    conf = 1

t.penup()
xy_position = json.loads(xy_position)
for xy in xy_position:
    y1 = xy["x1"]//150+1
    x1 = xy["y1"]//150+1
    y2 = xy["x2"]//150+1
    x2 = xy["y2"]//150+1

    # os.system("cls")
    # print_map(x1, y1, x2, y2)
    # print(f"x{x1},y{y1} => x{x2},y{y2}")
    sleep(0.1)
    t.goto(y1 * 50, x1 * (-50))
    t.pendown()
    t.goto(y2 * 50, x2 * (-50))
    if conf:
        input()
sleep(5)
