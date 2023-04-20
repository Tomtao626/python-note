#pass  空语句 不执行

import os
cmd  = input("输入指令：")
if cmd == "关机":
    os.system("shutdown -s -t 3600")
else:
    pass
print("game over")
