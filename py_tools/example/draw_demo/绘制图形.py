import turtle
turtle.screensize(1024,768) #屏幕大小设定
turtle.color("red")
turtle.write("hello天朝",font = ("华文琥珀",80,"normal")) #设定字体大小
turtle.showturtle()
##########################
turtle.begin_fill()
turtle.circle(100,steps = 5) #图形的边长控制图形
turtle.color("green")
turtle.end_fill()
turtle.reset()
##############################
turtle.pensize(30)
turtle.begin_fill()
turtle.circle(100,steps = 6) #图形的边长控制图形
turtle.color("yellow")
turtle.end_fill()
turtle.hideturtle()

turtle.done()