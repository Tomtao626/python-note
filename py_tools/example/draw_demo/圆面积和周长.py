import turtle

R = eval(input("请输入半径："))

turtle.circle(R)
turtle.penup()
turtle.goto(0,R)
turtle.pendown()
turtle.write("("("0，"+str(R)+")"))
turtle.done()