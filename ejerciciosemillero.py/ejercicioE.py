numerotiros = int(input())
turnos = list(map(int, input().split()))
print(sum(x for x in turnos if x != -1) / sum(1 for x in turnos if x != -1))

