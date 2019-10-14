#버전 비교하는 프로그램 작성하시오
# ex) 1.0.0 , 1.0.23, 2.1.0

a = input("버전1을 입력하시오")
b = input("버전2을 입력하시오")

ai = a.split('.')
bi = b.split('.')
if ai[0] > bi[0]:
    print(a + ">" + b)
else:
    if ai[1] > bi[1]:
        print(a + ">" + b)
    else:
        if ai[2] > bi[2]:
            print(a + ">" + b)
        else:
            print(a + "<" + b)