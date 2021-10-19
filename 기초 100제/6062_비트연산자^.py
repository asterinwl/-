# 입력된 정수 두 개를 비트단위로 xor 연산한 후 그 결과를 정수로 출력해보자.

a,b=input().split()
a=int(a)
b=int(b)
print(a^b)

# ** 비트단위(bitwise) 연산자는,
# ~(bitwise not), &(bitwise and), |(bitwise or), ^(bitwise xor),
# <<(bitwise left shift), >>(bitwise right shift)
# 가 있다.

# ^는 두 장의 이미지가 겹쳐졌을 때 색이 서로 다른 부분만 처리할 수 있다.
