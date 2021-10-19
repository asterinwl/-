# 무작위로 중복없이 뽑기

# 입력 예시
import random

n=int(input())
a=random.randint(1,23) # randint(최소,최대) 비슷한 것 : randrange
b=[]
for i in range(1,n+1):
   while a in b:                    # b에서 골라진 임의의 숫자가 이미 list에
        a = random.randint(1, 23)   # 있다면 다시 뽑으라는 의미
   b.append(a)
print(b)

for i in b :
    print(i,end=" ")  # [ ] 없애는 방법
print()


# 출력 예시
list=[]                 # 출력시에는 한 칸 넉넉하게 해야 오류가 안난다
for i in range(1,25):   # range(1,n) 은 1부터 n-1까지. n=25이면 1,2...,23,24
    list.append(0)      # 24개에 0을 싹 다 집어넣는다.

for i in range(n):      # 번호를 부를 때마다, 그 번호에 대한 카운트 1씩 증가
    list[b[i]] += 1
print(list[1:24])       # 값은 1부터 보여주기를 원하므로 list[1:24]가 맞다.

for i in list[1:24]:
    print(i,end=" ")    # [ ] 없애는 방법

# 좋은 코드이다. 입력 방법과 출력 방법 모두 다 외우자.