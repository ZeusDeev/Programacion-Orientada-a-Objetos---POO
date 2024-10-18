# Definición del decorador, que toma una función como argumento
def decorador(funcion):
    # Función interna que modifica el comportamiento de la función original
    def funcion_modificada():
        print('Antes de Llamar a la funcion')  # Comportamiento extra antes de ejecutar la función
        funcion()  # Llamada a la función original
    return funcion_modificada  # Se retorna la función modificada

# Usamos el decorador para modificar la función 'saludo'
@decorador
def saludo():
    print('Hola soy zeus')  # Comportamiento original de la función

# Al llamar 'saludo', en realidad se llama a 'funcion_modificada' del decorador
saludo()
