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
                if medico.especialidad.nombre == esp:
                    return False 
                else: return True
                    
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
        print("--------------------------------------")
        while True:
            nombre = input("Ingrese el nombre de la especialidad: ")
            if(not all(x.isalpha() or x.isspace() for x in nombre)): 
                print("El nombre de la especialidad es incorrecto,ingréselo nuevamente")
                continue
            break
            
        while True:
            precio = input("Ingrese el precio asociado: ")
            if(not precio.isdecimal()):
                print("El precio de la especialidad es incorrecto,ingréselo nuevamente")
                continue
            break 

        Policlinica.especialidades.append(Especialidad(nombre, precio))
        print("La especialidad se ha creado con exito")
        for especialidad in Policlinica.especialidades:
            print(especialidad)
        
    def dar_alta_medico():
        print("--------------------------------------")
        while True:
            nombre = input("\t- Ingrese el nombre: ")
            if(not all(x.isalpha() or x.isspace() for x in nombre)): 
                print("No es un nombre válido ingreselo nuevamente.")
                continue
            break
        
        while True:
            apellido = input("\t- Ingrese el apellido: ")
            if(not all(x.isalpha() or x.isspace() for x in apellido)): 
                print("No es un apellido válido, ingreselo nuevamente.")
                continue
            break
        
        while True:
            ci = input("\t- Ingrese la cédula de identidad: ")
            if(Utils.verificar_ci(ci)):
                print("No es una cédula válida, ingrese nuevamente una cédula de 8 dígitos.")
                continue
            break
        
        while True:
            fecha_nacimiento = input("\t- Ingrese la fecha de nacimiento en formato aaaa-mm-dd: ")
            if(Utils.validar_fecha(fecha_nacimiento)):
                print("No es una fecha válida, vuelva a ingresarla en el formato aaaa-mm-dd.")
                continue
            break
        
        while True:
            fecha_ingreso = input("\t- Ingrese la fecha de ingreso a la institución en formato aaaa-mm-dd: ")
            if(Utils.validar_fecha(fecha_ingreso)):
                print("No es una fecha válida, vuelva a ingresarla en el formato aaaa-mm-dd.")
                continue
            break
        
        
        while True:
            celular = input("\t - Ingrese el número de celular: ")
            if(Utils.verificar_celular(celular)):
                print("No es un número de celular válido, ingrese un número con el formato 09XXXXXXX")
                continue
            break
        
        while True:
            especialidad = input("\t - Ingrese la especialidad: ")
            if(Policlinica.verificar_especialidad(especialidad) == 1):
                continue
            elif(Policlinica.verificar_especialidad(especialidad) == 2):
                Policlinica.alta_especialidad()
            else: break            
        
        for esp in Policlinica.especialidades:
            if esp.nombre == especialidad:
                especialidad = esp
                
        Policlinica.medicos.append(Medico(nombre, apellido, ci, fecha_nacimiento, fecha_ingreso, celular, especialidad))
        print("El médico se ha agregado exitosamente.")
        for medico in Policlinica.medicos:
            print(medico)


    def alta_socio():
        # while True:
        print("--------------------------------------")
        while True:
            nombre = input("\t- Ingrese el nombre: ")
            if(not all(x.isalpha() or x.isspace() for x in nombre)): 
                print("No es un nombre válido,ingréselo nuevamente")
                continue
            break

        while True:
            apellido = input("\t- Ingrese el apellido: ")
            if(not all(x.isalpha() or x.isspace() for x in apellido)): 
                print("No es un apellido válido,ingréselo nuevamente")
                continue
            break
        while True:
            ci = input("\t- Ingrese la cédula de identidad: ")
            if(Utils.verificar_ci(ci)):
                print("No es una cédula válida, ingrese nuevamente una cédula de 8 digitos.")
                continue            
            break
        while True:
            fecha_nacimiento = input("\t- Ingrese la fecha de nacimiento en formato aaaa-mm-dd: ")
            if(Utils.validar_fecha(fecha_nacimiento)):
                print("No es una fecha válida, vuelva a ingresarla en el formato aaaa-mm-dd.")
                continue
            break

        while True:
            fecha_ingreso = input("\t- Ingrese la fecha de ingreso a la institución en formato aaaa-mm-dd: ")
            if(Utils.validar_fecha(fecha_ingreso)):
                print("No es una fecha válida, vuelva a ingresarla en el formato aaaa-mm-dd.")
                continue
            break
        
        while True:
            celular = input("\t- Ingrese el número de celular: ")
            if(Utils.verificar_celular(celular)):
                print("No es un número de celular válido, ingrese un número con el formato 09XXXXXXX")
                continue
            break

        while True:
            tipo = input("\t- Ingrese el tipo de socio(1-Bonificado, 2-No bonificado): ")
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
        for socio in Policlinica.socios:
            print(socio)
        
    def alta_consulta_medica():
            print("--------------------------------------")
            while True:
                especialidad = input("\t - Ingrese la especialidad: ")
                res = Policlinica.verificar_especialidad(especialidad)
                if(res == 1):
                    continue
                elif(res == 2):
                    Policlinica.alta_especialidad()
                break
            
            while True:
                ci = input("\t- Ingrese la cedula del médico: ")
                if(Utils.verificar_ci(ci)):
                    print("No es una cédula válida, ingrese nuevamente una cédula de 8 digitos.")
                    continue 
                res = Policlinica.verificar_medico(medico)
                if res == 1:
                    continue
                elif res == 2:
                    Policlinica.dar_alta_medico()  
                    
                if(Policlinica.verificar_esp_medico(especialidad,ci)):
                    continue        
                break

            while True:
                fecha_consulta = input("\t- Ingrese la fecha de la consulta en formato aaaa-mm-dd: ")
                if(Utils.validar_fecha(fecha_consulta)):
                    print("No es una fecha válida, vuelva a ingresarla en el formato aaaa-mm-dd.")
                    continue
                break

            while True:
                cant_pacientes=input("\t- Ingrese la cantidad de pacientes que se atenderán: ")
                if (Utils.verificar_cant(cant_pacientes)):
                    print("La cantidad de pacientes debe de ser un numero, ingreselo de nuevo")
                    continue
                break  
            
            for medico in Policlinica.medicos:
                if medico.ci == ci:
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
                

                
        
                
        