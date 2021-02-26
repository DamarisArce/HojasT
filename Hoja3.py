# ejercicio 1
print('Bienvenido Usuario ')
nombre = input(print('Ingrese un nombre '))
contraseña = input(print('Ingrese contraseña nueva: '))
confirme = input(print('Ingresa nuevamente la contraseña '))
if contraseña == confirme:
    print('la contraseña a sido guardada exitosamente')
else:
    print('La contraseña no coincide')

# ejercicio 2

genero = input(print('Ingrese su genero: '))
if genero == 'M':
    if nombre.lower() > 'm': 
       print ('Estas asignado al grupo A')
    else:
         print ('Estas asignado al grupo B') 
else:
    if nombre.lower() < 'n':
         print('Estas asignado al grupo A')    
    else: 
       print ('Estas asignado al grupo B')  
