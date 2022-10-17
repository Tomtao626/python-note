import numpy as np

print(np.arange(0, 12).reshape(4, 3))  ##reshape()将一维数组拆分成几个部分 4 指分成1个四维数组，四个一维数组 3指每个数组三个元素
print(np.linspace(0, 10, 5))  # 前两个参数用来指定序列的起始和结尾，第三个参数表示将指定范围内的序列分成几个部分
print(np.random.random(5))  # random()指生成包含5个随机元素的数组
print(np.random.random((3, 3)))  # 生成每个包含三个随机元素的3维数组
