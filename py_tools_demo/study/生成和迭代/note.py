#环境准备
#三方模块：itchat
#安装 pip install itchat
#图灵机器人
#快速打造聊天机器人

#/////////////////
import turtle
min = eval(input("请输入你的时间（分）："))
day = min//(60*24)
year = day//365
day = day//365
min = min//(60*24)
print(year,'年',day,"天",min,"分钟")
turstr = str(year)+"年"+str(day)+"天"+str(min)+"分钟"
turtle.color("red")
turtle.circle(200)
turtle.write(turstr)
turtle.done()
