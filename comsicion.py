# En el contexto de una Universidad que contiene Departamentos. Cada Departamento tiene a su vez Profesores.
# Aquí, la clase Universidad está compuesta por varias instancias de Departamento, y la clase Departamento está compuesta por varias instancias de Profesor.

# + Si se destruye una instancia de la clase Universidad, se destruyen también los departamentos que contiene.
# + Si se destruye un departamento, también se destruyen los profesores que pertenecen a él.

class Profesor:
    def __init__(self, name, especialidad):
        self.name = name
        self.especialidad = especialidad

    def __str__(self):
        return f'Profesor {self.name}, especialidad: {self.especialidad}'

class Departamento:
    def __init__(self, nombre_departamento):
        self.nombre_departamento = nombre_departamento
        self.profesores = []

    def add_profesor(self, profesor):
        self.profesores.append(profesor)

    def show_profesores_list(self):
        print(f'Listado de profesores del departemento: ${self.nombre_departamento}')
        for profesor in self.profesores:
            print(profesor)




class Universidad:
    def __init__(self, nombre_universidad):
        self.nombre_universidad = nombre_universidad
        self.departamentos = []

    def agregar_departamento(self, departamento):
        self.departamentos.append(departamento)

    def show_departamentos_list(self):
        print(f'La universidad, {self.nombre_universidad}, tiene los siguentes departamentos')
        for dpto in self.departamentos:
            print(dpto.nombre_departamento)



#Crando profesores
prof1 = Profesor('Richar', 'Python')
prof2 = Profesor('Marcos', 'Javascript')
prof3 = Profesor('Mercedes', 'Psicologia')

# Creando los departamento
dpto_computacion = Departamento('Computación')
dpto_medicina = Departamento('Medicina')

dpto_medicina.add_profesor(prof3)
dpto_computacion.add_profesor(prof1)
dpto_computacion.add_profesor(prof2)

universidad_catolica = Universidad('Universidad Catolica')
universidad_catolica.agregar_departamento(dpto_medicina)
universidad_catolica.agregar_departamento(dpto_computacion)

universidad_catolica.show_departamentos_list()








