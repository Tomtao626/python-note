import importlib
lib = importlib.import_module('lib.aa')
print(lib)
aa = importlib.import_module('lib.aa')
obj = aa.C()
#assert 断言

assert type(obj.name) is str
print("sdfsd")
''' 
lib =__import__('lib.aa')
lib.aa'''
