from entities.persona import Persona

class Socio(Persona):
    
    def __init__(self, nombre, apellido, ci, fecha_nacimiento, fecha_ingreso, celular, tipo):
        super().__init__(nombre, apellido, ci, fecha_nacimiento, fecha_ingreso, celular)
        self.tipo = tipo
        self.deuda = 0
        
    def __str__(self):
        print([self.nombre, self.apellido])
        
    