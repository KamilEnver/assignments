def sayac():
  cümle = input("lütfen bir cümle giriniz: ")
  a = {}  
  for i in cümle:
    a[i] = cümle.count(i)
  return print(a)
sayac()
