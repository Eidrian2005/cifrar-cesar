class cifrador:    
    def __init__(self, mensaje):
        self.mensaje = mensaje

    def cifrar(self):
        abc="ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
        clave = 1
        cifrado = ''
        for letra in self.mensaje.upper():
            if letra in abc:
                indice = abc.find(letra)
                indice += clave
                if indice >= 27 :
                    indice -= 27
                cifrado += abc[indice]
            else:
                cifrado += letra 
                return cifrado
        print(cifrado)


inputEntrada = input("esto es secreto: ")
mensajes = cifrador(inputEntrada)

mensajes.cifrar()


        #Expected index or slice expression ---> falto agregar el "indice"
        #mensaje is not define --> definir mensaje con "self"
        #TypeError: find() takes at least 1 argument (0 given) ---> agregar un argumento para el .find() "letra"
        

