numbers = [-1, 1, 3, -2, 2]
Pos_ary = []
Neg_ary = []

for number in numbers:
    if number < 0:
        Neg_ary.append(number)  # append()함수를 이용해서 리스트에 요소를 추가.  리스트명.append(요소) 형태로 사용
        # insert()함수를 이용해서 리스트에 요소를 추가할 수도 있음. 리스트명.insert(위치,요소) 형태로 사용

    else:
        Pos_ary.append(number)

Output = Neg_ary + Pos_ary  # 리스트를 연결할 때는 문자열 연결 연산자 +를 사용해서 리스트를 연결한다.
print(Output)  # 리스트를 반복할 때는 문자열 반복 연산자 *를 사용해서 리스트를 반복한다.
