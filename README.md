# Virtual Machine Text Editor
**Bienvenidos a la presentación de mi proyecto de una máquina virtual básica de edición de texto para la Universidad Camilo José Cela.** 
**En este proyecto nos han pedido hacer una pequeña Máquina Virtual basada en pilas, en este caso he utilizado Python.**

**El codigo se basa en una serie de funciones que se van a encargar de realizar el funcionamiento básico de un editor de texto como escribir, copiar, pegar, deshacer, rehacer...**


> ## INTEGRANTES DEL PROYECTO
>  -Iván Seco Martín
>
>  -Mario Suárez del Hierro
>
>  -Javier Poza Garijo

>[!IMPORTANT]
>## REQUISITOS
>Tener Python instalado.
>
>Instalar Flask
>
>     pip install Flask  
>
>Descargar la carpeta de *VirtualMachine*
>
>Acceder a la carpeta descargada
>
>      cd ruta/al/archivo
>
>Ejecución del programa
>
>      python .\app.py
>
>
>
>



>
### EXPLICACION BASICA DEL PROGRAMA
El código implementa una clase "MaquinaVirtualSimple" en Python, que simula un editor de texto básico con funcionalidades de escribir, deshacer, rehacer, copiar, pegar, transformar a mayúsculas texto.

La clase maneja 3 pilas: una para las acciones realizadas, otra para las acciones que se pueden rehacer y otra que actúa como portapapeles para almacenar el texto que se ha copiado.

Esto permite un control eficiente del estado del texto y sus modificaciones.

>[!NOTE]
> Las instrucciones se cargan desde un archivo de texto y se ejecutan secuencialmente, no se ejecuta el código desde Python.

# Funcionalidades
## Clase MaquinaVirtualSimple
### Métodos Principales
Hay una serie de métodos en la clase MaquinaVirtualSimple que hacen funcionar a la máquina, dichos métodos son los siguientes:
- **__init__():** Constructor de la clase, aquí se inicializan las 3 pilas que tenemos, y la lista de instrucciones que indicamos en el archivo de texto.
- **cargarPrograma(instrucciones):** Cargar una lista de instrucciones para ser ejecutadas.
- **ejecutar():** Ejecuta las instrucciones cargadas en la máquina virtual.

### Comandos para ejecutar las instrucciones en el fichero de texto
Aquí se explicarán los comandos que hemos asignado a cada instrucción:
- **ESCRIBIR:** Añade el texto especificado al texto actual.
- **DESHACER:** Deshace la última acción realizada.
- **REHACER:** Rehace la última acción que fue deshecha.
- **COPIAR:** Copia la palabra especificada al portapapeles.
- **PEGAR:** Pega la última palabra copiada al texto actual.
- **MOSTRAR:** Muestra la última modificación del texto.

# Métodos de operación sobre las pilas
Estos son los métodos que van a realizar las diferentes instrucciones, a las que se han asignado los distintos comandos:
- **escribir_texto(texto):**  Agrega texto a la pila de cambios, se corresponde con el comando ESCRIBIR.
- **deshacer():**  Deshace el último cambio realizado., se corresponde con el comando DESHACER.
- **rehacer():**  Rehace el último cambio deshecho, se corresponde con el comando REHACER.
- **copiarPalabra(palabra):**  Copia la palabra del texto actual que el usuario eliga, se corresponde con el comando COPIAR.
- **pegarPalabra():**   Pega la última palabra copiada al texto actual, se corresponde con el comando PEGAR.
- **vaciar_rehacer():**  Vacía la pila de rehacer al realizar un nuevo cambios, se utiliza en los métodos escribir_texto.
- **obtenerTextoActual():**  Devuelve el texto actual concatenando todos los cambios, se corresponde con el comando MOSTRAR.


### CARACTERÍSTICAS CLAVE
Lo mas importante de este proyecto es poder hacer uso de la programación para hacer música y sobretodo poder modificarla en directo, haciendo uso de variables y jugando con operaciones básicas como If get o while.

Por otro lado, el poder modificar el sonido de forma directa usando bucles for te abre un mundo de posibilidades para cualquier estilo de música, en concreto para este proyecto el poder hacer drops para la canción.

Este programa usa programación en **Ruby**, un lenguaje que te exige tener un poco de idea de programacion (sobretodo en bucles) pero que aun así es sencillo de aprender si se trabaja.

>[!NOTE]
>### DOCUMENTACIÓN
> **SONIC PI:** https://sonic-pi.net/tutorial.html
>
> **MP3 CUTTER:** https://mp3cut.net/es/
>
> **VOCAL REMOVER:** https://vocalremover.org/splitter-ai
>
> **MELODY GENRATOR:** https://dopeloop.ai/melody-generator/
>
> **SONG BPM:** https://songbpm.com/
>
> **TECHNO SAMPLES:**
>    https://www.loopmasters.com/genres/40-Techno?srsltid=AfmBOorgyWB2plTl2cSTh1MSIXF0XR28i28we7g5g0hW45qDhZ6-D9I-
>
>    https://samplefocus.com/
>
> **README GUIDE:** https://tiloid.com/p/readme-md-the-ultimate-guide
>
> **CHAT GPT 4**
