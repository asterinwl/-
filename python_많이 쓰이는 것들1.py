## sep
print('S','E','P', sep='@')
# 출력 >>>>> S@E@P
# S , E , P라는 문자열 사이에 @가 끼워넣어져 출력된다. 즉, 구분자는 @가 된다.
print('1','2','3',sep='')
# 이 꼴로 제일 많이 쓰인다.

## end
print("I like", end=" ")
print("money")
# end옵션을 사용하면 그 뒤의 출력값과 이어서 출력한다. (즉, 줄바꿈을 하지 않게 된다.)

## \n \t
print("I like \nmondy")  # 줄바꿈
print("I like \tmondy")  # 뛰어쓰기

## format
print("{0}월{1}일 입니다.".format(10,31))
# 출력 >>>>> 10월31일 입니다.
a=30.5555
print(format(a, ".2f") )
print("{:.2f}".format(a)) # 이 형태가 많이 쓰인다. 이 형태를 외우자.
print("%.2f" %(a)) # 이 형태가 많이 쓰인다. 이 형태를 외우자.

print("%s을 %d개 주세요."%("아이스크림", 10))
# 출력 >>>>> 아이스크림을 10개 주세요.