from entities.policlinica import Policlinica

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
                Policlinica.alta_especialidad()
            case "2":
                Policlinica.alta_socio()
            case "3":
                Policlinica.dar_alta_medico()
            case "4":
                Policlinica.alta_consulta_medica()
            case "5":
                Policlinica.emitir_ticket()
            case "6":
                Policlinica.realizar_consulta()
            case "7":
                break
            case _:
                print("La opción seleccionada no es correcta, vuelva a intentar con otra opción.")
                
                

        
        
        
        