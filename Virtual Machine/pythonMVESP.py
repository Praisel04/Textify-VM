import argparse

class MaquinaVirtualSimple:
    DESHACER = "DESHACER"
    REHACER = "REHACER"
    COPIAR = "COPIAR"
    PEGAR = "PEGAR"
    ESCRIBIR = "ESCRIBIR"

    def __init__(self):
        # Pilas necesarias para la Máquina Virtual
        self.pilaCambios = []        # Pila principal para cambios de texto (deshacer)
        self.pilaRehacer = []        # Pila secundaria para rehacer
        self.pilaCopiar = []         # Pila para copiar y pegar
        self.instrucciones = []      # Lista para almacenar instrucciones

    def cargarPrograma(self, instrucciones):
        """Cargar las instrucciones desde un archivo o una lista"""
        self.instrucciones = instrucciones  # Cargar la lista de instrucciones

    def ejecutar(self):
        """Ejecutar las instrucciones cargadas en la máquina"""
        for instr in self.instrucciones:
            comando = instr[0]
            if comando == self.DESHACER:
                self.deshacer()
            elif comando == self.REHACER:
                self.rehacer()
            elif comando == self.COPIAR:
                palabra = instr[1] if len(instr) > 1 else ""
                self.copiarPalabra(palabra)
            elif comando == self.PEGAR:
                self.pegarPalabra()
            elif comando == self.ESCRIBIR:
                texto = instr[1] if len(instr) > 1 else ""
                self.escribir_texto(texto)

    # Métodos de operación sobre las pilas

    def escribir_texto(self, texto):
        """Simulación de escribir texto (se guarda en la pila de cambios)"""
        if texto:
            self.pilaCambios.append(texto)
            self.vaciar_rehacer()  # Vaciar pila de rehacer cuando se añade nuevo texto
        print(f"The text has been write. Actual text: {self.obtenerTextoActual()}")

    def deshacer(self):
        if len(self.pilaCambios) > 0:
            ultimo_cambio = self.pilaCambios.pop()  # Sacar último cambio
            self.pilaRehacer.append(ultimo_cambio)  # Guardar en rehacer
            print(f"Deshacer realizado. Texto actual: {self.obtenerTextoActual()} ")
        else:
            print("No hay más cambios para deshacer.")

    def rehacer(self):
        if len(self.pilaRehacer) > 0:
            texto_rehecho = self.pilaRehacer.pop()  # Rehacer último cambio
            self.pilaCambios.append(texto_rehecho)  # Guardar en cambios
            print(f"Rehacer realizado. Texto actual: {self.obtenerTextoActual()}")
        else:
            print("No hay más cambios para rehacer.")

    def copiarPalabra(self, palabra):
        if palabra in self.obtenerTextoActual():
            if len(self.pilaCopiar) > 0:
                self.pilaCopiar.pop()  # Vaciar cualquier palabra previamente copiada
            self.pilaCopiar.append(palabra)
            print(f"Palabra '{palabra}' copiada.")
        else:
            print(f"La palabra '{palabra}' no se encuentra en el texto actual.")

    def pegarPalabra(self):
        if len(self.pilaCopiar) > 0:
            palabra = self.pilaCopiar[-1]
            self.pilaCambios.append(palabra)
            print(f"Palabra '{palabra}' pegada en el texto actual.")
        else:
            print("No hay ninguna palabra copiada.")

    def vaciar_rehacer(self):
        """Vacía la pila de rehacer cuando se hace un nuevo cambio"""
        self.pilaRehacer = []

    def obtenerTextoActual(self):
        """Obtener el texto actual concatenando todos los cambios"""
        return ''.join(self.pilaCambios)


# Función para leer el archivo de texto personalizado
def leer_instrucciones_desde_fichero(fichero):
    instrucciones = []
    with open(fichero, 'r') as f:
        for linea in f:
            partes = linea.strip().split(' ')
            comando = partes[0]
            argumentos = partes[1:]  # Restante de la línea como argumentos
            instrucciones.append([comando] + argumentos)
    return instrucciones


# Configurar argparse para aceptar argumentos de línea de comandos
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Máquina virtual simple para ejecutar instrucciones de un archivo.")
    parser.add_argument('fichero', type=str, help="El fichero de texto con las instrucciones")
    args = parser.parse_args()

    # Leer las instrucciones desde el fichero
    instrucciones = leer_instrucciones_desde_fichero(args.fichero)

    # Crear una instancia de la máquina virtual
    maquina = MaquinaVirtualSimple()

    # Cargar las instrucciones y ejecutarlas
    maquina.cargarPrograma(instrucciones)
    maquina.ejecutar()