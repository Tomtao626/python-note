import os
print(os.getcwd())

import os
os.path.join("My Project", "Dream")
print("c:\\" + os.path.join("My Project", "Dream"))


print(os.listdir("/Users/macos/Documents/workspaces"))
for i in os.scandir("/Users/macos/Documents/workspaces"):
    print(i)


import os
for dirpath, dirname, files in os.walk("/Users/macos/Documents/workspaces/pywork/Python_Interview_Note/subject/others"):
    print(f"发现文件夹\t{dirpath}")
    print(dirname)
    print(files)