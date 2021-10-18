#입력된 정수 두 개를 비트단위로 or 연산한 후 그 결과를 정수로 출력해보자.

a,b=input().split()
a=int(a)
b=int(b)
print(a|b)

# ** 비트단위(bitwise) 연산자는,
# ~(bitwise not), &(bitwise and), |(bitwise or), ^(bitwise xor),
# <<(bitwise left shift), >>(bitwise right shift)
# 가 있다.

# 비트단위 or 연산은 둘 중 하나라도 1인 자리를 1로 만들어주는 것과 같다.