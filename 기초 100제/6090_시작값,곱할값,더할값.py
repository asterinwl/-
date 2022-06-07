# 시작 값(a), 곱할 값(m), 더할 값(d), 몇 번째인지를 나타내는 정수(n)가 입력될 때,
# n번째 수를 출력하는 프로그램을 만들어보자.

a,m,d,n=input().split()
a=int(a)
m=int(m)
d=int(d)
n=int(n)
for i in range (1,n):
  a*=m
  a+=d
  #  a = a*m+d
print(a)

# 6088,6089 처럼 `while True : ~ break` 문을 사용했을 때 시간초과가 나왔다.
# for i in range () 가 시간이 훨씬 짧고 코드도 적은 것을 알 수 있다.
