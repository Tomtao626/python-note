---
layout: mypost
title: 08-asyncio
categories: [Python]
---

## 多线程的缺点

- 运行过程容易被打断，有可能出现race condition的情况
- 线程切换本身存在一定的损耗，线程数不可能无限增加，因此，如果你的 I/O 操作非常 heavy，多线程很有可能满足不了高效率、高质量的需求。

## 同步-sync

- 一个接一个的执行，下一个操作必须等待上一个操作完成后才能执行

## 异步-async

- 不同操作间，可以相互交替执行，如果其中的某个操作被block了，程序并不会等待，而是会找出可执行的操作继续执行

> 举个简单的例子，你的老板让你做一份这个季度的报表，并且邮件发给他。
> + 如果按照 Sync 的方式，你会先向软件输入这个季度的各项数据，接下来等待 5min，等报表明细生成后，再写邮件发给他。
> + 但如果按照 Async 的方式，再你输完这个季度的各项数据后，便会开始写邮件。等报表明细生成后，你会暂停邮件，先去查看报表，确认后继续写邮件直到发送完毕。

## asyncio

### 原理

> 事实上，Asyncio 和其他 Python 程序一样，是单线程的，它只有一个主线程，但是可以进行多个不同的任务（task），这里的任务，就是特殊的 future 对象。这些不同的任务，被一个叫做 event loop 的对象所控制。你可以把这里的任务，类比成多线程版本里的多个线程。
> + 为了简化讲解这个问题，我们可以假设任务只有两个状态：一是预备状态；二是等待状态。
> + 所谓的预备状态，是指任务目前空闲，但随时待命准备运行。
> + 而等待状态，是指任务已经运行，但正在等待外部的操作完成，比如 I/O 操作。
> + 在这种情况下，event loop 会维护两个任务列表，分别对应这两种状态；并且选取预备状态的一个任务（具体选取哪个任务，和其等待的时间长短、占用的资源等等相关），使其运行，一直到这个任务把控制权交还给 event loop 为止。
> + 当任务把控制权交还给 event loop 时，event loop 会根据其是否完成，把任务放到预备或等待状态的列表，然后遍历等待状态列表的任务，查看他们是否完成。
>   + 如果完成，则将其放到预备状态的列表；
>   + 如果未完成，则继续放在等待状态的列表。而原先在预备状态列表的任务位置仍旧不变，因为它们还未运行。
> + 这样，当所有任务被重新放置在合适的列表后，新一轮的循环又开始了：event loop 继续从预备状态的列表中选取一个任务使其执行…如此周而复始，直到所有任务完成。
> + 值得一提的是，对于 Asyncio 来说，它的任务在运行时不会被外部的一些因素打断，因此 Asyncio 内的操作不会出现 race condition 的情况，这样你就不需要担心线程安全的问题了。

### 用法

```python

import asyncio
import aiohttp
import time

async def download_one(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            print('Read {} from {}'.format(resp.content_length, url))

async def download_all(sites):
    tasks = [asyncio.create_task(download_one(site)) for site in sites]
    await asyncio.gather(*tasks)

def main():
    sites = [
        'https://en.wikipedia.org/wiki/Portal:Arts',
        'https://en.wikipedia.org/wiki/Portal:History',
        'https://en.wikipedia.org/wiki/Portal:Society',
        'https://en.wikipedia.org/wiki/Portal:Biography',
        'https://en.wikipedia.org/wiki/Portal:Mathematics',
        'https://en.wikipedia.org/wiki/Portal:Technology',
        'https://en.wikipedia.org/wiki/Portal:Geography',
        'https://en.wikipedia.org/wiki/Portal:Science',
        'https://en.wikipedia.org/wiki/Computer_science',
        'https://en.wikipedia.org/wiki/Python_(programming_language)',
        'https://en.wikipedia.org/wiki/Java_(programming_language)',
        'https://en.wikipedia.org/wiki/PHP',
        'https://en.wikipedia.org/wiki/Node.js',
        'https://en.wikipedia.org/wiki/The_C_Programming_Language',
        'https://en.wikipedia.org/wiki/Go_(programming_language)'
    ]
    start_time = time.perf_counter()
    asyncio.run(download_all(sites))
    end_time = time.perf_counter()
    print('Download {} sites in {} seconds'.format(len(sites), end_time - start_time))
    
if __name__ == '__main__':
    main()

## 输出
Read 63153 from https://en.wikipedia.org/wiki/Java_(programming_language)
Read 31461 from https://en.wikipedia.org/wiki/Portal:Society
Read 23965 from https://en.wikipedia.org/wiki/Portal:Biography
Read 36312 from https://en.wikipedia.org/wiki/Portal:History
Read 25203 from https://en.wikipedia.org/wiki/Portal:Arts
Read 15160 from https://en.wikipedia.org/wiki/The_C_Programming_Language
Read 28749 from https://en.wikipedia.org/wiki/Portal:Mathematics
Read 29587 from https://en.wikipedia.org/wiki/Portal:Technology
Read 79318 from https://en.wikipedia.org/wiki/PHP
Read 30298 from https://en.wikipedia.org/wiki/Portal:Geography
Read 73914 from https://en.wikipedia.org/wiki/Python_(programming_language)
Read 62218 from https://en.wikipedia.org/wiki/Go_(programming_language)
Read 22318 from https://en.wikipedia.org/wiki/Portal:Science
Read 36800 from https://en.wikipedia.org/wiki/Node.js
Read 67028 from https://en.wikipedia.org/wiki/Computer_science
Download 15 sites in 0.062144195078872144 seconds

# Async 和 await 关键字是 Asyncio 的最新写法，表示这个语句 / 函数是 non-block 的，正好对应前面所讲的 event loop 的概念。如果任务执行的过程需要等待，则将其放入等待状态的列表中，然后继续执行预备状态列表里的任务。
# 主函数里的 asyncio.run(coro) 是 Asyncio 的 root call，表示拿到 event loop，运行输入的 coro，直到它结束，最后关闭这个 event loop。
# 事实上，asyncio.run() 是 Python3.7+ 才引入的，相当于老版本的以下语句：

loop = asyncio.get_event_loop()
try:
    loop.run_until_complete(coro)
finally:
    loop.close()

# 至于 Asyncio 版本的函数 download_all()，和之前多线程版本有很大的区别：
tasks = [asyncio.create_task(download_one(site)) for site in sites]
await asyncio.gather(*task)

# asyncio.create_task(coro)，表示对输入的协程 coro 创建一个任务，安排它的执行，并返回此任务对象。这个函数也是 Python 3.7+ 新增的，如果是之前的版本，你可以用asyncio.ensure_future(coro)等效替代。
# 可以看到，这里我们对每一个网站的下载，都创建了一个对应的任务。再往下看，asyncio.gather(*aws, loop=None, return_exception=False)，则表示在 event loop 中运行aws序列的所有任务
```

- 如果你需要 await 一系列的操作，就得使用 asyncio.gather()；
- 如果只是单个的 future，或许只用 asyncio.wait() 就可以了。那么，对于你的 future，你是想要让它 run_until_complete() 还是 run_forever() 呢？诸如此类，都是你在面对具体问题时需要考虑的。

### 多线程和Asyncio 怎么选

```python

if io_bound:
    if io_slow:
        print('Use Asyncio')
    else:
        print('Use multi-threading')
else if cpu_bound:
    print('Use multi-processing')
```

- 如果是 I/O bound，并且 I/O 操作很慢，需要很多任务 / 线程协同实现，那么使用 Asyncio 更合适。
- 如果是 I/O bound，但是 I/O 操作很快，只需要有限数量的任务 / 线程，那么使用多线程就可以了。
- 如果是 CPU bound，则需要使用多进程来提高程序运行效率。

## Note

- 不同于多线程，Asyncio 是单线程的，但其内部 event loop 的机制，可以让它并发地运行多个不同的任务，并且比多线程享有更大的自主控制权。
- Asyncio 中的任务，在运行过程中不会被打断，因此不会出现 race condition 的情况。尤其是在 I/O 操作 heavy 的场景下，Asyncio 比多线程的运行效率更高。
- 因为 Asyncio 内部任务切换的损耗，远比线程切换的损耗要小；并且 Asyncio 可以开启的任务数量，也比多线程中的线程数量多得多。
- 但需要注意的是，很多情况下，使用 Asyncio 需要特定第三方库的支持，比如前面示例中的 aiohttp。
- 而如果 I/O 操作很快，并不 heavy，那么运用多线程，也能很有效地解决问题。

```python
# 输入一个列表，对于列表中的每个元素，我想计算 0 到这个元素的所有整数的平方和。

# 单进程版本
import time
def cpu_bound(number):
    print(sum(i * i for i in range(number)))

def calculate_sums(numbers):
    for number in numbers:
        cpu_bound(number)

def main():
    start_time = time.perf_counter()  
    numbers = [10000000 + x for x in range(20)]
    calculate_sums(numbers)
    end_time = time.perf_counter()
    print('Calculation takes {} seconds'.format(end_time - start_time))
    
if __name__ == '__main__':
    main()

# 多线程版本
import multiprocessing
import time


def cpu_bound(number):
    return sum(i * i for i in range(number))


def find_sums(numbers):
    with multiprocessing.Pool() as pool:
        pool.map(cpu_bound, numbers)


if __name__ == "__main__":
    numbers = [10000000 + x for x in range(20)]

    start_time = time.time()
    find_sums(numbers)
    duration = time.time() - start_time
    print(f"Duration {duration} seconds")
```

- Python的协程，大概搞明白了其中原理，这里的“阻塞“与“异步“是一个更高层次的抽象概念，并非指系统调用级别的。
- 我为什么强调“阻塞”，“异步”这些概念，如果你读过unp那本书，要理解unix的io模型这些是避不开的概念。
- 网上大部分的文章引用了unp的内容来介绍阻塞，非阻塞，同步，异步的概念，紧接着便介绍asyncio包的使用，其实asyncio里阻塞和异步的概念并不完全等同于unp中介绍的系统调用io，是在一个更好的抽象层次上，一个asyncio的协程依然可能遇到底层同步的io调用，此时这个协程就是会阻塞住整个当前线程，使得线程失去CPU，从而影响到其它的协程。
- 其实你理解的也没错，只是高层抽象的解释，但前提是你要清楚你此时说的阻塞是什么意思，它不是指系统调用级别，而是任务级别的某些条件不能满足的情况，而这些不能满足的条件可能是其它协程的CPU操作，而不是io操作。
- 因为你要清楚一个事实:目前Linux下对异步io的支持是有限的，它只实现了磁盘的异步io，网络io仍然是同步的，也就是说在Linux上异步io使用场景很少很少，业界几乎只拿它当个概念来讲。
- 因此我觉得Python的这个asyncio包名是一个很糟糕的命名，特别是对于理解一点点底层原理的人来说。它的协程真的很难理解也很难使用，如果你用过go的goroutine你就明白我为什么如此吐槽Python的协程了。
- 虽然它避免了线程切换带来的成本，避免了并发时的静态条件，但go的线程模型某种程度上讲也避免了goroutine的切换开销，仅仅需要在并发时照顾好竞态条件，但go带来的简单易用性是Python的协程望尘莫及的，所以现阶段我是不会使用Python的协程的。