#부모 클래스를 정의 
class Person:
    def __init__(self, name, phoneNumber):
        self.name = name
        self.phoneNumber = phoneNumber
    def printInfo(self):
        print("Info(Name:{0}, Phone Number: {1})".format(
            self.name, self.phoneNumber))

#자식 클래스를 정의 
class Student(Person):
    #선택한 블럭 주석 처리: ctrl + / 
    def __init__(self, name, phoneNumber, subject, studentID):
        #명시적으로 부모의 초기화 메서드 호출
        Person.__init__(self, name, phoneNumber)
        self.subject = subject
        self.studentID = studentID
    #상속받은 메서드를 덮어쓰기(재정의, override)
    def printInfo(self):
        print("학생정보( {0} , {1} , {2} , {3} )".format(
            self.name, self.phoneNumber, self.subject, self.studentID))



p = Person("전우치", "010-222-1234")
s = Student("이순신", "010-111-1234", "컴공", "991122") 
p.printInfo()
s.printInfo()

