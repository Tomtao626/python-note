---
layout: mypost
title: 03-assert
categories: [Python]
---

## 什么是assert

- Python 的 assert 语句，可以说是一个 debug 的好工具，主要用于测试一个条件是否满足。
  - 如果测试的条件满足，则什么也不做，相当于执行了 pass 语句；
  - 如果测试条件不满足，便会抛出异常 AssertionError，并返回具体的错误信息（optional）。
  - `assert_stmt ::=  "assert" expression ["," expression]`

```python

assert 1 == 2

# 等同于：

if __debug__:
    if not expression: raise AssertionError


assert 1 == 2,  'assertion is wrong'

# 等同于：

if __debug__:
    if not expression1: raise AssertionError(expression2)

# __debug__是一个常数。如果 Python 程序执行时附带了-O这个选项，比如Python test.py -O，那么程序中所有的 assert 语句都会失效，常数__debug__便为 False；反之__debug__则为 True。
# 不过，需要注意的是，直接对常数__debug__赋值是非法的，因为它的值在解释器开始运行时就已经决定了，中途无法改变。

# 不要在使用 assert 时加入括号

assert(1 == 2, 'This should fail')
# 输出
<ipython-input-8-2c057bd7fe24>:1: SyntaxWarning: assertion is always true, perhaps remove parentheses?
  assert(1 == 2, 'This should fail')

# 无论表达式对与错（比如这里的 1 == 2 显然是错误的），assert 检查永远不会 fail，程序只会给你 SyntaxWarning。
# 正确的写法，应该是下面这种不带括号的写法：
assert 1 == 2, 'This should fail'
# 输出
AssertionError: This should fail
```

- 总的来说，assert 在程序中的作用，是对代码做一些 internal 的 self-check。使用 assert，就表示你很确定。这个条件一定会发生或者一定不会发生。
- 举个例子，比如你有一个函数，其中一个参数是人的性别，因为性别只有男女之分（这里只指生理性别），你便可以使用 assert，以防止程序的非法输入。
- 如果你的程序没有 bug，那么 assert 永远不会抛出异常；而它一旦抛出了异常，你就知道程序存在问题了，并且可以根据错误信息，很容易定位出错误的源头。

## assert用法

- 写一个 apply_discount() 函数，要求输入为原来的价格和折扣，输出是折后的价格

```python

def apply_discount(price, discount):
    updated_price = price * (1 - discount)
    assert 0 <= updated_price <= price, 'price should be greater or equal to 0 and less or equal to original price'
    return updated_price

# 在计算新价格的后面，我们还写了一个 assert 语句，用来检查折后价格，这个值必须大于等于 0、小于等于原来的价格，否则就抛出异常。
# 
apply_discount(100, 0.2)
80.0

apply_discount(100, 2)
AssertionError: price should be greater or equal to 0 and less or equal to original price

# 显然，当 discount 是 0.2 时，输出 80，没有问题。但是当 discount 为 2 时，程序便抛出下面这个异常：

AssertionError：price should be greater or equal to 0 and less or equal to original price

# 如果开发人员修改相关的代码，或者是加入新的功能，导致 discount 数值的异常时，我们运行测试时就可以很容易发现问题。正如我开头所说，assert 的加入，可以有效预防 bug 的发生，提高程序的健壮性。
```

- 最常见的除法操作

```python

def calculate_average_price(total_sales, num_sales):
    assert num_sales > 0, 'number of sales should be greater than 0'
    return total_sales / num_sales

# 加入了 assert 语句，规定销售数目必须大于 0，这样就可以防止后台计算那些还未开卖的专栏的价格。
```

```python

def func(input):
    assert isinstance(input, list), 'input must be type of list'
    # 下面的操作都是基于前提：input必须是list
    if len(input) == 1:
        ...
    elif len(input) == 2:
        ...
    else:
        ... 

# 函数 func() 里的所有操作，都是基于输入必须是 list 这个前提。是不是很熟悉的需求呢？那我们就很有必要在开头加一句 assert 的检查，防止程序出错。当然，我们也要根据具体情况具体分析。
# 比如上面这个例子，之所以能加 assert，是因为我们很确定输入必须是 list，不能是其他数据类型。
# 如果你的程序中，允许 input 是其他数据类型，并且对不同的数据类型都有不同的处理方式，那你就应该写成 if else 的条件语句了：


def func(input):
    if isinstance(input, list):
        ...
    else:
        ...
```

## 示例

- 很多 if 条件语句是不是都可以换成 assert 呢
  - 不可以

```python

def delete_course(user, course_id):
    assert user_is_admin(user), 'user must be admin'
    assert course_exist(course_id), 'course id must exist'
    delete(course_id)

# assert 的检查是可以被关闭的，比如在运行 Python 程序时，加入-O这个选项就会让 assert 失效。
# 因此，一旦 assert 的检查被关闭，user_is_admin() 和 course_exist() 这两个函数便不会被执行。这就会导致：任何用户都有权限删除专栏课程；并且，不管这个课程是否存在，他们都可以强行执行删除操作。

# 这显然会给程序带来巨大的安全漏洞。所以，正确的做法，是使用条件语句进行相应的检查，并合理抛出异常：

def delete_course(user, course_id):
    if not user_is_admin(user):
        raise Exception('user must be admin')
    if not course_exist(course_id):
        raise Exception('coursde id must exist')
    delete(course_id)  
```

- 打开一个文件，进行数据读取、处理等一系列操作，那么下面这样的写法，显然也是不正确的：

```python

def read_and_process(path):
    assert file_exist(path), 'file must exist'
    with open(path) as f:
      ...

# 因为 assert 的使用，表明你强行指定了文件必须存在，但事实上在很多情况下，这个假设并不成立。
# 另外，打开文件操作，也有可能触发其他的异常。所以，正确的做法是进行异常处理，用 try 和 except 来解决：

def read_and_process(path):
    try:
        with open(path) as f:
            ...
    except Exception as e:
            ...
```

- 总的来说，assert 并不适用 run-time error 的检查。

## Note

- assert 通常用来对代码进行必要的 self check，表明你很确定这种情况一定发生，或者一定不会发生。
- 使用 assert 时，一定不要加上括号，否则无论表达式对与错，assert 检查永远不会 fail。
- 程序中的 assert 语句，可以通过-O等选项被全局 disable。