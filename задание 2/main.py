y = float(input("Введите y: "))
x = float(input("Введите x: "))

if 0 <= x <= 6 and -6 <= y <= 6: 
  if (x**2+y**2)**0.5 <= 6:
    if y >= 0:
      print(True)
    elif 0 <= x <= 6 and -6 <= y <= 0 and -6 <= y - x <= 0:
      print(True)
    else:
      print(False)
  else:
    print(False)
else:
  print(False)