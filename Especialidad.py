from Policlinica import Policlinica
class Especialidad():
    
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio
        Policlinica.especialidades.append((self.nombre, self.precio))
        
    def __str__(self):
        print([self.nombre, self.precio])