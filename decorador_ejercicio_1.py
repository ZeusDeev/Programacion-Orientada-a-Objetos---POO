def regalo(funcion):
    # Función interna que modifica el comportamiento
    def regalo_modificado():
        print('Desenvolviendo regalo para poner nuevo envoltorio...')  # Esto es lo que añades antes
        funcion()  # Aquí llamas a la función original (envoltorio_nuevo)
    return regalo_modificado  # Devuelves la función modificada

# Aplicas el decorador a la función 'envoltorio_nuevo'
@regalo
def envoltorio_nuevo():
    print('Estoy envolviendo con un envoltorio nuevo color rojo')  # Esta es la función original

# Llamas a la función decorada
envoltorio_nuevo()
