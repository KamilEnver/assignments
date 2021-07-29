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
