m = int(input("> 총 건수를 입력하시오: "))
n = int(input(">한 페이지에 보여줄 게시물 수를 입력하시오: "))

if n <= 0:
    print(("1이상의 수를 입력하시오."))
    n = int(input(">한 페이지에 보여줄 게시물 수를 입력하시오: "))

if m > n:
    output = (m // n) + 1

elif m == n:
    output = (m // n)

elif (m // n) == 0:
    output = m // n
    
else:
    ouput = (m // n) + 1

print(m, n, output)
