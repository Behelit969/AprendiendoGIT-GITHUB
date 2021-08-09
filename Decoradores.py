'''
def decorador(func): #Creamos la funcion decorador (A)
    def nueva_funcion(): #Creamos la nueva funcion (C)
        print ("Perro dice:")#Añadimos una modificacion a la funcion (B) dentro (C)
        func() #Aqui estamos incluyendo la funcion (B) que le dimos como argumento a (A)
                
    return nueva_funcion #Para crear (C)

@decorador #Decoramos la función
def saluda(): #Con decorador
    print("Guau!")

@decorador
def despedida(): #Con decorador
    print ("Chau")

def movercola(): #Sin decorador
    print ("El perro mueve la cola")

#saluda()
#despedida()
    
#movercola()
'''

def otra (func):
    def multiplica(x,y):
        print (2 * func(x,y))
    
    return multiplica


@otra
def suma (x,y):
    return x + y

#suma(2,3)

@otra
def resta(x,y):
    return x - y

#resta(15,6)



def decorador(func):
    def nueva_funcion(self, mensaje):
        print ("El perro dice:")
        func(self,mensaje)
    
    return nueva_funcion

class perro:
    def __init__(self, nombre) -> None:
        self.nombre = nombre

    @decorador
    def saluda(self, mensaje):
        self.mensaje = mensaje
        print (mensaje)
        print ("GUAU")

#maty = perro("Sultan")
#maty.saluda("Hola puto")

class midecorador:
    def __init__(self,func) -> None:
        self.func = func

    def __call__(self):
        print ("Soy una clase llamada mediante call")
        self.func()

@midecorador
def hablar():
    print("Hola soy la función hablar")

matias = midecorador(hablar)
#matias()
matias.__call__()



