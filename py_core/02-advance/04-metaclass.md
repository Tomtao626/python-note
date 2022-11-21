---
layout: mypost
title: 04-metaclass
categories: [Python]
---

## metaclass

### 通过yaml例子来说说metaclass

- 元类，超越变形特性

```python

class Monster(yaml.YAMLObject):
  yaml_tag = u'!Monster'
  def __init__(self, name, hp, ac, attacks):
    self.name = name
    self.hp = hp
    self.ac = ac
    self.attacks = attacks
  def __repr__(self):
    return "%s(name=%r, hp=%r, ac=%r, attacks=%r)" % (
       self.__class__.__name__, self.name, self.hp, self.ac,      
       self.attacks)

yaml.load("""
--- !Monster
name: Cave spider
hp: [2,6]    # 2d6
ac: 16
attacks: [BITE, HURT]
""")

Monster(name='Cave spider', hp=[2, 6], ac=16, attacks=['BITE', 'HURT'])

print(yaml.dump(Monster(
    name='Cave lizard', hp=[3,6], ac=16, attacks=['BITE','HURT'])))

# 输出
!Monster
ac: 16
attacks: [BITE, HURT]
hp: [3, 6]
name: Cave lizard
```

- 调用统一的 yaml.load()，就能把任意一个 yaml 序列载入成一个 Python Object；
- 而调用统一的 yaml.dump()，就能把一个 YAMLObject 子类序列化。
- 对于 load() 和 dump() 的使用者来说，他们完全不需要提前知道任何类型信息，这让超动态配置编程成了可能。
- 只要简单地继承 yaml.YAMLObject，就能让你的 Python Object 具有序列化和逆序列化能力。是不是相比普通 Python 类，有一点“变态”，有一点“超越”？

### 怎么用metaclass

```python
# 比如上面的yaml.load功能，简单来说，只需要一个全局的注册器，让 YAML 知道，序列化文本中的 !Monster 需要载入成 Monster 这个 Python 类型。
# 一个很自然的想法就是，那我们建立一个全局变量叫 registry，把所有需要逆序列化的 YAMLObject，都注册进去。比如下面这样：
registry = {}

def add_constructor(target_class):
    registry[target_class.yaml_tag] = target_class

# 然后，在 Monster 类定义后面加上下面这行代码：

add_constructor(Monster)

# 但这样的缺点也很明显，对于 YAML 的使用者来说，每一个 YAML 的可逆序列化的类 Foo 定义后，都需要加上一句话，add_constructor(Foo)。这无疑给开发者增加了麻烦，也更容易出错，毕竟开发者很容易忘了这一点。
# metaclass就可以解决这个问题


# Python 2/3 相同部分
class YAMLObjectMetaclass(type):
  def __init__(cls, name, bases, kwds):
    super(YAMLObjectMetaclass, cls).__init__(name, bases, kwds)
    if 'yaml_tag' in kwds and kwds['yaml_tag'] is not None:
      cls.yaml_loader.add_constructor(cls.yaml_tag, cls.from_yaml)
  # 省略其余定义

# Python 3
class YAMLObject(metaclass=YAMLObjectMetaclass):
  yaml_loader = Loader
  # 省略其余定义

# Python 2
class YAMLObject(object):
  __metaclass__ = YAMLObjectMetaclass
  yaml_loader = Loader
  # 省略其余定义

# YAMLObject 把 metaclass 都声明成了 YAMLObjectMetaclass，尽管声明方式在 Python 2 和 3 中略有不同。在 YAMLObjectMetaclass 中， 下面这行代码就是魔法发生的地方：

cls.yaml_loader.add_constructor(cls.yaml_tag, cls.from_yaml) 

#YAML 应用 metaclass，拦截了所有 YAMLObject 子类的定义。也就说说，在你定义任何 YAMLObject 子类时，Python 会强行插入运行下面这段代码，把我们之前想要的add_constructor(Foo)给自动加上。

cls.yaml_loader.add_constructor(cls.yaml_tag, cls.from_yaml)

#所以 YAML 的使用者，无需自己去手写add_constructor(Foo) 。
```

### 底层如何实现

- 深入理解Python类型模型
  - 所有的Python的用户定义的类，都是type这个类的实例
  - 用户自定义类，只不过是type类的__call__运算符重载
  - metaclass 是 type 的子类，通过替换 type 的__call__运算符重载机制，“超越变形”正常的类。

- 所有的Python的用户定义的类，都是type这个类的实例

```python
class MyClass:
    pass

instance = MyClass()
print(type(instance)) # <class '__main__.MyClass'>
print(type(MyClass)) # <class 'type '>

# instance 是 MyClass 的实例，而 MyClass 不过是“上帝”type 的实例。
```

- 用户自定义类，只不过是type类的__call__运算符重载

```python
class MyClass:
    data = 1

instance = MyClass()
print(MyClass, instance) # <class '__main__.MyClass'> <__main__.MyClass object at 0x7fc4b6f7b610>
print(instance.data) # 1

MyClass = type('MyClass', (), {'data':1})
instance = MyClass()
print(MyClass, instance) # <class '__main__.MyClass'> <__main__.MyClass object at 0x7fc4b6f472b0>
print(instance.data) # 1

# 正常的 MyClass 定义，和你手工去调用 type 运算符的结果是完全一样的
```

- metaclass 是 type 的子类，通过替换 type 的__call__运算符重载机制，“超越变形”正常的类。
  - 一旦你把一个类型 MyClass 的 metaclass 设置成 MyMeta，MyClass 就不再由原生的 type 创建，而是会调用 MyMeta 的__call__运算符重载。

```python

class = type(classname, superclasses, attributedict) 
# 变为了
class = MyMeta(classname, superclasses, attributedict)
```

### 使用metaclass的困扰

- metaclass在开发框架层面的 Python 库时使用的。
- 在应用层，metaclass 往往不是很好的选择。

## Note

- metaclass 与 类装饰器相似，大多数情况下本质上都是重载了 __call__ 函数，但有一个明显的区别是前者对【继承了 metaclass 的子类本身】的属性造成了影响，
- 而类装饰器是对【作为装饰器本身的类】造成影响而已，对【被装饰的类】的属性没有直接影响（间接影响就看被装饰的函数怎么操作了）。
- metaclass的应用：单例模式、ORM模式