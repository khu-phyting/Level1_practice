#자기 자신을 제외한 모든 양의 약수들의 합이 자기 자신이 되는 자연수를 완전수라고 한다.
# 예를 들면, 6과 28은 완전수이다.
# 6=1+2+3 // 1,2,3은 각각 6의 약수 28=1+2+4+7+14 // 1,2,4,7,14는 각각 28의 약수
#입력으로 자연수 N을 받고, 출력으로 N 이하의 모든 완전수를 출력하는 코드를 작성하라.

input = int(input())
for a in range(1,input+1):
    list = []
    sum = 0
    for i in range(1, a):
        if (a % i == 0):
            list.append(i)
    for i in list:
        sum = sum + i
    if (a == sum):
        print(a)
