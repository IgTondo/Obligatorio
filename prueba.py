class excepcion(Exception):
    def __init__(self, mensaje):
        self.mensaje = mensaje
        
    def __str__(self):
        return self.mensaje
    
raise excepcion("Error de prueba")

print("Hola")