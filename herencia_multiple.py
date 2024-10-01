# Clase base 1: Dispositivo Electrónico
class DispositivoElectronico:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
    
    def encender(self):
        print(f"El {self.marca} {self.modelo} está encendido.")
    
    def apagar(self):
        print(f"El {self.marca} {self.modelo} está apagado.")

# Clase base 2: Conectable
class Conectable:
    def __init__(self, red):
        self.red = red
        self.conectado = False
    
    def conectar(self):
        if not self.conectado:
            print(f"Conectando a la red {self.red}...")
            self.conectado = True
        else:
            print(f"Ya está conectado a la red {self.red}.")
    
    def desconectar(self):
        if self.conectado:
            print(f"Desconectando de la red {self.red}...")
            self.conectado = False
        else:
            print(f"Ya está desconectado de la red {self.red}.")

# Clase derivada: Teléfono Inteligente
class TelefonoInteligente(DispositivoElectronico, Conectable):
    def __init__(self, marca, modelo, red, numero_telefono):
        # Llamada explícita a los inicializadores de las clases base
        DispositivoElectronico.__init__(self, marca, modelo)
        Conectable.__init__(self, red)
        self.numero_telefono = numero_telefono
    
    def hacer_llamada(self, numero_destino):
        if self.conectado:
            print(f"Llamando a {numero_destino} desde {self.numero_telefono}...")
        else:
            print("El teléfono no está conectado a la red, no se puede realizar la llamada.")

# Uso de la clase TelefonoInteligente
telefono = TelefonoInteligente("Samsung", "Galaxy S21", "Wi-Fi Hogar", "+123456789")

# Usamos métodos de ambas clases base
telefono.encender()
telefono.conectar()
telefono.hacer_llamada("+987654321")
telefono.desconectar()
telefono.apagar()
