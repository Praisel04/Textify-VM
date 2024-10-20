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
>Tras ejecutar esto, en al terminal saldrá una ruta donde se estará ejecutando el servidor.



>
### EXPLICACION BASICA DEL PROGRAMA
El codigo implementa una variedad de archivos.

  - **mv1.py:** Es el archivo dedicado a la Máquina Virtual. Cuenta con la inicialización de todas instrucciones del programa , así como sus funciones.
  - **app.py:** Contiene Flask y las rutas de servidor, con las ejecuciones que van a llevar cada una.
  - **genQrCode.py:** Es el archivo dedicado a la generación del codigo QR, donde hay que cambiar la URL y tras ejecutarlo, introducir la imagen en la carpeta static.
  - **templates/index.html:** Contiene la estructura de l página web.
  - **static/style.css:** Contiene el formato de la página web.
  

# Funcionalidades de la Máquina Virtual
### Métodos Principales

- **__init__():** Constructor de la clase, aquí se inicializan las 5 pilas que usará el programa, y el listado de instrucciones
  
  - changeStack: Pila principal donde se guarda el texto que se escribe y las modificaciones que se hacen.
  - redoStack: Pila que se encarga de guardar los cambios de UNDO y REDO.
  - copyStack: Pila que se encarga de guardar los cambios de COPY y PASTE.
  - instructions: Pila encargada de almacenar las instrucciones del usuario.
  - messages: Pila encargada de almacenar los mensajes que se van a mostrar al usaurio.
      
- **loadProgram(instrucciones):** Cargar una lista de instrucciones para ser ejecutadas.
- **execute():** Ejecuta las instrucciones cargadas en la máquina virtual.

### Comandos para ejecutar las instrucciones en el fichero de texto
- **WRITE:** Escribe el texto especificado por el usuario.
- **UNDO:** Deshace la última acción realizada.
- **REDO:** Rehace la última acción que fue deshecha.
- **COPY:** Copia la palabra especificada al portapapeles.
- **PASTE:** Pega la última palabra copiada al texto actual.
- **SHOW:** Muestra la última modificación del texto.
- **UPPER:** Convierte todo el texto a mayúsculas
- **LOWER:** Convierte todo el texto a minúsculas
- **CLEAR:** Borra todos los mensajes de la terminal
- **HELP** Muestra un pequeño mensaje mostrando todos los comando disponibles
>[!NOTE]
>**TODOS LOS COMANDO MOSTRARÁN UN MENSAJE DE ERROR SI NO PUEDEN EJECUTAR LA INSTRUCCIÓN**

# Métodos de operación sobre las pilas
- **writeText(text):**  Agrega el texto solicitado a la pila de cambios.
- **undo():**  Deshace el último cambio realizado guardado en la pila se cambios. Guarda la palabra cambiada en la pila para poder hacer un REDO.
- **redo():**  Rehace el último cambio deshecho.
- **copyWord(palabra):**  Copia la palabra del texto actual que el usuario pase como parametro de la función. Se guarda en la pila copyStack, para poder ser utilizada por la función PASTE.
- **paste():**   Pega la última palabra copiada al texto actual. Cuando se ejecuta la función la palabra no sale de la pila, para poder ser pegada mas veces
- **clearRedo():** Función para limpiar la pila del REDO
- **getCurrentText():**  Función que se usa para obtener el texto actual, simplemente para uso entre funciones.
- **showAddedText():** Función para mostar al usuario el texto actual.
- **upper():** Función para pasar todo el texto a mayúsculas.
- **lower():** Función para pasar todo el texto a minúsculas.
- **clear():** Función para borrar todos los mensajes de la terminal.
- **help():** Funcion que muestra todos los comandos disponibles usando la pila de mensajes.


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
