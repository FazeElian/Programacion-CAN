#Variables: Y definimos Variables. Ejemplo: Nombre_Cliente = str(input("Cuál es su nombre"))
Nombre_Cliente = str(input("Cuál es su nombre"))
Cuenta_Banco = int(input("Ingrese su número de Cuenta"))
Tipo_Cuenta = str(input("¿Qué tipo de cuenta tiene?"))


Operación_Banco = str(input("¿Qué operación desea realizar?"))

#Desarrollo:
print(Nombre_Cliente) #Imprimimos lo que dice en la variable "Nombre_Cliente"
print(Cuenta_Banco) #Imprimimos lo que dice en la variable "Cuenta_Banco"
print(Tipo_Cuenta) #Imprimimos lo que dice en la variable "Tipo_Cuenta"
if Tipo_Cuenta == "Corriente, Ahorros": #Preguntamos tipo de cuenta
    print(Operación_Banco), #Preguntamos que operación desea realizar
    if Operación_Banco == "Depósito":
        Depósito = int(input("¿Cuánto desea depositar en su cuenta?"))
        print(Depósito)and print(Nombre_Cliente + "Usted depositó:" + Depósito + "en su cuenta bancaria")
else:
    Retiro = int(input("¿Cuánto desea retirar de su cuenta?"))
    print(Retiro),
    print(Nombre_Cliente + "Usted retiró:" + Retiro + "de su cuenta bancaria")




