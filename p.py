class Student:
    school = 'Telusko'


    def __init__(self,m1,m2,m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3



    def avg(self):
        return(self.m1+self.m2+self.m3)/3

    @classmethod
    def info(cls):
        return cls.school
        
    @staticmethod
    def print():
        print("this is static method")


s1 = Student(23,32,43)

print(s1.avg())
print(Student.info())
print(Student.print())
