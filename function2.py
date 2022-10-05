# function2.py
#교집합 글자 리턴 
def intersect(prelist, postlist):
    #지역변수 
    result = []
    #H(0) | A(1) | M(2)
    for x in prelist:
        if x in postlist and x not in result:
            result.append(x)
    return result 

#호출
print( intersect("HAM","SPAM") ) 

#가변형식
def change(x):
    x[0] = "H"

#호출
wordlist = ["J","A","M"]
change(wordlist)
print("함수호출후:", wordlist)

print("---코드를 수정---")
def change(x):
    #복사본을 생성
    x1 = x[:]
    x1[0] = "H"
    print("함수내부:", x1)

#호출
wordlist = ["J","A","M"]
change(wordlist)
print("함수호출후:", wordlist)

#불변형식에서 함수내부에서 읽기+쓰기
g = 1 
def testScope(a):
    #global g 
    g = 2 
    return a+g 

#함수호출
print( testScope(1) )
print("전역변수 g:", g)

#기본값
def times(a=10,b=20):
    return a*b 

#호출
print( times() )
print( times(5) )
print( times(5,6) )

#키워드 인자
def connectURI(server, port):
    strURL = "http://" + server + ":" + port 
    return strURL 

#호출
print( connectURI("credu.com", "80") )
print( connectURI(port="80", server="credu.com") )

