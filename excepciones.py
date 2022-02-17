import math

#x = float(input("Ingresa x: "))
#y = math.sqrt(x)

#print("La raíz cuadrada de", x, "es igual a", y)


first_number = int(input("ingresa el primer numero: "))
second_number = int(input("ingresa el segundo numero: "))

try:
  print(first_number / second_number)
except:
  print("esta operación no puede ser realizada.")

print("fin")