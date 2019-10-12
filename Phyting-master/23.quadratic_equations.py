#A씨는 학교숙제로 이차방정식 문제를 풀어야 한다. 하지만 시간이 얼마 없다.
# 이 A씨를 도와주기 위한 이차방정식 풀이 프로그램을 작성해라.
# (단, 일차방정식은 ax^2 + bx + c = 0의 꼴에서 a, b와 c를 입력받아 해를 구하고 해를 구하기 위해 근의 공식을 사용해야 한다.
# 또, 해는 정수로 반올림한 값을 구하고 해가 없거나 여러개인 경우도 모두 구해야 한다.)
import math

def fun(a,b,c) :
    D = b*b -4*a*c
    if(D>0):
        x1 = round((-b-D**0.5)/2*a)
        x2 = round((-b+D**0.5)/2*a)
        print("x","=",x1,",",x2)
    elif(D==0):
        x=round(-b/2*a)
        print("중근입니다")
        print("x","=", x)
    else:
        print("허근입니다")
a = int(input("a를 입력해 주세요\n"))
b = int(input("b를 입력해 주세요\n"))
c = int(input("c를 입력해 주세요\n"))
fun(a,b,c)
