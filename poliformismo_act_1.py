#Crea una clase CiberTruck y Otra Nissan Sentra, Ambos carros, uno electrico y otro a gasolina, usa el polimorfismo creando una funcion o metodo manejar para ambos estados(clases), y me devuelva segun el tipo de carro manejado. Ejemplo: 'Estoy manejando un carro electrico' o 'Estoy manejando un carro a gasolina'abs

class CiberTruck():  # Definición de una clase llamada CiberTruck
    def manejar(self):  # Método manejar dentro de la clase CiberTruck
        return 'Estoy Manejando un carro futurista Electrico'  # Devuelve una cadena que describe el tipo de carro

class NissanSentra():  # Definición de una clase llamada NissanSentra
    def manejar(self):  # Método manejar dentro de la clase NissanSentra
        return 'Estoy manejando un carro moderno a gasolina'  # Devuelve una cadena que describe el tipo de carro

def tipo_manejar(carro):  # Función que recibe un objeto llamado carro
    print(carro.manejar())  # Llama al método manejar del objeto carro y lo imprime

ciber_truck = CiberTruck()  # Creación de una instancia de la clase CiberTruck
nissan_sentra = NissanSentra()  # Creación de una instancia de la clase NissanSentra

tipo_manejar(ciber_truck)  # Llama a la función tipo_manejar pasando un objeto de la clase CiberTruck
tipo_manejar(nissan_sentra)  # Llama a la función tipo_manejar pasando un objeto de la clase NissanSentra


