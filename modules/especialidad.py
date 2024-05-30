class Especialidad():
    
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio
        self.medicos = []        
    
        
    def __str__(self):
        return (f"{self.nombre}, {self.precio}")