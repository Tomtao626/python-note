# from module_01 import logger as logger_01
# import module_01

# from module_01 import name,logger
# def logger():  # logger ----- >.>> 'print'
#     print("in the main")
import sys,os
print(sys.path)

x = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(x)
import module_01

say_hello()
'''
module_01 = all_code
name = 'tom_tao'
def say_hello():
    print("hello tom_tao")

def logger():  # logger ----->>> ‘pass’
    pass

def reunning():
    pass
'''
print(name)
logger()
# module_01.logger()
# logger()
# logger_01()
# print(module_01.name)
# module_01.say_hello()