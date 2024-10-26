# TEXTIFY VIRTUAL MACHINE
**Bienvenidos a la presentación de mi proyecto de una máquina virtual básica de edición de texto para la Universidad Camilo José Cela.** 
**En este proyecto nos han pedido hacer una pequeña Máquina Virtual basada en pilas.**

**Lenguajes Utilizados (Programacion, tipo y estilo)**
  - Python.
  - JavaScript
  - HTML
  - CSS
    

**El código se basa en una serie de funciones que se van a encargar de realizar el funcionamiento básico de un editor de texto como escribir, copiar, pegar, deshacer, rehacer...**


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
>Instalar Flask (framework), QrCode(generación del codigo QR) y googletranslator (Traductor de textos)
>
>     pip install flask
>     pip install qrcode[pil]
>     pip install googletrans==4.0.0-rc1
>
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

### INTRUCCIONES DE USO
Este editor de texto está hecho de una manera que el usuario pueda usarlo de una forma sencilla.

En el cuadro donde pone *Enter instruccions here...* escribiremos los comandos deseados ( el listado de comandos está indicado debajo, tambien puede usar el comando **HELP** para mas información.)  
>[!NOTE]
>  - LAS INTRUCCIONES DEBERÁN IR SEPARADAS POR LINEAS.
>  - SOLO SE PUEDE INTRODUCIR UNA PALABRA POR SENTENCIA
>  - DA IGUAL SI ES MAYUSCULA O MINUSCULA.
>

Tras escribir la sentencia deseada, se deberá hacer click en el botón **EXECUTE**, una vez hecho eso se verá en el campo **OUTPUT** el texto resultante y en **COMMAND CONTROL** el listado de ejecución de comandos.

El botón **DOWNLOAD PDF** permitirá descargarte un PDF con el output del texto y la ejecución de los comandos.

### EXPLICACION BASICA DEL PROGRAMA
El codigo implementa una variedad de archivos.

  - **mv1.py:** Es el archivo dedicado a la Máquina Virtual. Cuenta con la inicialización de todas instrucciones del programa , así como sus funciones.
  - **app.py:** Contiene Flask y las rutas de servidor, con las ejecuciones que van a llevar cada una.
  - **genQrCode.py:** Es el archivo dedicado a la generación del codigo QR, donde hay que cambiar la URL y tras ejecutarlo, introducir la imagen en la carpeta static.
  - **templates/index.html:** Contiene la estructura de l página web.
  - **static/style.css:** Contiene el formato de la página web.
  - **static/qrcode.png:** Contiene la imagen del codigo QR.
  - **static/textify.png:** Contiene la imagen del logo de Textify VM.

# Funcionalidades de la Máquina Virtual
### Métodos Principales

- **__init__():** Constructor de la clase, aquí se inicializan las 5 pilas que usará el programa, y el listado de instrucciones.
  
  Para este editor de texto, queríamos usar la menor cantidad de pilas posibles, pero evitando que se produzcan fallos porque dos funciones quieran entrar a la vez a alguna pila por ello hemos usado las       siguientes:
  - changeStack: Pila principal donde se guarda el texto que se escribe y las modificaciones que se hacen.
  - redoStack: Pila que se encarga de guardar los cambios de UNDO y REDO.
  - copyStack: Pila que se encarga de guardar los cambios de COPY y PASTE.
  - instructions: Pila encargada de almacenar las instrucciones del usuario.
  - messages: Pila encargada de almacenar los mensajes que se van a mostrar al usaurio.
  - changeReplaceWord: Pila encargada de almacenar las palabras que se van a reemplazar.
  - Translator(): Se inicia la clase translator para poder traducir textos.
      
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
- **REPLACE:** Reemplaza una palabra existente por otra que el usuario elija.
- **TRANSLATE:** Traduce el texto original al idioma pedido
- **HELP:** Muestra un pequeño mensaje mostrando todos los comando disponibles
- **HELPTRANSLATE:** Muestra un pequeño mensaje de como se debe usar la funcion *Translate*
>[!NOTE]
>**TODOS LOS COMANDO MOSTRARÁN UN MENSAJE DE ERROR SI NO PUEDEN EJECUTAR LA INSTRUCCIÓN**

# Métodos de operación sobre las pilas
- **writeText(text):**  Agrega el texto solicitado a la pila de cambios.
- **undo():**  Deshace el último cambio realizado guardado en la pila se cambios. Guarda la palabra cambiada en la pila para poder hacer un REDO.
- **redo():**  Rehace el último cambio deshecho.
- **copyWord(palabra):**  Copia la palabra del texto actual que el usuario pase como parametro de la función. Se guarda en la pila copyStack, para poder ser utilizada por la función PASTE.
- **pasteWord():**   Pega la última palabra copiada al texto actual. Cuando se ejecuta la función la palabra no sale de la pila, para poder ser pegada mas veces
- **clearRedo():** Función para limpiar la pila del REDO
- **getCurrentText():**  Función que se usa para obtener el texto actual, simplemente para uso entre funciones.
- **showAddedText():** Función para mostar al usuario el texto actual.
- **upper():** Función para pasar todo el texto a mayúsculas.
- **lower():** Función para pasar todo el texto a minúsculas.
- **clear():** Función para borrar todos los mensajes de la terminal.
- **replaceWord(original_word, new_word):** Función para reemplazar palabras.
- **translateText(target_language)**: Funcion para traducir el texto. El parametro de entrada será el idioma al que se quiere traducir, introduciendo las dos primeras letras (en = English, es = Spanish)
- **help():** Funcion que muestra todos los comandos disponibles usando la pila de mensajes.


### OTROS ELEMENTOS DEL PROGRAMA
Como se ha indicado antes, este editor de texto cuenta con una pequeña página web que permite ver al usuario de una manera mas sencilla que es lo que se está ejecutando.

Esta página se divide en tres secciones
  - Título + QR Code: Un código QR que nos lleva directamente a este repositorio.
  - Intrucciones: Una pequeña definicion de como funciona el editor y de como escribir los comandos.
  - OUTPUT: Es donde se mostrará el texto directamente
  - Command Control: Se muestra el control de los comando utilizados por el usuario.
  - PDF Downloader: Se ha implementado una libreria para poder descargar los textos en formato PDF.
  - Save File: Se ha implementado la posibilidad de descargar archivos .tfy para guardar el texto escrito.
  - Load File: Se ha implementado la posibilidad de cargar archivos .tfy con el contenido de los textos.


>[!NOTE]
>### DOCUMENTACIÓN
> 
>
> **CHAT GPT 4**
>
> **PYTHON DOC**
>
> **JavaScript DOC**
>
> **HTML DOC**
>
> **CSS DOC**
>
> **FLASK DOC**
>
> **JSPDF DOC**
>
> **QRCODE DOC**
>
