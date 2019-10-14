#예로, 10~15까지의 각 숫자 분해하여 곱하기의 전체 합은 다음과 같다.
#10 = 1 * 0 = 0
# 11 = 1 * 1 = 1
# 12 = 1 * 2 = 2
# 13 = 1 * 3 = 3
# 14 = 1 * 4 = 4
# 3 15 = 1 * 5 = 5

#그러므로, 이 경우의 답은 0+1+2+3+4+5 = 15

sum=0
for n in range(10,1001):
    part=1
    for i in str(n):
        part*=int(i)
    sum+=part
print(sum)



#k =0
#sum = 0
#sum2 = 0
#for i in range(10, 1001):
 #   if len(str(i)) ==2:
  #      a = int(str(i)[k]) * int(str(i)[k+1])
   #     sum = sum +a
   # elif len(str(i)) ==3:
    #    b =int(str(i)[k]) * int(str(i)[k + 1]) * int(str(i)[k + 2])
     #   sum2 = sum2 +b
#print(sum+sum2)

     #for c in str(i):
       # print(c[0]*c[1])