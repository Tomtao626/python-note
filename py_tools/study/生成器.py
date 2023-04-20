def fib(max):
    n,a,b = 0,0,1
    while n< max:
        # print(b)
        yield b
        a,b = b,a+b
        n = n + 1
    return 'done'

f = (fib(10))
while True:
    try:
        n = next(f)
        print('f:',n)
    except Exception as e:
        print("error")
        break
# print(f.__next__())
# print(f.__next__())
# print("------------")
# print(f.__next__())
# print(f.__next__())
# print(f.__next__())
# print(f.__next__())
# print(f.__next__())
# print("ytutyuy-------hfgjfj")
# print(f.__next__())
# print(f.__next__())
# print(f.__next__())
# print(f.__next__())# next次数超出所制定次数  必须抛出异常并抓取

# for i in f:
#     print(i)
