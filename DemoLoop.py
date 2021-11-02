#주석: DemoLoop.py 

#계산을 해야 하는 경우
value = 5 
while value > 0:
    print(value)
    value -= 1 

print("---두번째 연습---")
value = 1 
while value < 10:
    print(value)
    value += 1 

#갯수를 이미 알고 있는 경우
lst = ["apple", 100, 3.14]
print("갯수:", len(lst))
for item in lst:
    print(item, type(item))

#딕셔너리
d = {"apple":100, "kiwi":200, "orange":300}
for item in d.items():
    print(item)




