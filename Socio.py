from Persona import Persona
from Policlinica import Policlinica

class Socio(Persona):
    
    def __init__(self, nombre, apellido, ci, fecha_nacimiento, fecha_ingreso, celular, tipo):
        super().__init__(self, nombre, apellido, ci, fecha_nacimiento, fecha_ingreso, celular)
        self.tipo = tipo
        self.deuda = 0
        Policlinica.socios.append((self.nombre, self.ci))