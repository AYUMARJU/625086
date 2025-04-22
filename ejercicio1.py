##Declarar variables##
#nombre = input("¿Cual es tu nombre?")
edad = int(input("¡cual es tu edad?"))
#print(f"Hola {nombre}! Tienes {edad} años")

#def saludar(nombre):
# print(f"Hola{nombre}! Bienvenid@ al taller")
#saludar(nombre)

#for recorrer in range(1,10):
 #print(recorrer)

def esMayorDeEdad(edad):
    if edad >= 18:
       return "Eres mayor de edad" 
    else:
        return "Eres menor de edad" 
print(esMayorDeEdad(edad))       


