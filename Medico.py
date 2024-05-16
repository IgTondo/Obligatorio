from Persona import Persona
from Policlinica import Policlinica

class Medico(Persona):
    def __init__(self, nombre, apellido, ci, fecha_nacimiento, fecha_ingreso, celular):
        super().__init__(self, nombre, apellido, ci, fecha_nacimiento, fecha_ingreso, celular)