edad = 29
nombre = "Luis"
edad_legal = 18

if edad >= edad_legal:
    print(f"Felicidades {nombre} por tu mayoria de edad")
else:
    print(f"Hola {nombre}, aun eres menor de edad")
    print("chale")

i = 0
steps = 10
while(i < steps):
    i += 1
    print("running")

precios = [10,20,30,40]
total=0
for precio in precios:
    total += precio
print(f"Total: {total}")