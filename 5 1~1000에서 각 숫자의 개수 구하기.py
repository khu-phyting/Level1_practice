#예로 10 ~ 15 까지의 각 숫자의 개수를 구해보자

a = [0,0,0,0,0,0,0,0,0,0]
for i in range(1,1001):
    for char in str(i):
        a[int(char)] += 1
print(a)