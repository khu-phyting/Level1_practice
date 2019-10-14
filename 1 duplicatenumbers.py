#0~9까지의 문자로 된 숫자를 입력 받았을 때,
#이 입력 값이 0~9까지의 숫자가 각각 한 번 씩만 사용된 것인지 확인하는 함수를 구하시오.
a= input("0~9 사이의 숫자를 입력하시오.")
if len(set(a))== 10:
    print("true")
else:
    print("false")

print(set(a))
