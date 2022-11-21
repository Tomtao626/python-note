---
layout: mypost
title: 09-GIL
categories: [Python]
---

```python
def CountDown(n):
    while n > 0:
        n -= 1
%time CountDown(100000000)
# CPU times: user 4.18 s, sys: 9.08 ms, total: 4.19 s
# Wall time: 4.2 s

# cpu-bound 代码

# 多线程

from threading import Thread

n = 100000000

t1 = Thread(target=CountDown, args=[n // 2])
t2 = Thread(target=CountDown, args=[n // 2])
t1.start()
t2.start()
t1.join()
t2.join()

# CPU times: user 4.12 s, sys: 11.7 ms, total: 4.13 s
# Wall time: 4.15 s

# 两个版本对比消耗时间 没有太大差别，如果在一台单核的电脑上运行，单线程运行需要 11s 时间，2 个线程运行也是 11s 时间。虽然不像第一台机器那样，多线程反而比单线程更慢，但是这两次整体效果几乎一样，看起来，这不像是电脑的问题，而是 Python 的线程失效了，没有起到并行计算的作用。
# Python 的线程是不是假的线程？Python 的线程，的的确确封装了底层的操作系统线程，在 Linux 系统里是 Pthread（全称为 POSIX Thread），而在 Windows 系统里是 Windows Thread。另外，Python 的线程，也完全受操作系统管理，比如协调何时执行、管理内存资源、管理中断等等。
# 所以，虽然 Python 的线程和 C++ 的线程本质上是不同的抽象，但它们的底层并没有什么不同。
```

## GIL

### 什么是GIL

- Python解释器CPython中的一个技术术语，全局解释器锁，本质上是类似于操作系统的Mutex，每一个Python线程，在Python解释器中执行时，都会先锁住自己的线程，阻止别的线程运行
- CPython 会做一些小把戏，轮流执行 Python 线程。这样一来，用户看到的就是“伪并行”——Python 线程在交错执行，来模拟真正并行的线程。
- CPython使用引用计数来管理内存，所有的Python程序中创建的实例，都会有一个引用计数，记录有多少个指针指向它，当引用计数只有0时，则会自动释放内存。
  - 一是设计者为了规避类似于内存管理这样的复杂的竞争风险问题（race condition）；
  - 二是因为 CPython 大量使用 C 语言库，但大部分 C 语言库都不是原生线程安全的（线程安全会降低性能和增加复杂度）。

```python
import sys

a = []
b = a
print(sys.getrefcount(a)) # 3

# a的引用计数是3，因为有a和b，以及作为参数传递getrefcount这三个地方，都引用了一个空列表
# 当有两个Python线程同时引用了a，会造成引用计数的race condition，引用计数可能最终只加1，这样就会造成内存污染，当第一个线程访问a结束后，会把引用计数-1，直接释放a的内存，当第二个线程再访问a时，就找不到有效的内存了
```

### 原理

- GIL在Python程序中工作实例，三个线程Thread1/2/3轮流执行，每一个线程开始执行时，都会给GIL加锁，以阻止别的线程运行；同样的，每一个线程执行完一段后，会释放 GIL，以允许别的线程开始利用资源。

![gil-01.png](/py_core/assets/02-advance/09/gil-01.png)

- CPython 中还有另一个机制，叫做 check_interval，意思是 CPython 解释器会去轮询检查线程 GIL 的锁住情况。每隔一段时间，Python 解释器就会强制当前线程去释放 GIL，这样别的线程才能有执行的机会。
- 不同版本的 Python 中，check interval 的实现方式并不一样。早期的 Python 是 100 个 ticks，大致对应了 1000 个 bytecodes；而 Python 3 以后，interval 是 15 毫秒。
- 当然，我们不必细究具体多久会强制释放 GIL，这不应该成为我们程序设计的依赖条件，我们只需明白，CPython 解释器会在一个“合理”的时间范围内释放 GIL 就可以了

![gil-02.png](/py_core/assets/02-advance/09/gil-02.png)

- 整体来说，每一个 Python 线程都是类似这样循环的封装，我们来看下面这段代码：

```c++
for (;;) {
    if (--ticker < 0) {
        ticker = check_interval;
    
        /* Give another thread a chance */
        PyThread_release_lock(interpreter_lock);
    
        /* Other threads may run now */
    
        PyThread_acquire_lock(interpreter_lock, 1);
    }

    bytecode = *next_instr++;
    switch (bytecode) {
        /* execute the next instruction ... */ 
    }
}

// 每个Python线程都会先检查ticker计数，只有在ticker大于0的情况下，线程才会去执行自己的bytecode
```

### Python线程安全

- 有了 GIL，并不意味着我们 Python 编程者就不用去考虑线程安全了。即使我们知道，GIL 仅允许一个 Python 线程执行，但前面我也讲到了，Python 还有 check interval 这样的抢占机制。我们来考虑这样一段代码：

```python
import threading

n = 0

def foo():
    global n
    n += 1

threads = []
for i in range(100):
    t = threading.Thread(target=foo)
    threads.append(t)

for t in threads:
    t.start()

for t in threads:
    t.join()

print(n) # 100
```

- 如果你执行的话，就会发现，尽管大部分时候它能够打印 100，但有时侯也会打印 99 或者 98。
- 这其实就是因为，n+=1这一句代码让线程并不安全。如果你去翻译 foo 这个函数的 字节码，就会发现，它实际上由下面四行 bytecode 组成：

```python
# 获取程序的字节码
import dis
dis.dis(foo)
 # 7            0 LOAD_GLOBAL              0 (n)
 #              2 LOAD_CONST               1 (1)
 #              4 INPLACE_ADD
 #              6 STORE_GLOBAL             0 (n)
 #              8 LOAD_CONST               0 (None)
 #             10 RETURN_VALUE
# 存在被打断的可能

# GIL 的设计，主要是为了方便 CPython 解释器层面的编写者，而不是 Python 应用层面的程序员。作为 Python 的使用者，我们还是需要 lock 等工具，来确保线程安全。

n = 0
lock = threading.Lock()

def foo():
    global n
    with lock:
        n += 1
```

### 绕过GIL

- 绕过 CPython，使用 JPython（Java 实现的 Python 解释器）等别的实现；
- 把关键性能代码，放到别的语言（一般是 C++）中实现。

## Note

- cpu-bound任务的多线程相比单线程，时间的增加在于锁添加的获取和释放的开销结果。
- GIL相对来说是合理而且有效率的，它易于实现，很容易就添加到python中，而且它为单线程程序提供了性能提升。

