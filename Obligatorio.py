from abc import ABC, abstractmethod

class Policlinica:
    def dar_alta_medico():
        pass
    
    def dar_alta_consulta():
        pass
    
    def emitir_ticket():
        pass
    
    def realizar_consulta():
        pass

class Persona(ABC):
    def __init__(self, nombre, apellido, ci, fecha_nacimiento, fecha_ingreso, celular):
        self.nombre = nombre
        self.apellido = apellido
        self.ci = ci
        self.fecha_nacimiento = fecha_nacimiento
        self.fecha_ingreso = fecha_ingreso

class Socio(Persona):
    socios = []
    
    def __init__(self, nombre, apellido, ci, fecha_nacimiento, fecha_ingreso, celular, tipo):
        super().__init__(self, nombre, apellido, ci, fecha_nacimiento, fecha_ingreso, celular)
        self.tipo = tipo
        self.deuda = 0
        

class Medico(Persona):
    medicos = []
    
    def __init__(self, nombre, apellido, ci, fecha_nacimiento, fecha_ingreso, celular, tipo):
        super().__init__(self, nombre, apellido, ci, fecha_nacimiento, fecha_ingreso, celular)
        

class Especialidad():
    especialidades = []
    
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

class ConsultaMedica():
    pass