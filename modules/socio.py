from modules.persona import Persona

class Socio(Persona):
    
    def __init__(self, nombre, apellido, ci, fecha_nacimiento, fecha_ingreso, celular, tipo):
        super().__init__(nombre, apellido, ci, fecha_nacimiento, fecha_ingreso, celular)
        self.tipo = tipo
        self.deuda = 0
        self.consultas_medicas = []
        
    def __str__(self):
        return (f"{self.nombre}, {self.apellido}")
    