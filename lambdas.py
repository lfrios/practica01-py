dos = lambda: 2
sqr = lambda x: x * x
pwr = lambda x, y: x ** y

for a in range(-3, 4):
  print(sqr(a), end=" ")
  print(pwr(a, dos()))