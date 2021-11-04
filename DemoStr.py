# DemoStr.py 

#멤버 목록 
#print( dir(str) )

strA = "python is very powerful"
print( len(strA) )
print( strA.capitalize() )
print( strA.count("p") )
print( strA.endswith("ful") )

names = ["전우치","이순신","김유신"]
for name in names:
    print("안녕하세요 멋진 가을입니다. {0}님".format(name))
    print("="*40)

#문자열 가공 
u = "<<<  spam and ham  >>>"
print(u)
result = u.strip("<> ")
print(result)
result = result.replace("spam", "spam egg")
print(result)
lst = result.split() 
print( lst )
print("---하나의 문자열로 합치기---")
print( ":)".join(lst) )




