# func

## 函数

```python
def printMax(a, b = 1):
    if a > b:
        print(a)
        return a
    else:
        print(b)
        return b
x = 5
y = 7
printMax(x, y)

def update(*args,**kwargs):
    p=''
    for i,t in kwargs.items():
            p = p+ '%s=%s,' %(i,str(t))
    sql = "update  'user' set (%s) where (%s)" %(args[0],p)
    print(sql)

update('aaa',uu='uu',id=3)
```
