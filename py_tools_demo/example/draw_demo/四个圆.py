# /usr/bin/env python
# -*- coding=UTF-8 -*-

import turtle
#第一个
turtle.penup()
turtle.forward(100)
turtle.color("red")
turtle.pendown()
turtle.circle(70)
#第二个
turtle.penup()
turtle.goto(-40,0)
turtle.color("green")
turtle.pendown()
turtle.circle(70)

turtle.penup()
turtle.goto(-40,-150)
turtle.color("blue")
turtle.right(90)
turtle.pendown()
turtle.circle(70)
turtle.done()