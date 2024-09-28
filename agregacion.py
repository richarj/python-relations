# Ejemplo:

# en el contexto de Músicos y una Orquesta. En este caso:

# Un Músico puede pertenecer a varias orquestas.
# Una Orquesta tiene muchos músicos, pero si se destruye la orquesta, los músicos seguirán existiendo y podrán unirse a otras orquestas.

class Musico:
    def __init__(self, nombre, instrumento):
        self.nombre = nombre
        self.instrumento = instrumento

    def __str__(self):
        return f'El musico {self.nombre}, toca el instrumento: {self.instrumento}'

    def tocar(self):
        print(f'El musico {self.nombre}, esta tocando el instrumento: {self.instrumento}')

class Orquesta:
    def __init__(self, nombre_orquesta):
        self.nombre_orquesta = nombre_orquesta
        self.musicos = []

    def agregar_musico(self, musico):
        self.musicos.append(musico)

    def lista_musicos(self):
        print(f'La lista de muicos de la orquesta {self.nombre_orquesta} es:')
        for musico in self.musicos:
            print(musico)

    def dar_concierto(self):
        print(f'Los muicos de la orquesta {self.nombre_orquesta}')
        for musico in self.musicos:
            print(musico.tocar())

    def __del__(self):
        print(f'La orquesta {self.nombre_orquesta} se ha eliminado')


musico1 = Musico('Sergio', 'Bateria')
musico2 = Musico('Angela', 'Violin')
musico3 = Musico('Carlos', 'Piano')

orquesta_laflorida = Orquesta('Orquesta municipal La Florida')
orquest_macul = Orquesta('Orquesta municipal Macul')

orquesta_laflorida.agregar_musico(musico1)
orquesta_laflorida.agregar_musico(musico2)

orquest_macul.agregar_musico(musico2)
orquest_macul.agregar_musico(musico3)

orquesta_laflorida.dar_concierto()
orquest_macul.dar_concierto()

del orquesta_laflorida
print(musico2)

while True:

    entrada = input()

    if (entrada.lower() == 'x'):
        break
