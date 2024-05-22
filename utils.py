import datetime
from Policlinica import Policlinica

def verificar_string(string):
    if(type(string) != str or string == ""): 
        return True
    else:
        return False
    
def verificar_ci(ci):
    if(not ci.isdecimal() or len(ci) != 8):
        return True
    else:
        return False
    
def validar_fecha(fecha):
    try:
        datetime.date.fromisoformat(fecha)
        return True
    except:
        return False
    
def verificar_celular(cel):
    if(not cel.isdecimal() or len(cel) != 9 or cel[0:2] != "09"):
        return True
    else:
        return False
    
def verificar_especialidad(esp):
    if(not verificar_string(esp)):
        if (esp not in (especialidad[0] for especialidad in Policlinica.especialidades)):
            while True:
                print("Esta especialidad no está dada de alta elija un opción:")
                print("1 - Volver a ingresar la especialidad")
                print("2 - Dar de alta esta especialidad")
                op = input("Opcion: ")
                
                if(op == "1"):
                    return True
                elif(op == "2"):
                    return False
                else:
                    print("Opción inválida.")
                    continue
                
                
        
    