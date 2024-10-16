class Estudiante:
    def __init__(self, nombre, edad, grado):
        self.nombre = nombre
        self.edad = edad
        self.grado = grado

    def Estudiando(self):
        print(f'El estudiante {self.nombre}, de grado {self.grado}, está estudiando.')


nombre = input('Ingrese su nombre: ')
edad = int(input('Ingrese su edad: '))
grado = int(input('Ingrese su grado: '))

# Crear una instancia de Estudiante
estudiante = Estudiante(nombre, edad, grado)

# Imprimir los datos del estudiante
print(f'Datos del estudiante\n Nombre: {estudiante.nombre}\n Edad: {estudiante.edad}\n Grado: {estudiante.grado}')

# Llamar al método 'Estudiando'
estudiante.Estudiando()
