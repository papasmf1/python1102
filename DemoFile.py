# DemoFile.py 

#파일에 쓰기(write + text)
#mac, linux: /users/kim/Desktop/work 
#win: c:\work\test.txt 특수문자(탈출문자)
f = open("c:\\work\\demo.txt", "wt")
f.write("첫번째\n두번째\n세번째\n")
#버퍼를 비우고 작업을 종료 
f.close() 

#파일을 읽기(read + text)
f = open("c:\\work\\demo.txt", "rt")
print( f.readline() )
print( f.readline() )
print("---하나의 문자열로 읽기---")
print( f.tell() )
f.seek(0)
result = f.read() 
print( result )