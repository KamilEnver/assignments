n = int(input("enter a number : "))
L = []
for j in range(1,n+1):
    count = 0
    for i in range(1,j+1):
      if j % i == 0:
       count += 1
    if not ((j == 1) or (count >= 3)):
     L.append(j)
print(L)