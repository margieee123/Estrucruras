mb = int(input()) 
meses = int(input())  

total = mb
for _ in range(meses):
    gasto = int(input())
    total += mb - gasto 
print(total)
