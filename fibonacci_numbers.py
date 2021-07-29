number1 = 1
number2 = 1
summ = 0
fibonacci_list = [1,1]
while summ < 55:
  summ = number1 + number2
  fibonacci_list.append(summ)
  number1 = number2
  number2 = summ
print(fibonacci_list) 

2. Çözüm

liste = []
n = 0
for i in range(10):
  if (i==0) or (i==1):
    n = 1
    liste.append(n)
  else:
    n = liste[i-2]+liste[i-1]
    liste.append(n)
print("Fibonacci's first ten numbers:",liste)


