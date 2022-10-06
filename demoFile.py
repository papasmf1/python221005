# demoFile.py
#파일쓰기
f = open("c:\\work\\test.txt", "wt", encoding="utf-8")
f.write("첫번째\n두번쩨\n세번째\n")
f.close()

#파일읽기
f = open("c:\\work\\test.txt", "rt", encoding="utf-8")
print( f.read() )
print( f.tell() )
#파일 포인터를 리셋
f.seek(0)
print( f.readline(), end="" )
print( f.readline(), end="" )
f.seek(0)
result = f.readlines()
print(result)
for item in result:
    #print(item, end="")
    print(item.replace("\n", ""))
f.close() 

#기존 파일에 첨부하는 경우
f = open("c:\\work\\test.txt", "wt", encoding="utf-8")
f.write("다른 데이터\n")
f.close() 