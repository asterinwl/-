# 정수값이 입력될 때,
# 그 불 값을 반대로 출력하는 프로그램을 작성해보자.

a = bool(int(input()))
print(not a)

# a = bool(int(input()))
# 와 같은 형태로 겹쳐 작성하면, 한 번에 한 단계씩 계산/처리/평가된다.
# 위와 같은 명령문의 경우 input( ), int( ), bool( ) 순서로 한 번에 한 단계씩 계산/처리/평가된다.
# 어떤 불 값이나 변수에 not True, not False, not a 와 같은 계산이 가능하다.
