class Rectangle:
    def __init__(self, width, height) :
        self.width = width
        self.height = height
    def area(self):
        return self.width*self.height

# 인스턴스 생성 시 생성자 메서드 호출
rectangle1 = Rectangle(3, 4)
print(rectangle1.width) # 출력 결과: 3
print(rectangle1.height) # 출력 결과: 4

# 인스턴스 메서드 호출
print(rectangle1.area()) # 출력 결과: 12
'''

class Claculator:  #초기화 해줄 필요가 없을 땐 굳이 생성자 만들지 않음
    operator = '+'

    @classmethod
    def set_operator(cls, new_oprator):
        cls.operator = new_oprator


class Deposit:
    def _init_(self, initial, interest, n):
        self.initial = initial
        self.interest = interest
        self.n = n
        initial*(1+interest)**n

#    @classmethod
    def profit(self):
        return int(self.initial*(1+self.interest)**self.n)

deposit = Deposit(1000000, 0.035, 7)
print(deposit.profit())


class People:
    def __init__(self, age=0, name=None) :
        self.age = age
        self.name = name

    def get_name(self):
        return self.__name
    def set_name(self, name):
        self.__name = name

    def get_age(self):
        return self.__age
    def set_age(self, age):
        self.__age = age

    def introMe(self):
        print("name : ", self.__name, "age : ", str(self.__age))
        
class Teacher(People):
    def __init__(self, age=0, name=None, school=None):
        super().__init__(age, name, school)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def getName(self):
        print(self.name)
    def getAge(self):
        print(self.age)
    
class Employee(Person):
    def __init__(self, name, age, employeeID):
        super().__init__(name, age)
        self.employeeID = employeeID
    def getID(self):
        print(self.employeeID)

temp = Employee("동양", 65, 2019)
print(temp.getName)
print(temp.getAge)
print(temp.getID)




class Character:
    def __init__(self, name, level, health):
        self.name = name
        self.level = level
        pass

class Player:
    def __init__(self):
        
class Monster:
    def __init__(self):
        
class Game:
    def __init__(self):
        self.player = None
        self.monster = None

                
'''

class Student:
    def __init__(self, name, student_id, year, major, avg_score):
        self.name = name
        self.student_id = student_id
        self.year = year
        self.major = major
        self.avg_score = avg_score
    
    def get_info(self):
        print("name : ", self.name, "student_id : ", self.student_id, "year : ", self.year, "avg_score", self.avg_score)
'''
    def get_name(self):
        return self.__name
    def set_name(self, name):
        self.__name = name

    def get_student_id(self):
        return self.__student_id
    def set_student_id(self, student_id):
        self.__student_id = student_id

    def get_year(self):
        return self.__year
    def set_year(self, year):
        self.__year = year

    def get_major(self):
        return self.__major
    def set_major(self, major):
        self.__major = major

    def get_avg_score(self):
        return self.__avg_score
    def set_avg_score(self, avg_score):
        self.__avg_score = avg_score

    def get_info(self):
        print("name : ", self.__name, "student_id : ", self.__student_id, "year : ", self.__year, "avg_score", self.__avg_score)
'''
    

class StudentManager:
    def __init__(self):
        self.student_list = []

    def add_student(self, student):
        self.student_list.append(student)
    
    def remove_student(self, student_id):
         for student in self.student_list:
             if student.student_id == student_id:
                 self.student_list.remove(student)
                 print(f"{student_id}번의 {student.name}이 삭제되었습니다")

    def find_student(self, student_id):
        for student in self.student_list:
            if student.student_id == student_id:
                print(f"{student_id}번의 {student.name}학생을 찾았습니다")
                return
        print(f"{student_id}번의 학생을 찾을 수 없습니다")

    def show_all_student(self):
        for student in self.student_list:
            print(student.get_info())


student_manager = StudentManager()
student1 = Student('홍길동', '20230001', 2, '컴퓨터공학', 90.5)
student2 = Student('김철수', '20230002', 3, '전자공학', 85.2)
student3 = Student('이영희', '20230003', 1, '수학', 92.8)


student_manager.add_student(student1)
student_manager.add_student(student2)
student_manager.add_student(student3)

student_manager.find_student('20230001')

student_manager.show_all_student()

student_manager.remove_student('20230001')

student_manager.show_all_student()

student_manager.find_student('20230001')
student_manager.find_student('20230002')
student_manager.show_all_student()




