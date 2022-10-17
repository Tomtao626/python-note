import numpy as np

a = np.array([1, 2, 3, 4])  # 使用array()函数，以python列表作为参数，列表的元素即是ndarray的元素
print(a)  # 输出adarray
print(type(a))  # 检测新创建的对象是否是ndarray
print(a.dtype)  # 运用dtype,获取新建的ndarray输入哪种数据类型
print(a.ndim)  # 获取数组的轴，即秩的数量
print(a.shape)  # 获取数组的型，用shape
print(a.size)  # 获取数组的长度
