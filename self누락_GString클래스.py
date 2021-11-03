#전역변수 
str = "Not Class Member"
#파이썬은 명확하게 코딩해야 좋다~~ 
#클래스 정의 
class GString:
    def __init__(self):
        #인스턴스 멤버 변수 self.str 
        self.str = "" 
    def set(self, msg):
        self.str = msg
    def print(self):
        #약간의 버그(실수)
        print(self.str)

#인스턴스(복사본)생성 
g = GString()
g.set("First Message")
g.print()
