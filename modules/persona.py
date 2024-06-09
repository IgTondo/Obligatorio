from abc import ABC

class Persona(ABC):
    def __init__(self, nombre, apellido, ci, fecha_nacimiento, fecha_ingreso, celular):
        self.nombre = nombre
        self.apellido = apellido
        self.ci = ci
        self.fecha_nacimiento = fecha_nacimiento
        self.fecha_ingreso = fecha_ingreso
        self.celular = celular