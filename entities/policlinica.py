from entities.especialidad import Especialidad
from entities.medico import Medico
from entities.socio import Socio
from entities.consultaMedica import ConsultaMedica
from entities.utils import Utils

class Policlinica:
    medicos = []
    socios = []
    consultas_medicas = []
    especialidades = []
    tickets_emitidos = []
    
    def verificar_especialidad(esp):
        if(all(x.isalpha() or x.isspace() for x in esp)):
            if (esp not in (especialidad.nombre for especialidad in Policlinica.especialidades)):
                while True:
                    print("Esta especialidad no está dada de alta elija un opción:")
                    print("1 - Volver a ingresar la especialidad")
                    print("2 - Dar de alta esta especialidad")
                    op = input("Opcion: ")
                    
                    if(op == "1"):
                        return 1
                    elif(op == "2"):
                        return 2
                    else: 
                        print("Opción inválida.")
                        continue
            else:
                return False
        else: 
            print("La especialidad debe ser un string")
            return True
        
    def verificar_esp_medico(esp,ci):
        for medico in Policlinica.medicos:
            if medico.ci==ci:
                if medico.especialidad == esp:
                    return False 
                    
    def verificar_medico(ci):
        if(ci not in (medicos.ci for medicos in Policlinica.medicos)):
                while True:
                    print("Este médico no está dado de alta, elija una opción:")
                    print("1 - Volver a ingresar médico") 
                    print("2 - Dar de alta el médico")
                    op= input("Opcion: ")

                    if (op=="1"):
                        return 1
                    if (op=="2") :
                        return 2
                    else:
                        print("Opción inválida.")
                        continue      
        else:
                return False
    def alta_especialidad():
        while True:
            print("--------------------------------------")
            nombre = input("Ingrese el nombre de la especialidad: ")
            precio = input("Ingrese el precio asociado: ")
            
            
            if(not all(x.isalpha() or x.isspace() for x in nombre)): 
                print("El nombre de la especialidad es incorrecto, ingréselo nuevamente")
                continue
            
            if(not precio.isdecimal()):
                print("El precio de la especialidad es incorrecto, ingréselo nuevamente")
                continue
            break
        Policlinica.especialidades.append(Especialidad(nombre, precio))
        print("La especialidad se ha creado con exito")
        print(Policlinica.especialidades[-1].nombre)
        lista1=Policlinica.especialidades
        for elemento in lista1:
            print(elemento)
        
    def dar_alta_medico():
        while True:
            print("--------------------------------------")
            nombre = input("\t- Ingrese el nombre: ")
            apellido = input("\t- Ingrese el apellido: ")
            ci = input("\t- Ingrese la cédula de identidad: ")
            fecha_nacimiento = input("\t- Ingrese la fecha de nacimiento en formato aaaa-mm-dd: ")
            fecha_ingreso = input("\t- Ingrese la fecha de ingreso a la institución en formato aaaa-mm-dd: ")
            celular = input("\t - Ingrese el número de celular: ")
            especialidad = input("\t - Ingrese la especialidad: ")
            
            if(not nombre.isalpha()): 
                print("No es un nombre válido, ingréselo nuevamente")
                continue
            
            if(not apellido.isalpha()): 
                print("No es un apellido válido, ingréselo nuevamente")
                continue
            
            if(Utils.verificar_ci(ci)):
                print("No es una cédula válida, ingrese nuevamente una cédula de 8 dígitos.")
                continue
                
            if(Utils.validar_fecha(fecha_nacimiento) or Utils.validar_fecha(fecha_ingreso)):
                print("No es una fecha válida, vuelva a ingresarla en el formato aaaa-mm-dd.")
                continue
                
            if(Utils.verificar_celular(celular)):
                print("No es un número de celular válido, ingrese un número con el formato 09XXXXXXX")
                continue
            
            if(Policlinica.verificar_especialidad(especialidad) == 1):
                continue
            elif(Policlinica.verificar_especialidad(especialidad) == 2):
                Policlinica.alta_especialidad()
            break
        
        for esp in Policlinica.especialidades:
            if esp.nombre == especialidad:
                especialidad = esp
                
        Policlinica.medicos.append(Medico(nombre, apellido, ci, fecha_nacimiento, fecha_ingreso, celular, especialidad))
        print("El médico se ha agregado exitosamente.")
        print(Policlinica.medicos)
        
    def alta_socio():
        while True:
            print("--------------------------------------")
            nombre = input("\t- Ingrese el nombre: ")
            apellido = input("\t- Ingrese el apellido: ")
            ci = input("\t- Ingrese la cédula de identidad: ")
            fecha_nacimiento = input("\t- Ingrese la fecha de nacimiento en formato aaaa-mm-dd: ")
            fecha_ingreso = input("\t- Ingrese la fecha de ingreso a la institución en formato aaaa-mm-dd: ")
            celular = input("\t- Ingrese el número de celular: ")
            tipo = input("\t- Ingrese el tipo de socio(1-Bonificado, 2-No bonificado): ")
            
            if(not nombre.isalpha()): 
                print("El nombre es incorrecto, ingréselo nuevamente")
                continue
            
            if(not apellido.isalpha()): 
                print("El apellido es incorrecto, ingréselo nuevamente")
                continue
            
            if(Utils.verificar_ci(ci)):
                print("No es una cédula válida, ingrese nuevamente una cédula de 8 digitos.")
                continue
                
            if(Utils.validar_fecha(fecha_nacimiento) or Utils.validar_fecha(fecha_ingreso)):
                print("No es una fecha válida, vuelva a ingresarla en el formato aaaa-mm-dd.")
                continue
            
            if(Utils.verificar_celular(celular)):
                print("No es un número de celular válido, ingrese un número con el formato 09XXXXXXX")
                continue
                
            if(tipo == "1"):
                tipo = True
            elif(tipo == "2"):
                tipo = False
            else:
                print("El valor ingresado no es correcto, elige la opción 1 o 2")
                continue
            break
                
        Policlinica.socios.append(Socio(nombre, apellido, ci, fecha_nacimiento, fecha_ingreso, celular, tipo))
        print("El socio se ha creado con exito.")
        
    def alta_consulta_medica():
        while True:
            print("--------------------------------------")
            especialidad = input("\t - Ingrese la especialidad: ")
            nombre = input("\t- Ingrese el nombre del médico: ")
            apellido=input("\t- Ingrese el apellido del médico: ")
            fecha_consulta = input("\t- Ingrese la fecha de consulta en formato aaaa-mm-dd: ")
            cant_pacientes=input("\t- Ingrese la cantidad de pacientes que se atenderán: ")
            
            
            if(not nombre.isalpha()): 
                print("El nombre es incorrecto, ingréselo nuevamente")
                continue
            
            if(not apellido.isalpha()): 
                print("El apellido es incorrecto, ingréselo nuevamente")
                continue
            
            if(Utils.validar_fecha(fecha_consulta)):
                print("No es una fecha válida, vuelva a ingresarla en el formato aaaa-mm-dd.")
                continue
                
            if(Policlinica.verificar_especialidad(especialidad) == 1):
                continue
            elif(Policlinica.verificar_especialidad(especialidad) == 2):
                Policlinica.alta_especialidad()
                continue

            if (Policlinica.verificar_medico(medico))==1:
                continue
            elif (Policlinica.verificar_medico(medico))==2:
                Policlinica.dar_alta_medico()
                continue

            if(Utils.verificar_esp_medico(especialidad,nombre,apellido)):
                continue
            break
        
        for medico in Policlinica.medicos:
            if medico.nombre==nombre:
                if medico.apellido==apellido:
                    medico1 = medico
                
        for especialidad in Policlinica.especialidades:
            if especialidad.nombre == especialidad:
                especialidad1 = especialidad
        
        Policlinica.consultas_medicas.append(ConsultaMedica(fecha_consulta, especialidad1, medico1, cant_pacientes))

    def emitir_ticket():
        # En emitir ticket no deberia de pedir la info del sopcio?
        # En emitir ticket no deberia de cambiar la deuda del socio
        while True:
            print("--------------------------------------")
            especialidad=input("Ingrese la especialidad: ")
            socio_ci = input("Ingrese su cédula, sin puntos ni guión: ")
            
            if(Especialidad.verificar_especialidad(especialidad)):
                continue
            else:
                Especialidad.alta_especialidad()
               
            ops = []
            while True:
                for i, consulta in enumerate(Policlinica.consultas_medicas):
                    if consulta.especialidad.nombre==especialidad:
                        if len(consulta.cant_pacientes) == 0: continue
                        
                        medico_nombre = consulta.medico.nombre
                        medico_apellido = consulta.medico.apellido
                        fecha_consulta = consulta.fecha_consulta
                        
                        ops.append((i, consulta))
                        
                        print(f"{i} - Doctor: {medico_nombre} {medico_apellido} Día de la consulta: {fecha_consulta}")
                    else: continue
                op = input("Seleccione la opción deseada: ")
            
                if op in [ops[i][0] for i in range(len(ops))]:
                    for num in consulta.cant_pacientes:
                        print(f" - {num}")
                else:
                    print(f"La opción ingresada no es una opción válida debe ser un número entre 1 y {len(ops)}")
                    continue
                    
                
                op1 = input("Seleccione el número de atención deseado: ")
                if op1 in consulta.cant_pacientes:
                    consulta.cant_pacientes.pop(op1)
                    print("Ticket Emitido")
                else:
                    print(f"No es un número de consulta válido, los números válidos son: {", ".join(str(x) for x in consulta.cant_pacientes)}")
                

                
        
                
        