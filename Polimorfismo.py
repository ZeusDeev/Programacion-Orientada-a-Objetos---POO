#polimorfismo es un concepto en programación orientada a objetos que permite que una misma función o método pueda comportarse de diferentes maneras según el contexto. Esto significa que distintos objetos pueden responder de manera distinta a la misma llamada de método, dependiendo de su clase o tipo.

class perro(): #clase perro
    def sonido(self):#Definimos funcion sonido segun el contexto de la clase
        return 'Guao'#retornamos guao por sonido de perro

class pato():
    def sonido(self):#Definimos funcion sonido segun el contexto de la clase
        return 'cuak'#Retornamos cuak por sonido de pato

def hacer_sonido(animal):
    print(animal.sonido())

perro = perro() #creamos una instancia de nuestra clase perro
pato = pato() #creamos una instancia de nuestra clase pato

#Aca se aplica el polimorfismo, puesto que creamos una mismas funcion o metodo sonido y esta nos permite usarlo segun sea el caso, si usamos sonido para pato, hara el sonido de pato, o viciversa si usamos perro hara el sonido de perro, se
print(pato.sonido()) 
print(perro.sonido())

#existe otra manera de aplicar el polimorfisto, creamos una funcion hacer_sonido y le pasamos el argumento animal, dependiendo que animal sea hara el sonido (mirar en funcion hacer_sonido)
hacer_sonido(pato)
