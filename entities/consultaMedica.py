class ConsultaMedica():
    def __init__(self,fecha,especialidad,medico,cant_pacientes = 1):
        self.fecha = fecha
        self.especialidad=especialidad
        self.medico = medico
        self.cant_pacientes = [i for i in range(1, cant_pacientes+1)]
        self.socios = []
        
    
        
    