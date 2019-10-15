a=input("키보드를 막 두들기시오: ")
b=['1','2','3','4','5','6','7','8','9','0']
result=''
for c in a:
    if c in b:
        result=result+c
print(result)
