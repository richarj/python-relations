# Ejemplo:

# Vamos a modelar una relación de asociación entre un Profesor y un Curso.
# Un Profesor puede enseñar múltiples cursos, y un Curso puede tener múltiples profesores asignados.
# Los Profesores y Cursos existen independientemente, pero están asociados entre sí.

class Profesor:
    def __init__(self, nombre):
        self.nombre = nombre
        self.cursos = []

    def asignar_curso(self, curso):
        self.cursos.append(curso)

    def mostar_cursos(self):
        if self.cursos:
            print(f'El profesor {self.nombre} enseña los siguientes cursos')
            for curso in self.cursos:
                print(curso.nombre_curso)
        else:
            print(f'El profesor {self.nombre} no tiene cursos asignados')


class Curso:
    def __init__(self, nombre_curso):
        self.nombre_curso = nombre_curso
        self.profesores = []

    def asignar_profesor(self, profesor):
        self.profesores.append(profesor)

    def mostar_profesores(self):
        if self.profesores:
            print(f'El curso {self.nombre_curso} tiene los siguientes profesores')
            for profesor in self.profesores:
                print(profesor.nombre)
        else:
            print(f'El curso {self.nombre_curso} no tiene profesores asignados')


profesor1 = Profesor('Mercedes H')
profesor2 = Profesor('Richar L')

curso_basededatos = Curso("MongoDB")
curso_programacion = Curso('Python')
curso_matematica = Curso('Algebra Matricial')

profesor1.asignar_curso(curso_basededatos)
profesor1.asignar_curso(curso_programacion)

profesor2.asignar_curso(curso_basededatos)
profesor2.asignar_curso(curso_programacion)
profesor2.asignar_curso(curso_matematica)

profesor1.mostar_cursos()
profesor2.mostar_cursos()

print('**************   ')
curso_basededatos.mostar_profesores()
