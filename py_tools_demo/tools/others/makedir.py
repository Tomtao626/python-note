import os
base_path=r'E:\program\workspaces\gowork\Go-Python-Micro-Service\go-projects\golang-learn\levelup'
sup_file= {'01':['1'],
           '02':['1'],
           '03':['1'],
           '04':['1'],
           '05':['1'],
           '06':['1'],
           '07':['1'],
           '08':['1'],
           '09':['1'],
           '10':['1'],
           '11':['1'],
           '12':['1'],
           '13':['1'],
           '14':['1'],
           '15':['1'] }
for key,val in sup_file.items():
    path=os.path.join(base_path,key)
    for v in val:
        sub_path=os.path.join(path,v)
        os.makedirs(sub_path)
