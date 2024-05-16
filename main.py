from Policlinica import Policlinica
from Medico import Medico
from Socio import Socio
from Especialidad import Especialidad
from ConsultaMedica import ConsultaMedica
import datetime

def alta_especialidad():
    while True:
        print("--------------------------------------")
        nombre = input("Ingrese el nombre de la especialidad: ")
        precio = input("Ingrese el precio asociado: ")
        
        
        if(type(nombre) != str or nombre == ""): 
            print("El nombre de la especialidad es incorrecto, ingréselo nuevamente")
            continue
        
        if(not precio.isdecimal()):
            print("El precio de la especialidad es incorrecto, ingréselo nuevamente")
            continue
        break
    print("La especialidad se ha creado con exito")
    Especialidad(nombre, precio)
    # print(Policlinica.especialidades)
    
def alta_socio():
    while True:
        print("--------------------------------------")
        nombre = input("\t- Ingrese el nombre: ")
        apellido = input("\t- Ingrese el apellido: ")
        ci = input("\t- Ingrese la cédula de identidad: ")
        fecha_nacimiento = input("\t- Ingrese la fecha de nacimiento en formato aaaa-mm-dd: ")
        fecha_ingreso = input("\t- Ingrese la fecha de ingreso a la institución en formato aaaa-mm-dd: ")
        celular = input("\t - Ingrese el número de celular: ")
        tipo = input("\t - Ingrese el tipo de socio(1-Bonificado, 2-No bonificado): ")
        
        if(type(nombre) != str or nombre == ""): 
            print("El nombre es incorrecto, ingréselo nuevamente")
            continue
        
        if(type(apellido) != str or apellido == ""): 
            print("El apellido es incorrecto, ingréselo nuevamente")
            continue
        
        if(not ci.isdecimal() or len(ci) != 8):
            print("No es una cédula válida, ingrese nuevamente una cédula de 8 digitos.")
        
        
        
    

if __name__ == "__main__":
    while True:
        print("---MENU---")
        print("\t1. Dar de alta una especialidad")
        print("\t2. Dar de alta un socio")
        print("\t3. Dar de alta un médico")
        print("\t4. Dar de alta una consulta médica")
        print("\t5. Emitir un ticket de consulta")
        print("\t6. Realizar consultas")
        print("\t7. Salir del programa")
        op = input("Seleccione una opción del menú:")
        
        match op:
            case "1":
                alta_especialidad()
            case "2":
                alta_socio()
            case "3":
                alta_medico()
            case "4":
                alta_consulta_medica()
            case "5":
                emitir_ticket()
            case "6":
                realizar_consulta()
            case "7":
                break
            case _:
                print("La opción seleccionada no es correcta, vuelva a intentar con otra opción.")
                
                

        
        
        
        