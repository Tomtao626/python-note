class school(object):
    def __init__(self,name,addr):
        self.name= name
        self.addr= addr
        self.teachers = []
        self.students = []
        self.staff = []
    def enroll(self,stu_obj):
        print("为学员%s办理注册手续"% stu_obj)
        self.students.append(stu_obj)
    def hire(self,staff_obj):
        self.staff.append(staff_obj)
        print("雇佣新员工%s" % staff_obj.name)
class Schoolmember(object):
    def __init__(self,name,age,sex):
        self.name = name
        self.age = age
        self.sex = sex
    def tell(self):
        pass

class teacher(Schoolmember):
    def __init__(self,name,age,sex,salary,course,school_obj):  #先覆盖
        super(teacher, self).__init__(name,age,sex)  #再继承
        # Schoolmember.__init__(self.name,age,sex)  经典类  不适用于多继承
        self.school.name = school_obj  #组合self.school.  后面任意调用
        self.salary = salary  #再调用自己的功能
        self.course = course
    def tell(self):
        print('''
        ----info of teacher:%s----
        Name:%s
        Age:%s
        Sex:%s
        salary:%s
        course:%s
        ''' %(self.name,self.name,self.age,self.sex,self.salary,self.course))
    def teach(self):
        print("$s is teaching course"% self.name,self.course)
class student(Schoolmember):
    def __init__(self,name,age,sex,stu_id,grade):
        super(student, self).__init__(name,age,sex)
        self.stu_id = stu_id
        self.grade = grade

    def tell(self):
        print('''
        ----info of student:%s----
        Name:%s
        Age:%s
        Sex:%s
        stu_id:%s
        grade:%s
        ''' %(self.name,self.name,self.age,self.sex,self.stu_id,self.grade))
    def pay_money(self,amount):
        print("%s has paid money for $%s"%(self.name,amount))

school = school("老男孩IT","沙河")
t1 = teacher("Tom_tao",20,"man",20000,"Linux")
t2= teacher("Alex",22,"man",3000,"Python")
s1 = student("lizijian",30,"man",1001,"Python")
s2 = student("zhanghua",19,"man",1002,"Linux")

t1.tell()

s1.tell()
school.hire(t1)
school.enroll(s1)
school.enroll(s2)
print(school.students)
print(school.staff)
school.staff[0].teach()

for stu in school.students:
    stu.pay_money(5000)