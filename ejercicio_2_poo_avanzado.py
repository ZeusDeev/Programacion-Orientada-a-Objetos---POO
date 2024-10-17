
""" 
Ejercicio:
Desarrollar una aplicación de galería de imágenes que permita a los usuarios gestionar sus fotos mediante la actualización y eliminación de las mismas. Utilizando Programación Orientada a Objetos (POO), la aplicación debe incluir interacciones con el usuario en cada función o método. Además, se debe implementar una clase derivada que incorpore capacidades de mejora y dibujo sobre las imágenes utilizando inteligencia artificial.

Objetivos:
- Crea una aplicación de galería que permite al usuario actualizar y eliminar - imágenes.
- Utiliza principios de Programación Orientada a Objetos (POO) y métodos interactivos.
"""

# Lista para almacenar los títulos de las fotos
almacen_fotos = []

# Clase base que representa una galería de imágenes
class galeria:
    # Inicializa los atributos de la galería
    def __init__(self, titulo, dimension, tipo):
        self.titulo = titulo  # Título de la imagen
        self.dimension = dimension  # Dimensiones de la imagen
        self.tipo = tipo  # Tipo de archivo (png, jpg, etc.)

    # Método para subir una foto a la galería
    def subir(self):
        print('Se está subiendo su foto...')  # Mensaje informativo
        print(f'Nombre de la foto: {self.titulo}\ndimension: {self.dimension}\ntipo: {self.tipo}')
        almacen_fotos.append(self.titulo)  # Agrega el título a la lista de fotos
        print(f'Se subió: {almacen_fotos}')  # Muestra el estado del almacén de fotos
    
    # Método para actualizar la información de la foto
    def actualizar(self):
        modificar = input('¿Desea modificar tu imagen? (Si o No): ').lower()  # Pregunta al usuario

        if modificar == 'si':  # Si el usuario desea modificar
            titulo_anterior = self.titulo  # Guarda el título anterior
            # Solicita nuevos datos
            nuevo_titulo = input('Ingrese el nuevo titulo: ')
            nueva_dimension = input('Ingrese las nuevas dimensiones: ')
            nuevo_tipo = input('Ingrese el nuevo tipo(png, jpg, web): ')

            # Actualiza los atributos de la instancia
            self.titulo = nuevo_titulo
            self.dimension = nueva_dimension
            self.tipo = nuevo_tipo

            # Busca el índice del título anterior en la lista
            indice = almacen_fotos.index(titulo_anterior)

            # Reemplaza el título en la lista por el nuevo valor
            almacen_fotos[indice] = self.titulo

            # Mensaje de confirmación
            print(f'La imagen fue actualizada con éxito :) \nTitulo: {self.titulo}\nDimension: {self.dimension}\nTipo: {self.tipo}')

    # Método para eliminar la imagen del almacén
    def eliminar(self):
        # Pregunta al usuario si desea eliminar la imagen
        Eliminar = input(f'Sección Eliminar\nDesea eliminar su imagen {self.titulo} (Si o No): ').lower()

        if Eliminar == 'si':  # Si el usuario confirma la eliminación
            # Busca el índice de la imagen en el almacén y la elimina
            indice_drop = almacen_fotos.index(self.titulo)
            almacen_fotos.pop(indice_drop)  # Elimina el título del almacén
            print(f'Se borró su imagen, no existe algún registro en el almacen_fotos: {almacen_fotos}')

# Clase que hereda de galeria y añade funcionalidades de inteligencia artificial
class foto_ia(galeria):
    # Inicializa los atributos específicos de foto_ia
    def __init__(self, titulo, dimension, tipo):
        super().__init__(titulo, dimension, tipo)  # Llama al inicializador de la clase padre
        self.mejorar_ia = None  # Atributo para mejora de IA
        self.dibujar_ia = None  # Atributo para dibujo de IA
    
    # Método para mejorar la imagen usando inteligencia artificial
    def mejorar(self):
        acceso_mejorar = input(f'Sección IA\n ¿Desea Mejorar su imagen {self.titulo} con Inteligencia Artificial?\nResponda (Si o No): ').lower()

        if acceso_mejorar == 'si':  # Si el usuario desea mejorar
            mejorar_imagen = input('Mejora que se le hará a su imagen: ')  # Solicita mejora
            # Mensaje de confirmación
            print(f'A su Imagen {self.titulo}, se le aplicó la mejora de {mejorar_imagen} con Inteligencia Artificial...')

    # Método para dibujar sobre la imagen usando inteligencia artificial
    def dibujar(self):
        acceso_dibujar = input(f'¿Desea dibujar sobre su imagen {self.titulo} con Inteligencia Artificial?\nResponda (Si o No): ').lower()

        if acceso_dibujar == 'si':  # Si el usuario desea dibujar
            dibujo = input('¿Qué desea dibujar?\nResponda: ')  # Solicita el dibujo
            # Mensaje de confirmación
            print(f'A su Imagen {self.titulo}, se ha dibujado un bosquejo de {dibujo} con Inteligencia Artificial...')

# Bloque principal del programa
print('------------------------\nBienvenido a AppGalery\nAñada una foto\n------------------------')
titulo = input('Título de imagen: ')  # Solicita el título de la imagen
dimension = input('Dimensión de imagen: ')  # Solicita la dimensión de la imagen
tipo = input('Tipo de imagen (png, jpg, web): ')  # Solicita el tipo de imagen

# Crea una instancia de foto_ia con los datos proporcionados
imagen_1 = foto_ia(titulo, dimension, tipo)

# Llama a los métodos para subir, actualizar y eliminar la imagen
imagen_1.subir()
imagen_1.actualizar()
imagen_1.eliminar()

# Comprueba si la lista de fotos está vacía para decidir si aplicar IA
if almacen_fotos == []:
    print('Por lo tanto no se puede aplicar Inteligencia Artificial a tu imagen, ya que has borrado tu registro...')
else:    
    imagen_1.mejorar()  # Llama al método para mejorar la imagen
    imagen_1.dibujar()  # Llama al método para dibujar sobre la imagen
