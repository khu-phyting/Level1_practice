#DashInsert 함수는 숫자로 구성된 문자열을 입력받은 뒤,
#문자열 내에서 홀수가 연속되면 두 수 사이에 - 를 추가하고,
# 짝수가 연속되면 * 를 추가하는 기능을 갖고 있다.
# (예, 454 => 454, 4546793 => 454*67-9-3) DashInsert 함수를 완성하자

a = input("숫자를 입력하시오")
b=[]

for i in range(0, len(a)-1):
    if (int(a[i])%2==0 and int(a[i+1])%2==0):
        b.append(a[i]+"*")

    elif (int(a[i])%2==1 and int(a[i+1])%2==1):
        b.append(a[i] + "-")

    else:
        b.append(a[i])

print("".join(b) + a[len(a)-1])