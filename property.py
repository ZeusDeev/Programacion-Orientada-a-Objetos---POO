class Persona:
    def __init__(self, nombre, edad):
        self._nombre = nombre
        self._edad = edad

    @property #Con el @property hacemos referencia de que es un getter
    def nombre(self):
        return self._nombre
    
    @property
    def edad(self):
        return self._edad
    
    @nombre.setter #con el @set_nombre.setter definimos que set_nombre es un setter
    def nombre(self, nuevo_nombre):
        self._nombre = nuevo_nombre

    @edad.setter
    def edad(self, nueva_edad):
        self._edad = nueva_edad

zeus = Persona('Zeus', '19') 

nombre = zeus.nombre
edad = zeus.edad

print(f'{nombre}\n{edad}')

zeus.nombre = 'Emmanuel'
zeus.edad = 20

nombre = zeus.nombre
edad = zeus.edad

print(f'{nombre}\n{edad}')
