import time

def times(func):
    def warpper(*args,**kwargs):
        start_time = time.time()
        func()
        end_time = time.time()
        print('the func run time is %s' % (end_time-start_time))
    return warpper








def test1():
    time.sleep(3)
    print('in the test1')
# 沉睡3秒 打印


test1()