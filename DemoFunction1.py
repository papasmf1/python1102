# DemoFunction1.py 
#함수를 정의
def setValue(newValue):
    x = newValue

#함수를 호출
result = setValue(5)
print(result)

#함수를 정의
def swap(x,y):
    return y,x 

#호출
print( swap(5,6) )

#디버깅 연습을 위한 함수(교집합 문자를 만들기)
def intersect(prelist, postlist):
    #지역변수에 리스트로 저장하기
    result = []
    #H(0) | A(1) | M(2)
    for x in prelist:
        #x라는 글자가 postlist에 있고 그리고 x가 아직 result에는 없고 
        if x in postlist and x not in result:
            result.append(x)
    return result 

#함수를 호출
print( intersect("HAM","SPAM"))
