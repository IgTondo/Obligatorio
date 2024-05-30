import datetime
# from entities.policlinica import Policlinica

class Utils:    
            
    def verificar_string(string):
        if(not all(x.isalpha() or x.isspace() for x in string)):
            return False
        else: return True

    def verificar_ci(ci):
        if(not ci.isdecimal() or len(ci) != 8):
            return True
        else:
            return False
        
    def verificar_cant(cantidad_pacientes):
        if (not cantidad_pacientes.isdecimal()):
            return True
        else:
            return False
        
    def validar_fecha(fecha):
        try:
            datetime.date.fromisoformat(fecha)
            return False
        except:
            return True
        
    def verificar_celular(cel):
        if(not cel.isdecimal() or len(cel) != 9 or cel[0:2] != "09"):
            return True
        else:
            return False
        
    def fecha_consulta(fecha):
        if(fecha < str(datetime.datetime.now())): 
            return True
        else: 
            return False
        

        
        #cambiar nombre y apellido a cedula

            
                
        #verificar fecha de la consulta no vencida
                    