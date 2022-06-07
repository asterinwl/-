# 무작위로 중복 허용하고 뽑기

import random

n=int(input())
b=[]
for i in range(1,n+1):
  a = random.randint(1, 23) # randint(최소값,최대값) 비슷한 것:randrange
  b.append(a)
print(b)

b.reverse()    # 리스트의 형태를 거꾸로 돌리기
print(b)

for i in b :
    print(i,end=" ")   # [ ] 없애는 방법
print()

b.sort()   #리스트의 형태 작은 순서부터 정렬하기
print(b)

for i in b :
    print(i,end=" ")   # [ ] 없애는 방법

# 좋은 코드이다. 외우자.
