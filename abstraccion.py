
class Auto(): #Definimos Nuestra clase auto
    def __init__(self):#Creamos nuestro constructor y solamente le pasamos como parametro self
        self._estado = 'Apagado' #añadimos estado a nuestro parametro self como parametro muy privada asignadole un valor como Apagado

    def Encendido(self): #Defenimos una funcion de estado como Encendido
        self._estado = 'Encendido' #a la funcion encendido le pasamos el estado esta vez como encendido
        print('El auto esta encendido')#imprimimos que esta encendido
    
    def Conducir(self): #definimos una funcion conducir
        if self._estado == 'Apagado': #condicion para comprobar que si el estado esta apagado
            self.Encendido()#con self acceda a nuestra funcion encendido y encienda el carro
        print('Conduciendo el auto')#si el carro si esta encendido imprimimos que se esta conduciendo


mi_auto = Auto() #creamos una instancia de nuestra clase Auto
mi_auto.Conducir() #llamamos a la funcion conducir y gracias a la abstraccion se comete un proceso interno

