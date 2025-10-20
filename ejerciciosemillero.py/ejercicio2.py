totaldias = input()
temperatura = list(map(int, input().split()))

cont_dias = 0
for i in temperatura:
    if i<0:
        cont_dias += 1
print(cont_dias)


