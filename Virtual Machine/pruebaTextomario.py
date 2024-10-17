class Pila:
    DESHACER = "DESHACER"
    REHACER = "REHACER"
    COPIAR = "COPIAR"
    PEGAR = "PEGAR"

    def __init__(self):
        self.pila = []  # Pila principal para deshacer
        self.pilaRehacer = []  # Pila secundaria para rehacer
        self.pilaCopiar = []

    def esta_vacia(self):
        return len(self.pila) == 0  # Verifica si la pila de deshacer está vacía

    def agregar(self, item):
        self.pila.append(item)  # Añade un estado a la pila de deshacer

    def quitar(self):
        if not self.esta_vacia():
            r1 = self.pila.pop()  # Quita el último elemento de la pila de deshacer
            return r1
        else:
            return None

    def agregar_rehacer(self, item):
        """Añade un estado a la pila de rehacer"""
        self.pilaRehacer.append(item)

    def quitar_rehacer(self):
        """Quita el último estado de la pila de rehacer"""
        if len(self.pilaRehacer) > 0:
            return self.pilaRehacer.pop()
        else:
            return None

    def vaciar_rehacer(self):
        """Vacía la pila de rehacer (cuando se realiza una nueva acción)"""
        self.pilaRehacer = []
    
    def ultimo(self):
        if not self.esta_vacia():
            return self.pila[-1]
        else:
            return None

    def copiar(self,palabra):
        if len(self.pilaCopiar) > 0:
            self.pilaCopiar.pop()
        self.pilaCopiar.append(palabra)
        print(f"Se ha copiado correctamente la palabra: '{palabra}'. ")

    def pegar(self):
        if len(self.pilaCopiar) > 0:
            return self.pilaCopiar[-1]
        else:
            print("No hay ninguna palabra copiada para poder pegar")
            return ""


# Simulación de un editor de texto
texto_actual = ""
pila_cambios = Pila()  # Instancia de la clase Pila

def escribir_texto(texto):
    global texto_actual
    pila_cambios.agregar(texto_actual)  # Guardar el estado actual en la pila de deshacer
    texto_actual += texto  # Añadir el nuevo texto
    pila_cambios.vaciar_rehacer()  # Vaciar la pila de rehacer al escribir texto nuevo
    print("Texto escrito.")

def mostrarTextoAñadido():
    global texto_actual
    ultimo_texto = pila_cambios.ultimo()
    if ultimo_texto is not None:
        print(f"El texto actual es: '{texto_actual}'") 
    else:
        print("No se puede ver el último elemento de la pila, ya que está vacía")


def deshacer():
    global texto_actual
    if not pila_cambios.esta_vacia():
        pila_cambios.agregar_rehacer(texto_actual)  # Guardar el estado actual en la pila de rehacer
        texto_actual = pila_cambios.quitar()  # Recuperar el último estado de la pila de deshacer
        print(f"Deshacer realizado. Texto actual: '{texto_actual}'")
    else:
        print("No hay más acciones para deshacer.")

def rehacer():
    global texto_actual
    accion_rehacer = pila_cambios.quitar_rehacer()  # Recuperar el último estado de la pila de rehacer
    if accion_rehacer is not None:
        pila_cambios.agregar(texto_actual)  # Guardar el estado actual en la pila de deshacer
        texto_actual = accion_rehacer  # Actualizar el texto al estado rehecho
        print(f"Rehacer realizado. Texto actual: '{texto_actual}'")
    else:
        print("No hay acciones para rehacer.")

def copiarPalabra(palabra):
    global texto_actual
    if palabra in texto_actual:
        pila_cambios.copiar(palabra)
    else:
        print(f"La palabra '{palabra}' no se encuentra escrita")

def pegarPalabra():
    global texto_actual
    palabra = pila_cambios.pegar()
    if palabra:
        print(f"Palabara '{palabra}' pegada.")
        texto_actual += palabra




# Ejemplo de uso:
escribir_texto("Prueba")
escribir_texto("Prueba2")
escribir_texto("Prueba3")
mostrarTextoAñadido()
copiarPalabra("Prueba")
copiarPalabra("Prueba3")
pegarPalabra()
deshacer()
rehacer()
mostrarTextoAñadido()

