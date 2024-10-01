# La herencia: 

# Esta relacion permite que una clase (llamada clase hija o subclase) herede atributos y métodos de otra clase
# (llamada clase padre o superclase). 
# La herencia permite reutilizar código y establecer una jerarquía de clases. 
# as subclases pueden heredar comportamiento de la superclase y, si es necesario, 
# pueden sobrescribir o extender las funcionalidades de la clase padre.

# Ejemplo:

# en el contexto de una empresa donde tenemos diferentes tipos de empleados. 
# Crearemos una superclase llamada Empleado, de la cual heredarán las subclases Desarrollador, 
# Gerente y Interno. Estas clases hijas heredarán los atributos y métodos de la clase Empleado, 
# y podrán sobrescribir o añadir su propio comportamiento.

class Empleado:
    def __init__(self, nombre, salario):
        self.nombre = nombre
        self.salario = salario

    def mostrar_informacion(self):
        """Muestra la información básica del empleado."""
        print(f"Empleado: {self.nombre}")
        print(f"Salario: {self.salario}")

    def aumentar_salario(self, porcentaje):
        """Aumenta el salario del empleado en un porcentaje dado."""
        self.salario += self.salario * (porcentaje / 100)
        print(f"El salario de {self.nombre} ha sido aumentado a: {self.salario}")


class Desarrollador(Empleado):
    def __init__(self, nombre, salario, lenguajes):
        """Llama al constructor de la clase padre y agrega un atributo específico."""
        super().__init__(nombre, salario)
        self.lenguajes = lenguajes  # Lista de lenguajes de programación que domina el desarrollador

    def mostrar_informacion(self):
        """Sobrescribe el método de la clase padre para mostrar también los lenguajes que domina."""
        super().mostrar_informacion()
        print(f"Lenguajes de programación: {', '.join(self.lenguajes)}")


class Gerente(Empleado):
    def __init__(self, nombre, salario, departamento):
        """Llama al constructor de la clase padre y agrega un atributo específico."""
        super().__init__(nombre, salario)
        self.departamento = departamento  # Departamento que maneja el gerente

    def mostrar_informacion(self):
        """Sobrescribe el método de la clase padre para incluir el departamento."""
        super().mostrar_informacion()
        print(f"Departamento: {self.departamento}")

    def cambiar_departamento(self, nuevo_departamento):
        """Permite cambiar el departamento del gerente."""
        self.departamento = nuevo_departamento
        print(f"{self.nombre} ahora es el gerente del departamento de {self.departamento}.")


class Interno(Empleado):
    def __init__(self, nombre, salario, duracion):
        """Llama al constructor de la clase padre y agrega un atributo específico."""
        super().__init__(nombre, salario)
        self.duracion = duracion  # Duración del internado en meses

    def mostrar_informacion(self):
        """Sobrescribe el método de la clase padre para incluir la duración del internado."""
        super().mostrar_informacion()
        print(f"Duración del internado: {self.duracion} meses")

    def extender_internado(self, meses):
        """Permite extender el internado en un número dado de meses."""
        self.duracion += meses
        print(f"La duración del internado de {self.nombre} ha sido extendida a {self.duracion} meses.")


# Crear instancias de las subclases
desarrollador1 = Desarrollador("Alice", 80000, ["Python", "JavaScript", "Java"])
gerente1 = Gerente("Carlos", 120000, "Recursos Humanos")
interno1 = Interno("Sofía", 20000, 6)

# Mostrar información de cada empleado
desarrollador1.mostrar_informacion()
gerente1.mostrar_informacion()
interno1.mostrar_informacion()

print("\n--- Aumentos de salario ---")
# Aumentar el salario de los empleados
desarrollador1.aumentar_salario(10)
gerente1.aumentar_salario(5)
interno1.aumentar_salario(3)

print("\n--- Cambios específicos ---")
# Cambiar departamento del gerente
gerente1.cambiar_departamento("Marketing")

# Extender la duración del internado
interno1.extender_internado(3)
