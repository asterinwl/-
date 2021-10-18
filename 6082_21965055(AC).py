# 369 게임

N = int(input())
nList = [str(i) for i in range(1, N+1)]

for num in nList:
    cnt = 0
    if '3' in num:
        cnt += num.count('3')
    if '6' in num:
        cnt += num.count('6')
    if '9' in num:
        cnt += num.count('9')
    if cnt > 0:
        print('X'*cnt, end=' ')
    else:
        print(num, end=' ')
# 이 코드가 정확한 코드이다.
print()


n = int(input())
for i in range(1,n+1):
    if i%10 == 3 or i%10 == 6 or i%10 == 9:
        print("X", end=" ")
    else:
        print(i, end=" ")
# 이 코드는 29까지만 사용 가능한 코드이다.
