from flask import Flask, request, jsonify
from mv1 import VirtualMachine 
from flask import render_template

app = Flask(__name__)

@app.route('/execute', methods=['POST'])
def execute():
    """
    Handle the execution of instructions sent from the frontend.

    This function receives a JSON payload containing a list of instructions,
    creates an instance of the VirtualMachine, loads the instructions into
    the machine, and executes them. After execution, it returns the current
    text and any messages generated during execution as a JSON response.

    Returns:
        Response: A JSON response containing the resulting text and execution messages.
    """
    data = request.json  # Recibe las instrucciones enviadas desde el frontend
    instructions = data.get('instructions', [])

    # Crear una instancia de la máquina virtual
    machine = VirtualMachine()

    # Cargar las instrucciones y ejecutarlas
    machine.loadProgram(instructions)
    machine.execute()

    # Devolver el texto actual y los mensajes de la ejecución
    return jsonify({
        'result': machine.getCurrentText(),
        'messages': machine.messages  # Enviar todos los mensajes capturados
    })

# Ruta para la página principal (GET request)
@app.route('/')
def index():
    
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)

