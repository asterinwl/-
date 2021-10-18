r,g,b=input().split()
r=int(r)
g=int(g)
b=int(b)
for A in range(0,r):
    for B in range(0,g):
        for C in range(0,b):
            print(A,B,C)
print(r*g*b)

# for i in range 꼴을 절대 잊지 말자.. for안써서 오류라니 ㅠㅠ
