x = input("bir sayı giriniz: ")
y = len(x)
summ = 0
 
for i in range(y):
  summ += int(x[i]) ** y
if (summ == int(x)) :
    print(x, "is an Armstrong Number")
else:
   print(x, "is not an Armstrong Number")
