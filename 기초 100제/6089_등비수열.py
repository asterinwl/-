# 등비수열 문제
# 시작 값(a), 등비(r), 몇 번째인지를 나타내는 정수(n)가 입력될 때
# n번째 수를 출력하는 프로그램을 만들어보자.

a,r,n=input().split()
a=int(a)
r=int(r)
n=int(n)
b=0
while True:
  a*=r
  b+=1
  if b==n-1:
    break
print(a)
