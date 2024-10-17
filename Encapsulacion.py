class Persona:
    def __init__(self, nombre, edad):
        # Inicializa los atributos privados _nombre y _edad con los valores proporcionados
        self._nombre = nombre
        self._edad = edad

    def get_nombre(self):
        # Método getter para acceder al atributo privado _nombre
        return self._nombre

    def get_edad(self):
        # Método getter para acceder al atributo privado _edad
        return self._edad

    def set_nombre(self, nuevo_nombre):
        # Método setter para modificar el atributo privado _nombre con un nuevo valor
        self._nombre = nuevo_nombre
    
    def set_edad(self, nueva_edad):
        # Método setter para modificar el atributo privado _edad con un nuevo valor
        self._edad = nueva_edad

# Creamos una instancia de la clase Persona llamada 'zeus' con el nombre 'Zeus' y edad '19'
zeus = Persona('Zeus', '19') 

# Accedemos al nombre y la edad de la instancia 'zeus' utilizando los métodos getter
nombre = zeus.get_nombre()
edad = zeus.get_edad()

# Imprimimos el nombre y la edad actuales de la instancia 'zeus'
print(f'{nombre}\n{edad}')

# Modificamos el nombre y la edad de la instancia 'zeus' utilizando los métodos setter
zeus.set_nombre('Emmanuel')  
zeus.set_edad(20)

# Accedemos de nuevo al nombre y la edad después de haberlos actualizado
nombre = zeus.get_nombre()
edad = zeus.get_edad()

# Imprimimos el nuevo nombre y la nueva edad de la instancia 'zeus'
print(f'{nombre}\n{edad}')
