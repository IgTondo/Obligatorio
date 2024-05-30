from modules.persona import Persona

class Medico(Persona):
    def __init__(self, nombre, apellido, ci, fecha_nacimiento, fecha_ingreso, celular, especialidad):
        super().__init__(nombre, apellido, ci, fecha_nacimiento, fecha_ingreso, celular)
        self.especialidad = especialidad
        self.consultas_medicas = []
        
    def __str__(self):
        return (f"{self.nombre}, {self.apellido}, {self.especialidad.nombre}")
        
    