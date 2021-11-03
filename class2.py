# class2.py 
#1)클래스 형식을 정의
class Person:
    #위치를 잘 본다~~
    num_person = 0 
    #초기화메서드(생성자)
    def __init__(self):
        self.name = "default name"
        Person.num_person += 1 
    #인스턴스 메서드
    def print(self):
        print("이름은 ", self.name)

#2)인스턴스 생성
p1 = Person()
p2 = Person()

#인스턴스 갯수 확인
print("몇개:", Person.num_person)


