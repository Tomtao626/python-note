In [1]: import re

In [2]: result = re.match("hello","hello world")

In [3]: result = re.match(r"hello","hello world")

In [4]: print(result)
<_sre.SRE_Match object; span=(0, 5), match='hello'>

In [5]: result = re.match(r"[Hh]ello","hello world")

In [6]: print(result)
<_sre.SRE_Match object; span=(0, 5), match='hello'>

In [7]: result = re.match(r"[Hh]ello","Hello world")

In [8]: print(result)
<_sre.SRE_Match object; span=(0, 5), match='Hello'>

In [9]: re.match("速度与激情\d","速度与激情5")
Out[9]: <_sre.SRE_Match object; span=(0, 6), match='速度与激情5'>

In [10]: ret = re.match("速度与激情\d","速度与激情5")

In [11]: ret.group()
Out[11]: '速度与激情5'

In [12]: ret = re.match("速度与激情\d*","速度与激情55")

In [13]: re.group()
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
<ipython-input-13-256e58933302> in <module>()
----> 1 re.group()

AttributeError: module 're' has no attribute 'group'

In [14]: ret = re.match("速度与激情\d\d","速度与激情55")

In [15]: re.group()
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
<ipython-input-15-256e58933302> in <module>()
----> 1 re.group()

AttributeError: module 're' has no attribute 'group'

In [16]: ret = re.match("速度与激情[0-9]","速度与激情55")

In [17]: re.group()
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
<ipython-input-17-256e58933302> in <module>()
----> 1 re.group()

AttributeError: module 're' has no attribute 'group'

In [18]: ret.group()
Out[18]: '速度与激情5'


[4]+  Stopped                 ipython3
root@tomtao:/home/tooy# ipython3
Python 3.6.9 (default, Nov  7 2019, 10:44:02)
Type "copyright", "credits" or "license" for more information.

IPython 5.5.0 -- An enhanced Interactive Python.
?         -> Introduction and overview of IPython's features.
%quickref -> Quick reference.
help      -> Python's own help system.
object?   -> Details about 'object', use 'object??' for extra details.

In [1]: ret = re.match("速度与激情[0-9]","速度与激情9")
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
<ipython-input-1-6b2c2e0823b2> in <module>()
----> 1 ret = re.match("速度与激情[0-9]","速度与激情9")

NameError: name 're' is not defined

In [2]: import re

In [3]: ret = re.match("速度与激情[0-9]","速度与激情9")

In [4]: ret.group()
Out[4]: '速度与激情9'

In [5]: ret = re.match("速度与激情[1-36-8]","速度与激情9")

In [6]: ret.group()
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
<ipython-input-6-0c062bb84e23> in <module>()
----> 1 ret.group()

AttributeError: 'NoneType' object has no attribute 'group'

In [7]: ret = re.match("速度与激情[1-36-8A-Za-z]","速度与激情E")

In [8]: ret.group()
Out[8]: '速度与激情E'

In [9]: ret = re.match("速度与激情\w","速度与激情E")

In [10]: ret.group()
Out[10]: '速度与激情E'

In [11]: ret = re.match("速度与激情\w","速度与激情!")

In [12]: ret.group()
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
<ipython-input-12-0c062bb84e23> in <module>()
----> 1 ret.group()

AttributeError: 'NoneType' object has no attribute 'group'

In [13]: ret = re.match("速度与激情\s\w","速度与激情\t1")

In [14]: ret.group()
Out[14]: '速度与激情\t1'

In [15]: ret = re.match("速度与激情.","速度与激情\t1")

In [16]: ret.group()
Out[16]: '速度与激情\t'

In [17]: ret = re.match("速度与激情\d{1,3}","速度与激情\t1")

In [18]: ret.group()
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
<ipython-input-18-0c062bb84e23> in <module>()
----> 1 ret.group()

AttributeError: 'NoneType' object has no attribute 'group'

In [19]: ret = re.match("速度与激情\d{1,3}","速度与激情123")

In [20]: ret.group()
Out[20]: '速度与激情123'

In [21]: ret = re.match("速度与激情\d{3,4}-?\d{8}","18372620761")

In [22]: ret.group()
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
<ipython-input-22-0c062bb84e23> in <module>()
----> 1 ret.group()

AttributeError: 'NoneType' object has no attribute 'group'

In [23]: ret = re.match("速度与激情\d{3,4}-?\d{8}","0718-1234567")

In [24]: ret.group()
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
<ipython-input-24-0c062bb84e23> in <module>()
----> 1 ret.group()

AttributeError: 'NoneType' object has no attribute 'group'

In [25]: re.match("速度与激情\d{3,4}-?\d{8}","0718-1234567")

In [26]: re.match("速度与激情\d{3,4}-?\d{8}","0718-1234567").group()
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
<ipython-input-26-d7befc67e251> in <module>()
----> 1 re.match("速度与激情\d{3,4}-?\d{8}","0718-1234567").group()

AttributeError: 'NoneType' object has no attribute 'group'

In [27]: re.match(r"\d{3,4}-?\d{8}","0718-1234567").group()
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
<ipython-input-27-04bb85ff13b8> in <module>()
----> 1 re.match(r"\d{3,4}-?\d{8}","0718-1234567").group()

AttributeError: 'NoneType' object has no attribute 'group'

In [28]: re.match(r"\d{3,4}-?\d{8}","0718-12345678").group()
Out[28]: '0718-12345678'

In [29]: re.match(r"\d{3,4}-?\d{7,8}","0718-1234567").group()
Out[29]: '0718-1234567'

In [30]: html_content = """"""

In [31]: html_content = """23432
    ...: 42423
    ...: 2342
    ...: 3423
    ...: 4
    ...: 234
    ...: 242
    ...:
    ...: fdg
    ...: df
    ...: g
    ...: fdgf
    ...: d
    ...: gdfg"""

In [32]: re.match(r".*",html_content)
Out[32]: <_sre.SRE_Match object; span=(0, 5), match='23432'>

In [33]: re.match(r".*",html_content).group()
Out[33]: '23432'

In [34]: re.match(r".*",html_content, re.S).group()
Out[34]: '23432\n42423\n2342\n3423\n4\n234\n242\n\nfdg\ndf\ng\nfdgf\nd\ngdfg'

In [35]: re.match(r".+",html_content).group()
Out[35]: '23432'

In [36]: re.match(r".+","").group()
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
<ipython-input-36-3b3e27bb3407> in <module>()
----> 1 re.match(r".+","").group()

AttributeError: 'NoneType' object has no attribute 'group'

In [37]: names = ["name1".]
  File "<ipython-input-37-4a31428d15e8>", line 1
    names = ["name1".]
                     ^
SyntaxError: invalid syntax


In [38]:

In [38]: names = ["name1","_name","2_name","__name__"]

In [39]: for name in names:
    ...:     ret = re.match(r"[a-zA-Z]",name)
    ...:     if ret:
    ...:         print("yes %s "% ret.group())
    ...:     else:
    ...:         print("no %s "% name)
    ...:
yes n
no _name
no 2_name
no __name__

In [40]: for name in names:
    ...:     ret = re.match(r"[a-zA-Z_]+[\w]+",name)
    ...:     if ret:
    ...:         print("yes %s "% ret.group())
    ...:     else:
    ...:         print("no %s "% name)
    ...:
yes name1
yes _name
no 2_name
yes __name__

In [41]: for name in names:
    ...:     ret = re.match(r"^[a-zA-Z_]+[\w]+$",name)
    ...:     if ret:
    ...:         print("yes %s "% ret.group())
    ...:     else:
    ...:         print("no %s "% name)
    ...:
yes name1
yes _name
no 2_name
yes __name__

In [42]:

In [42]: re.match(r"^[a-zA-Z_0-9]{4,20}@163\.com$","tom_tao@163.com")
Out[42]: <_sre.SRE_Match object; span=(0, 15), match='tom_tao@163.com'>

In [43]: re.match(r"^[a-zA-Z_0-9]{4,20}@163\.com$","tom_tao@163.com").group()
Out[43]: 'tom_tao@163.com'

In [44]: re.match(r"^[a-zA-Z_0-9]{4,20}@(163|126|qq)\.com$","tom_tao@163.com").group()
Out[44]: 'tom_tao@163.com'

In [45]: re.match(r"^([a-zA-Z_0-9]{4,20})@((163|126|qq))\.com$","tom_tao@163.com").group()
Out[45]: 'tom_tao@163.com'

In [46]: re.match(r"^([a-zA-Z_0-9]{4,20})@((163|126|qq))\.com$","tom_tao@163.com").group(1)
Out[46]: 'tom_tao'

In [47]: re.match(r"^([a-zA-Z_0-9]{4,20})@((163|126|qq))\.com$","tom_tao@163.com").group(2)
Out[47]: '163'

In [48]: html_str = "<h1>534535gfdhdf</h1>"

In [49]: re.match(r"<\w*>.*</\w*>",html_str).group()
Out[49]: '<h1>534535gfdhdf</h1>'

In [50]: html_str = "<h1><h2>534535gfdhdf</h2></h1>"

In [51]: re.match(r"<\w*><\w*>.*</\w*></\w*>",html_str).group()
Out[51]: '<h1><h2>534535gfdhdf</h2></h1>'

In [52]: re.match(r"(<\w*>)(<\w*>).*</\1></\2>",html_str).group()
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
<ipython-input-52-a954052f2bee> in <module>()
----> 1 re.match(r"(<\w*>)(<\w*>).*</\1></\2>",html_str).group()

AttributeError: 'NoneType' object has no attribute 'group'

In [53]: re.match(r"(<\w*>)(<\w*>).*</\2></\1>",html_str).group()
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
<ipython-input-53-a0d871cb5311> in <module>()
----> 1 re.match(r"(<\w*>)(<\w*>).*</\2></\1>",html_str).group()

AttributeError: 'NoneType' object has no attribute 'group'

In [54]: re.match(r"(<\w*>)(<\w*>).*</\1></\2>",html_str).group()
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
<ipython-input-54-a954052f2bee> in <module>()
----> 1 re.match(r"(<\w*>)(<\w*>).*</\1></\2>",html_str).group()

AttributeError: 'NoneType' object has no attribute 'group'

In [55]: re.match(r"<(\w*)><(\w*)>.*</\1></\2>",html_str).group()
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
<ipython-input-55-a696d0cab2ed> in <module>()
----> 1 re.match(r"<(\w*)><(\w*)>.*</\1></\2>",html_str).group()

AttributeError: 'NoneType' object has no attribute 'group'

In [56]: re.match(r"<(\w*)><(\w*)>.*</\2></\1>",html_str).group()
Out[56]: '<h1><h2>534535gfdhdf</h2></h1>'

In [57]: re.search(r"\d+","阅读次数为 9999").group()
Out[57]: '9999'

In [58]: re.search(r"\d+","阅读次数为 9999, 点赞数为 31233").group()
Out[58]: '9999'

In [59]: re.findall(r"\d+","阅读次数为 9999, 点赞数为 31233").group()
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
<ipython-input-59-346da1765146> in <module>()
----> 1 re.findall(r"\d+","阅读次数为 9999, 点赞数为 31233").group()

AttributeError: 'list' object has no attribute 'group'

In [60]: re.findall(r"\d+","阅读次数为 9999, 点赞数为 31233")
Out[60]: ['9999', '31233']

InIn [61]: re.sub(r"\d+""8888","python=999")
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-61-6ac517d41441> in <module>()
----> 1 re.sub(r"\d+""8888","python=999")

TypeError: sub() missing 1 required positional argument: 'string'

In [62]: re.sub(r"\d+",33435d,"python=999")
  File "<ipython-input-62-3bc550470dfa>", line 1
    re.sub(r"\d+",33435d,"python=999")
                       ^
SyntaxError: invalid syntax


In [63]: re.sub(r"\d+","552532","python=999")
Out[63]: 'python=552532'
