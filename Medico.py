from Persona import Persona
from Policlinica import Policlinica

class Medico(Persona):
    def __init__(self, nombre, apellido, ci, fecha_nacimiento, fecha_ingreso, celular, especialidad):
        super().__init__(self, nombre, apellido, ci, fecha_nacimiento, fecha_ingreso, celular)
        self.especialidad = especialidad
        Policlinica.medicos.append((self.nombre, self.ci))