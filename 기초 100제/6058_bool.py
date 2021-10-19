# 2개의 정수값이 입력될 때,
# 그 불 값(True/False) 이 모두 False 일 때에만 True 를 출력하는 프로그램을 작성해보자.

a,b=input().split()
print((not bool(int(a))) and (not bool(int(b))))

# 정답
# 한꺼번에 써야지 오류가 발생하지 않는다.
