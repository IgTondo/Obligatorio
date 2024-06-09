from modules.especialidad import Especialidad
from modules.medico import Medico
from modules.socio import Socio
from modules.consultamedica import ConsultaMedica
from modules.utils import Utils
from exceptions.excepcionOpcionInvalida import ExcepcionOpcionInvalida

class Policlinica:
    
    def __init__(self):
        self.medicos = []
        self.socios = []
        self.consultas_medicas = []
        self.especialidades = []
    
    
    def verificar_especialidad(self, esp):
        if(Utils.verificar_string(esp)):
            print("La especialidad debe ser un string")
            return True
        if (esp not in (especialidad.nombre for especialidad in self.especialidades)):
            while True:
                try:
                    print("Esta especialidad no está dada de alta elija un opción:")
                    print("1 - Volver a ingresar la especialidad")
                    print("2 - Dar de alta esta especialidad")
                    op = input("Opcion: ")
                        
                    if(op == "1"):
                        return 1
                    elif(op == "2"):
                        return 2
                    else:
                        raise ExcepcionOpcionInvalida("Opción inválida.")
                except ExcepcionOpcionInvalida as e:
                    print(e)
                    continue
        else:
            return False
            
        
    def verificar_consultas_con_especialidad(self, especialidad):
        for medico in self.medicos:
            if(medico.especialidad.nombre != especialidad or medico.consultas_medicas == []):
                continue
            else:
                for consulta in medico.consultas_medicas:
                    if(Utils.fecha_consulta(consulta.fecha)):
                        continue
                    else:
                        return False
        return True
                          
        
    def verificar_esp_medico(self,esp,nombre,apellido):
        for medico in self.medicos:
            if medico.nombre==nombre and medico.apellido==apellido:
                if medico.especialidad.nombre == esp:
                    return False 
                else: 
                    print("El médico elegido no tiene esta especialidad. Ingrese otro médico")
                    return True
                    
    def verificar_medico(self, nombre, apellido):
        if(nombre in (medicos.nombre for medicos in self.medicos)):
            if(apellido in (medicos.apellido for medicos in self.medicos)):
                return False
        while True:
            try:
                print("Este médico no está dado de alta, elija una opción:")
                print("1 - Volver a ingresar médico") 
                print("2 - Dar de alta el médico")
                op = input("Opcion: ")
                        
                if(op == "1"):
                    return 1
                elif(op == "2"):
                    return 2
                else:
                    raise ExcepcionOpcionInvalida("Opción inválida.")
            except ExcepcionOpcionInvalida as e:
                print(e)
                continue
        
    def verificar_socio(self, socio_ci):
        if(socio_ci not in [socios.ci for socios in self.socios]):
            while True:
                try:
                    print("Este socio no está dado de alta, eliga una opción: ")
                    print("1 - Volver a ingresar el socio") 
                    print("2 - Dar de alta el socio ")
                    op = input("Opcion: ")
                        
                    if(op == "1"):
                        return 1
                    elif(op == "2"):
                        return 2
                    else:
                        raise ExcepcionOpcionInvalida("Opción inválida.")
                except ExcepcionOpcionInvalida as e:
                    print(e)
                    continue
        else:
                return False

    def alta_especialidad(self):
        print("--------------------------------------")
        while True:
            nombre = input("Ingrese el nombre de la especialidad: ")
            if(Utils.verificar_string(nombre)): 
                print("El nombre de la especialidad es incorrecto,ingréselo nuevamente")
                continue
            break
            
        while True:
            precio = input("Ingrese el precio asociado: ")
            if(not precio.isdecimal()):
                print("El precio de la especialidad es incorrecto,ingréselo nuevamente")
                continue
            break 

        self.especialidades.append(Especialidad(nombre, int(precio)))
        print("La especialidad se ha creado con exito")
        for especialidad in self.especialidades:
            print(especialidad)
        
    def dar_alta_medico(self):
        print("--------------------------------------")
        while True:
            nombre = input("\t- Ingrese el nombre: ")
            if(Utils.verificar_string(nombre)):
                print("No es un nombre válido ingreselo nuevamente.")
                continue
            break
        
        while True:
            apellido = input("\t- Ingrese el apellido: ")
            if(Utils.verificar_string(apellido)): 
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
            celular = input("\t- Ingrese el número de celular: ")
            if(Utils.verificar_celular(celular)):
                print("No es un número de celular válido, ingrese un número con el formato 09XXXXXXX")
                continue
            break
        
        while True:
            especialidad = input("\t- Ingrese la especialidad: ")
            res= self.verificar_especialidad(especialidad)
            if(res == 1):
                continue
            elif(res == 2):
                self.alta_especialidad()
            else: 
                break            
        
        for esp in self.especialidades:
            if esp.nombre == especialidad:
                especialidad = esp
                
        self.medicos.append(Medico(nombre, apellido, ci, fecha_nacimiento, fecha_ingreso, celular, especialidad))
        print("El médico se ha agregado exitosamente.")
        for medico in self.medicos:
            print(medico)


    def alta_socio(self):
        # while True:
        print("--------------------------------------")
        while True:
            nombre = input("\t- Ingrese el nombre: ")
            if(Utils.verificar_string(nombre)): 
                print("No es un nombre válido,ingréselo nuevamente")
                continue
            break

        while True:
            apellido = input("\t- Ingrese el apellido: ")
            if(Utils.verificar_string(apellido)): 
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
                
        self.socios.append(Socio(nombre, apellido, ci, fecha_nacimiento, fecha_ingreso, celular, tipo))
        print("El socio se ha creado con exito.")
        for socio in self.socios:
            print(socio)
        
    def alta_consulta_medica(self):
        print("--------------------------------------")
        while True:
            especialidad = input("\t- Ingrese la especialidad: ")
            res = self.verificar_especialidad(especialidad)
            if(res == 1):
                continue
            elif(res == 2):
                self.alta_especialidad()
            break
        
        while True:
            nombreCompleto = input("\t- Ingrese el nombre completo: ")
            if(Utils.verificar_string(nombreCompleto)): 
                print("No es un nombre válido,ingréselo nuevamente")
                continue
            nombre = nombreCompleto.split()[0]
            apellido = nombreCompleto.split()[1]
            res = self.verificar_medico(nombre,apellido)
            if res == 1:
                continue
            elif res == 2:
                self.dar_alta_medico()  
                
            if(self.verificar_esp_medico(especialidad,nombre,apellido)):
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
        
        for medico in self.medicos:
            if medico.nombre == nombre and medico.apellido == apellido:
                medico1 = medico
           
        for especialidadEnLista in self.especialidades:
            if especialidadEnLista.nombre == especialidad:
                especialidad = especialidadEnLista
    
        consulta_medica = ConsultaMedica(fecha_consulta, especialidad, medico1, int(cant_pacientes))
        self.consultas_medicas.append(consulta_medica)
        medico1.consultas_medicas.append(consulta_medica)
        print(consulta_medica)
        
        
    def emitir_ticket(self):
            print("--------------------------------------")
            while True:
                especialidad = input("\t- Ingrese la especialidad: ")
                res = self.verificar_especialidad(especialidad)
                if(res == 1):
                    continue
                elif(res == 2):
                    self.alta_especialidad()
                
                if(self.verificar_consultas_con_especialidad(especialidad)):
                    print("La especialidad elegida no tiene consultas disponibles, ingrese otra.")
                    continue
                break
            
            while True:
                ops = []
                cont = 0
                for consulta in self.consultas_medicas:
                    if consulta.especialidad.nombre!=especialidad:
                        continue
                    if len(consulta.cant_pacientes) == 0: continue
                    if (Utils.fecha_consulta(consulta.fecha)): continue
                    
                    medico_nombre = consulta.medico.nombre
                    medico_apellido = consulta.medico.apellido
                    fecha_consulta = consulta.fecha
                    
                    print(f"{cont+1} - Doctor: {medico_nombre} {medico_apellido}, Día de la consulta: {fecha_consulta}")
                    cont += 1
                    
                    ops.append((str(cont), consulta))
                    
                op = input("Seleccione la opción deseada: ")
            
                if op not in [ops[i][0] for i in range(len(ops))]:
                    print(f"La opción ingresada no es una opción válida debe ser un número entre 1 y {len(ops)}")
                    continue
                break
            
            while True:       
                for num in consulta.cant_pacientes:
                        print(f"- {num}")
                        
                op1 = input("Seleccione el número de atención deseado: ")
                if op1 not in consulta.cant_pacientes:
                    print(f"No es un número de consulta válido, los números válidos son: {", ".join(str(x) for x in consulta.cant_pacientes)}")
                    continue
                
                break
                
            
            while True:    
                socio_ci = input("Ingrese su cédula, sin puntos ni guión: ")
                res=self.verificar_socio(socio_ci)
                if(res == 1):
                    continue
                elif(res == 2):
                    self.alta_socio()
                else: 
                    break 
                
            consulta.cant_pacientes.remove(op1)
            print("Ticket Emitido")
            for s in self.socios:
                if s.ci==socio_ci:
                    socio=s
            for e in self.especialidades:
                if e.nombre==especialidad:
                    especialidad=e
            consulta.socios.append(socio)
            if socio.tipo:
                socio.deuda+= especialidad.precio*0.8
            else:
                socio.deuda+= especialidad.precio
            
            
            
    def realizar_consulta(self):
        print("""
              \t1. Obtener todos los médicos asociados a una especialidad específica. 
              \t2. Obtener el precio de una consulta de una especialidad en específico.  
              \t3. Listar todos los socios con sus deudas asociadas en orden ascendente. 
              \t4. Realizar consultas respecto a cantidad de consultas entre dos fechas 
              \t5. Realizar consultas respecto a las ganancias obtenidas entre dos fechas. """)            
        while True:
            op = input("Seleccionar opción:")
            match op:
                case "1":
                    self.medicos_con_especialidad()
                case "2":
                    self.precio_consulta()
                case "3":
                    self.listar_deudas()
                case "4":
                    self.cantidad_consultas()
                case "5":
                    self.ganancias()
                case _:
                    print("La opción no es válida, ingresela de nuevo.")
                    continue
            break
               
            

    def medicos_con_especialidad(self):
        var = False
        while True:
            especialidad=input("Insertar la especialidad:")
            res = self.verificar_especialidad(especialidad)
            if(res == 1):
                continue
            elif(res == 2):
                self.alta_especialidad()
            if self.medicos!=[]:
                for medico in self.medicos:
                    if medico.especialidad.nombre==especialidad:
                        print(f"{medico.nombre}, {medico.apellido}")
                        var = True
                if(var):
                    break

            print("No existe ningun medico con esta especialidad")
            print("1- Ingresar otra especialidad:")
            print("2- Salir")
            op=input("Seleccione la opción deseada:")
            if op=="1":
                continue
            break

    def precio_consulta(self):
        while True:
            especialidad=input("Insertar la especialidad:")
            res = self.verificar_especialidad(especialidad)
            if(res == 1):
                continue
            elif(res == 2):
                self.alta_especialidad()

            for e in self.especialidades:
                if e.nombre==especialidad:
                    print(f"{e.precio}")
            break
        
    #Listar todos los socios con sus deudas asociadas en orden ascendente. 
    def listar_deudas(self):
        if self.socios==[]:
            print("No hay ningún socio insertado")
            return
        for i in range(len(self.socios)):
            for j in range(len(self.socios)):
                if self.socios[i].deuda < self.socios[j].deuda:
                    self.socios[i],self.socios[j]=self.socios[j],self.socios[i]                 
        for socio in self.socios:
            print(f"{socio.nombre} {socio.apellido}, {socio.deuda}")
        

    #Realizar consultas respecto a cantidad de consultas entre dos fechas 
    def cantidad_consultas(self):
        while True:
            fecha1=input("Insertar la fecha 1:")
            if(Utils.validar_fecha(fecha1)):
                print("No es una fecha válida, vuelva a ingresarla en el formato aaaa-mm-dd.")
                continue
            break
        while True:
            fecha2=input("Insertar la fecha 2:")
            if(Utils.validar_fecha(fecha2)):
                print("No es una fecha válida, vuelva a ingresarla en el formato aaaa-mm-dd.")
                continue
            break
        cont=0
        for consulta in self.consultas_medicas:
            if consulta.fecha>fecha1 and consulta.fecha<fecha2:
                cont+=1
        print(f"La cantidad de consultas entre las fechas {fecha1} y {fecha2} es de {cont}")

#Realizar consultas respecto a las ganancias obtenidas entre dos fechas
    def ganancias(self):
        ganancia = 0
        while True:
            fecha1=input("Insertar la fecha 1:")
            if(Utils.validar_fecha(fecha1)):
                print("No es una fecha válida, vuelva a ingresarla en el formato aaaa-mm-dd.")
                continue
            break
        while True:
            fecha2=input("Insertar la fecha 2:")
            if(Utils.validar_fecha(fecha2)):
                print("No es una fecha válida, vuelva a ingresarla en el formato aaaa-mm-dd.")
                continue
            break
        for consulta in self.consultas_medicas:
            if consulta.fecha>fecha1 and consulta.fecha<fecha2:
                precio = consulta.especialidad.precio
                for socio in consulta.socios:
                    if socio.tipo:
                        ganancia += precio*0.8
                    else:
                        ganancia += precio
            break
        print(f"La ganancia entre las fechas {fecha1} y {fecha2} es de {ganancia}")

        #get-content correct_flow.txt | python main.py