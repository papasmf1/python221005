# class1.py
#1)클래스 정의(type)
class Person:
    #초기화메서드
    def __init__(self):
        self.name = "default name"
    #인스턴스메서드
    def print(self):
        print("My name is {0}".format(self.name))

#2)인스턴스(복사본)생성
#중단점(Break Point)
p1 = Person()
p2 = Person() 
p1.name = "전우치"
#3)메서드 호출
p1.print()
p2.print() 

