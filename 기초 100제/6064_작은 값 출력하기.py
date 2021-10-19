a,b,c=input().split()
a=int(a)
b=int(b)
c=int(c)
d=(a if a<b else b) if ((a if a<b else b)<c) else c
print(d)

# 예를 들어
# (a if a>b else b) if ((a if a>b else b)>c) else c
# 와 같은 계산식은 a, b, c 의 값 중 가장 큰 값으로 계산된다.
# 너무.. 어려운데???
