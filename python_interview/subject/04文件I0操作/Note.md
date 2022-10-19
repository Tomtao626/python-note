# Python 中 read 、readline 和 readlines 的区别？
### read()
    read 表示一次性将文件的所有内容都读取到内存之中，如果文件占用空间很大，一次性读取出出现内存不足的问题。
    针对文件过大，内存不足的问题，我们可以使用，read(size) 一次最多读取多少的 size 字节，读取大文件时候可以多次调用该方法。
### readline()
    每次只读取一行的内容，如果是文本文件，建议使用该方法，一次读取一行，逐行读取。
### readlines()
    和 read() 方法一样，也是一次读取所有的内容，但是返回结果不同，
    该方法是按行读取后返回的一个列表，可以使用for循环取出列表中每个元素，一个元素就代表一行。

# 大文件只需读取部分内容，或者避免读取时候内存不足的解决方法？
    方法1：直接for循环迭代文件，避免内存不足，但是使用 with 打开文件后会自动关闭，需要再次打开。
```python
with open("filtest.txt", 'r') as f:
    for line in f:
        print(line)
```
    方法2：迭代器切片操作，使用 islice。
    islice返回一个生成器函数，进行切片操作，取出索引为101到105的值
```python
from itertools import islice
with open("filtest.txt", 'r') as f:
    for line in islice(f, 101, 105):
        print(line)
    for line in islice(f, 5): #只给一个参数，指定的是结束的位置
        print(line)
```

# 什么是上下文？with 上下文管理器原理？
    1.上下文(context)，个人理解其实就是字面意思，在不同的场景下有不同的意思，也可以理解为和文章中的上下文是一个意思，在通俗一点，我觉得叫环境更好。
      ....林冲大叫一声“啊也！”....
      问:这句话林冲的“啊也”表达了林冲怎样的心里？
      答:啊你妈个头啊！
      看，一篇文章，给你摘录一段，没前没后，你读不懂，因为有语境，就是语言环境存在，一段话说了什么，要通过上下文(文章的上下文)来推断。
    2.子程序之于程序，进程之于操作系统，甚至app的一屏之于app，都是一个道理。程序执行了部分到达子程序，子程序要获得结果，要用到程序之前的一些结果(包括但不限于外部变量值，外部对象等等)；
      app点击一个按钮进入一个新的界面，也要保存你是在哪个屏幕跳过来的等等信息，以便你点击返回的时候能正确跳回，如果不存肯定就无法正确跳回了。
      看这些都是上下文的典型例子，理解成环境就可以，(而且上下文虽然叫上下文，但是程序里面一般都只有上文而已，只是叫的好听叫上下文。。
      进程中断在操作系统中是有上有下的，不过不给题主说了，免得产生新的问题)
    3.上下文虽然叫上下文，但是程序里面一般都只有上文而已，只是为了叫的好听叫上下文。
      进程中断在操作系统中是有上有下的，不过不这个高深的问题就不要深究了
      任何实现了 __enter__() 和 __exit__() 方法的对象都可以称之为上下文管理器，上下文管理器对象可以使用with关键字。
      显然，文件（file）对象也实现了上下文管理器。
    4.那么文件对象是如何实现这两个方法的呢？我们可以模拟实现一个自己的文件类，让该类实现 __enter__() 和 __exit__() 方法。
```python
# 文件管理器
class File():

    # 初始化方法
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    # 打开文件的方法，返回我们打开的对象，也就是传入的文件
    def __enter__(self):
        print("entering")
        self.f = open(self.filename, self.mode)
        return self.f

    # 关闭文件的方法，不用我们自己手动去关闭文件对象了
    def __exit__(self, *args):
        print("will exit")
        self.f.close()

with File('filetest.txt', 'w') as f:
    print("writing")
    f.write('hello, world')
```

# 什么是全缓冲、行缓冲和无缓冲？
    全缓冲：python默认的缓冲区是4096字节，当缓冲区内的空间占满后，就将数据写入到磁盘中；
    行缓冲：当写入的数据，每当遇到换行符，就将缓冲区中的数据写入到磁盘中；
    无缓冲：字面意思，一写入数据，就将数据写入到磁盘中；
    三种缓冲都可以通过buffering参数来设置
```python
# 全缓冲：python默认的缓冲区是4096字节，当缓冲区内的空间占满后，就将数据写入到磁盘中；
f = open("filetest.txt", 'w', buffering=2048)
#写入三个字节abc 打开txt文件依旧是空的
f.write('abc')
#写入2045个字节 打开txt文件依旧是空的
f.write('*'*2045)
# 此时我们在写入一个字节，就由缓冲存储到磁盘了，此时打开txt文件就可以看见数据了
# 行缓冲： buffering=1
f = open('001_测试缓冲案例文件.txt', 'w', buffering=1)
f.write('abc')
# 只要遇到换行符，就将缓存存到磁盘
f.write('\n')

# 无缓冲：buffering=0
# 写入数据就直接存储到磁盘
```

# 什么是序列化和反序列化？JSON 序列化时常用的四个函数是什么？
    序列化:我们程序中的变量和对象（比如文字、图片等内容），在传输的时候需要使用二进制数据，将这些变量或对象转换为二进制数据的过程，就是序列化。
    反序列化:反序列化就是序列化的逆过程，把获取的二进制数据重建为变量或对象。实际序列化和反序列化就是二进制数据和原始数据格式之间的一个转换过程。

    json常用的四个函数:
        json.dump:将数据序列化到文件
        json.load:将文件中的内容反序列化读取出来
        json.dumps:将python格式的数据转换为json的字符串格式(序列化)
        json.loads:将json的字符串格式转换为python支持的数据格式(反序列化)
    注意：标准 JSON 格式数据要使用双引号。

# JSON 中 dumps 转换数据时候如何保持中文编码？
    可以通过 json.dumps 的 ensure_ascii 参数解决，代码示例如下：
```python
# file = open('papers.json', 'w', encoding='utf-8')
# 将item字典类型的数据转换成json格式的字符串,
# 注意json.dumps序列化时对中文默认使用的ascii编码，要想写入中文，加上ensure_ascii=False
# line = json.dumps(dict(item), ensure_ascii=False) + "\n"
# file.write(line)

import json
a=json.dumps({"python":"你好"},ensure_ascii=False)
print(a)

# {"python"："你好"}
```