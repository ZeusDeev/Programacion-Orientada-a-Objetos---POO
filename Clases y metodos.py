# Creamos una clase llamada 'celular'
class celular:
    # El método __init__ se utiliza como constructor de la clase
    # Se ejecuta cuando se crea una nueva instancia de la clase
    def __init__(self, marca, modelo, camara):
        # 'self' se refiere a la instancia actual de la clase
        # Los atributos 'marca', 'modelo' y 'camara' se asignan a la instancia
        
        self.marca = marca  # Atributo de instancia que guarda la marca del celular
        self.modelo = modelo  # Atributo de instancia que guarda el modelo del celular
        self.camara = camara  # Atributo de instancia que guarda la resolución de la cámara

    # Método para realizar una llamada
    def llamar(self):
        # 'self' permite acceder a los atributos de la instancia
        # Imprime un mensaje que indica desde qué celular se está llamando
        print(f'Estas llamando desde un: {self.marca, self.modelo}')

    # Método para colgar una llamada
    def colgar(self):
        # Imprime un mensaje que indica desde qué celular se está colgando
        print(f'Estas colgando desde un: {self.marca, self.modelo}')

# Creamos una instancia de la clase celular
celu1 = celular("Iphone", 'xs', '58px')

# Llamamos al método 'llamar' de la instancia celu1
celu1.llamar()
