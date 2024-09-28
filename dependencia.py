# Ejemplo

# En el contexto de una Clínica y Pacientes. La clase Clínica depende de la clase Paciente para poder registrar y gestionar citas médicas.
# Sin embargo, la clínica no almacena a los pacientes de manera permanente;
# simplemente interactúa con ellos temporalmente al momento de gestionar una cita.

class Paciente:
    def __init__(self, nombre, edad, motivo_consulta):
        self.nombre = nombre
        self.edad = edad
        self.motivo_consulta = motivo_consulta

    def __str__(self):
        return f'Paciente: {self.nombre}, Edad: {self.edad}, Motivo: {self.motivo_consulta}'

    def update_motivo(self, nuevo_motivo):
        self.motivo_consulta = nuevo_motivo
        print(f'El motivo de la consulta de: {self.nombre}, ha cambiado a: {self.motivo_consulta}')

class Clinica:
    def __init__(self, nombre_clinica):
        self.nombre_clinica = nombre_clinica

    def registrar_cita(self, paciente):
        print(f'registrando cita en la clinica: {self.nombre_clinica} para:')
        print(paciente)
        print(f'La cita se registrp con exito para: {paciente.nombre}')

    def atender_cita(self, paciente):
        print(f'Atendiendo a {paciente.nombre} en al clinica {self.nombre_clinica}')
        print(f'Por el motivo de: {paciente.motivo_consulta}')

        paciente.update_motivo('Revision General')
        print(f'El paciente {paciente.nombre} se atendio con exito')


paciente1 = Paciente('Richar', 48, 'Vertigo')
paciente2 = Paciente('Marcos', 30, 'Gripe')

clinica_lascondes = Clinica('Clinica las condes')

clinica_lascondes.registrar_cita(paciente1)
clinica_lascondes.registrar_cita(paciente2)

clinica_lascondes.atender_cita(paciente1)
clinica_lascondes.atender_cita(paciente2)
