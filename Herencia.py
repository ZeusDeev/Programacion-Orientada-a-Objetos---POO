class persona: #Creamos una clase persona
    def __init__(self, nombre, edad, nacionalidad): #Definimos nuestro constructor
        self.nombre = nombre #inicamos nuestros parametros
        self.edad = edad
        self.nacionalidad = nacionalidad

    def camina(self):
        print(f'Hola, soy {self.nombre} y estoy caminando')


class empleado(persona): #Creamos una clase empleado que Hereda de persona
    pass

persona1 = empleado('zeus', 23,'Mexicano') #creamos una instancia de nuestro objeto heredando de nuestra clase padre

print(persona1.nombre)# imprimimos el nombre

persona1.camina() #imprime el metodo camina de nuestra clase padre