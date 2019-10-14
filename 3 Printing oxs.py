#input은 int n을 입력 받아 첫번째 row는 (n-1)의 O와 X, 두번째 row는 (n-2)의 O와 XX,
# 세번째 row는 (n-3)의 0와 XXX... n번째 row는 n의 X을 출력하시오.

a =  input("숫자 n 을 입력하시오")
for i in range(1 , int(a)+1):
    print("O" * (int(a)-i)+"X" *i)



#for i in range(0, int(a)):
