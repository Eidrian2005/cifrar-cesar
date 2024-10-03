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