
class persona: #Creamos una clase persona
    def __init__(self, nombre, edad, nacionalidad): #Definimos nuestro constructor
        self.nombre = nombre #inicamos nuestros parametros
        self.edad = edad
        self.nacionalidad = nacionalidad

    def camina(self):
        print(f'Estoy caminando para mi trabajo')


class empleado(persona): #Creamos una clase empleado que Hereda de persona
    def __init__(self, nombre, edad, nacionalidad, trabajo, salario):#Creamos un constructor a la cual le pasamos nuestros primeros parametros de nuestra clase padre
        super().__init__(nombre, edad, nacionalidad)#Con el constructor super, pasamos nuestros parametros que deseamos agregar a nuestra nueva clase (hija) y asi poder heredar y usar nuevos parametros.
        self.trabajo = trabajo
        self.salario = salario
    
    def caracteristicas(self):
        print(f'Hola soy {self.nombre}, Trabajo de {self.trabajo}, y gano al rededor de {self.salario}')


#creamos una instancia de nuestro objeto heredando de nuestra clase padre
persona1 = empleado('zeus', 23,'Mexicano', 'Cientifico de Datos - Junior', '$40,000') 

persona1.caracteristicas()
persona1.camina()
