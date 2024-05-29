import datetime
# from entities.policlinica import Policlinica

class Utils:    

    def verificar_ci(ci):
        if(not ci.isdecimal() or len(ci) != 8):
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
        

        
        #cambiar nombre y apellido a cedula

            
                
        #verificar fecha de la consulta no vencida
                    