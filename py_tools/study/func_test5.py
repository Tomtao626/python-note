# -*- coding:utf-8 -*-
# Ayuthor:Tom_Tao

'''
def  test(*args): #默认参数可有可无  *args：接受N个位置参数，转换成元祖形式
    print(args)
test(1,2,3,5,56,7)#针对多个实参，可以*开头定义，可传多个值

test(*[1,2,3,4,5]) #args = tuple（[1,2,3,4,5]）  元组

def test1(x,*args):
    print(x)
    print(args)

test1(1,2,3,4,5,6,7,8)#位置传参数
'''
'''
def test2(**kwargs):  # **kwargs  把N个关键字参数，转换成字典的格式
    print(kwargs)
    #读取字典
    print(kwargs['name'])
    print(kwargs['age'])
    print(kwargs['sex'])

test2(name='Tom',age='23',sex='M')  #dict:   key:value 键值对
test2(**{'name':'tom','age':'23','sex':'M'})

def test3(name,**kwargs):
    print(name)
    print(kwargs)

test3('tom',age =18,sex = 'm')

def test4(name,age =18,**kwargs):#**kwargs 1接受剩余参数
    print(name)
    print(age)
    print(kwargs)

test4('tom',sex='m',hobby='tesla')
test4('tom',4,hobby='tesla')
#给默认参数赋值两种方式：1.直接给值  2.匹配关键字'''

def test4(name,age =18,*args,**kwargs):#**kwargs 1接受剩余参数
    print(name)
    print(age)
    print(args)
    print(kwargs)
    logger("test4")
def logger(source):
    print("from %s"  %  source)
#*args接受位置参数，不能接受关键字参数，所以*args为空
test4('tom',sex='m',hobby='tesla',age=34)#位置参数不能写在关键字的后面

