from Persona import Persona

class Socio(Persona):
    socios = []
    
    def __init__(self, nombre, apellido, ci, fecha_nacimiento, fecha_ingreso, celular, tipo):
        super().__init__(self, nombre, apellido, ci, fecha_nacimiento, fecha_ingreso, celular)
        self.tipo = tipo
        self.deuda = 0