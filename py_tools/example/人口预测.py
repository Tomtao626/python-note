# /usr/bin/env python
# -*- coding=UTF-8 -*-
'''person = 3120324986  #当前人口
years = 365*3600# 每年按365天计算，总的时间（秒）
bron_person = years//7 #每年出生人口
died_person = years//13 #每年死亡人口
remove_person = years//45 #每年的移民
person_add1 = (person + bron_person + remove_person) - died_person
print(person_add1)
#print(4505142+700800+3120324986-2425846)
'''

def PersonAdd(years):
    person = 3120324986
    time = years*365*3600
    predict_person = person + (time//7)+(time//45)-(time//13)
    return predict_person
print(PersonAdd(1))
print(PersonAdd(2))
print(PersonAdd(3))
print(PersonAdd(4))
print(PersonAdd(5))
print(PersonAdd(6))
