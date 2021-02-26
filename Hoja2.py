
print("Bienvenido!!")
altura = int(input("Ingrese un numero entero positivo para que sea la altura del triangulo : "))
if altura>0:
    for i in range(altura):
        for j in range(i+1):
            print("*", end="")
        print()
else:
    print("El numero no es entero positivo")

print("Numero Primo")
cualquiera=int(input("Ingrese un numero entero positivo: "))
a=0
if cualquiera>1:
    for i in range(2, cualquiera):
        n=cualquiera%i
        if n==0:
            a+=1
    if a== 0:
        print("El numero "+str(cualquiera)+" es primo")
    else:
        print("El numero " +str(cualquiera) + " no es primo")
else:
    print("No es un numero primo")