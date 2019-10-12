#1부터 10까지의 어떤 수로도 나누어 떨어지는 가장 작은 수는 2520입니다.
#그렇다면 1부터 20까지의 어떤 수로도 나누어 떨어지는 가장 작은 수는 얼마입니까?
a=232792000
while True:
    a+=1
    check=[]
    for i in range(1,21):
        if(a%i==0):
            check.append(i)
    if(len(check) == 20):
        print(a)
        break




