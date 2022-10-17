# /usr/bin/env python
# -*- coding=UTF-8 -*-

import turtle

turtle.color("red")
turtle.penup()
turtle.goto(0,0)
turtle.pendown()
turtle.circle(100)

turtle.color("green")
turtle.penup()
turtle.goto(0,200)
turtle.write("24点")
turtle.goto(100,100)
turtle.write('3点')
turtle.goto(0,0)
turtle.write("6点")
turtle.goto(-100,100)
turtle.write('9点')

turtle.color("blue")
turtle.penup()
turtle.goto(0,180)
turtle.pendown()
turtle.goto(0,100)
turtle.goto(80,100)

turtle.done()