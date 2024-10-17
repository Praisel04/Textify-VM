import argparse

class VirtualMachine:

    """
    Initialization of the variables that represent the program instructions

    """
    
    # Instructions
    UNDO = "UNDO"
    REDO = "REDO"
    COPY = "COPY"
    PASTE = "PASTE"
    WRITE = "WRITE"
    SHOW = "SHOW"

    def __init__(self):
    # Necessary stacks for the Virtual Machine
        """
        Constructor for the VirtualMachine class.

        This method initializes the necessary stacks for the Virtual Machine:
        - changeStack: Main stack for text changes (undo)
        - redoStack: Secondary stack for redo
        - copyStack: Stack for copy-paste
        - instructions: List to store instructions

        """

        self.changeStack = []      
        self.redoStack = []         
        self.copyStack = []         
        self.instructions = []     

    def loadProgram(self, instructions):
        """
        Function in charge of loading the instructions on the virtual machine

        Args:
            instructions (list): List of instructions
            
        """
        self.reset()
        self.instructions = instructions  # Load the instruction list

    def execute(self):
        """Execute the loaded instructions in the machine"""
        for instr in self.instructions:
            command = instr[0]
            if command == self.UNDO:
                self.undo()
            elif command == self.REDO:
                self.redo()
            elif command == self.COPY:
                word = instr[1] if len(instr) > 1 else ""
                self.copyWord(word)
            elif command == self.PASTE:
                self.pasteWord()
            elif command == self.WRITE:
                text = instr[1] if len(instr) > 1 else ""
                self.writeText(text)
            elif command == self.SHOW:
                    self.showAddedText()

    def reset(self):
        """
        Reset the stacks (changeStack, redoStack, copyStack) to their initial state.
        """
        self.changeStack = []
        self.redoStack = []
        self.copyStack = []


    # Stack operation methods

    def writeText(self, text):
        """
        Function writeText
        This fuction takes a word as a parameter, stack it and then print it.

        Args:
            text (string): This arg takes the word that is going to be write and append it inside the stack.
        """
        if text:
            self.changeStack.append(text)
            self.clearRedo()  # Clear redo stack when new text is added
        print(f"Text has been written. Current text: {self.getCurrentText()}")

    def undo(self):
        """
        FUNCTION undo
        This function undoes the last action made in the main stack and storing it. 
        """
        
        if len(self.changeStack) > 0:
            last_change = self.changeStack.pop()  # Remove last change
            self.redoStack.append(last_change)  # Save in redo
            print(f"Undo performed. Current text: {self.getCurrentText()}")
        else:
            print("No more changes to undo.")

    def redo(self):
        
        """
        Function redo
        This function redoes the last undone action made in the main stack and stores it. 

        """
        if len(self.redoStack) > 0:
            redone_text = self.redoStack.pop()  # Redo last change
            self.changeStack.append(redone_text)  # Save in changes
            print(f"Redo performed. Current text: {self.getCurrentText()}")
        else:
            print("No more changes to redo.")

    def copyWord(self, word):
        """
        Function copyWord
        This function takes a word as a parameter, searches for it in the current text, and if it is found, it is copied to the copy stack.

        Args:
            word (string): This arg takes the word to be searched and copied.
            
        """
        if word in self.getCurrentText():
            if len(self.copyStack) > 0:
                self.copyStack.pop()  # Empty any previously copied word
            self.copyStack.append(word)
            print(f"Word '{word}' copied.")
        else:
            print(f"The word '{word}' is not found in the current text.")

    def pasteWord(self):
        """
        Function pasteWord
        This function takes the last copied word from the copy stack and adds it to the current text.
        
        """
        if len(self.copyStack) > 0:
            word = self.copyStack[-1]
            self.changeStack.append(word)
            print(f"Word '{word}' pasted into the current text.")
        else:
            print("There is no word copied.")

    def clearRedo(self):
        """
        Clear the redo stack when a new change is made

        """
        self.redoStack = []

    def getCurrentText(self):
        """
        Get the current text by concatenating all changes

        Returns:
            str: The current text
        """
        return ' '.join(self.changeStack)
    
    def showAddedText(self):
        """
        Show the last added text from the change stack.
        
        This function retrieves the last element from the change stack and displays it.
        If the stack is empty, it notifies the user.
        """

        last_text = self.changeStack[-1] if len(self.changeStack) > 0 else None
        if last_text is not None:
            print(f"The current text is: '{self.getCurrentText()}'")
        else:
            print("Cannot display the last element from the stack because it is empty.")


# Function to read the custom text file
def read_instructions_from_file(file):
    """ 
    Read instructions from a custom text file

    The instructions are read line by line. Each line is split into a command and arguments.
    The command is the first part of the line, and the arguments are the rest of the line.
    The instructions are returned as a list of lists, where each sublist contains a command and its arguments.

    Args:
        file (str): The path to the custom text file

    Returns:
        list: A list of instructions, where each instruction is a list containing a command and its arguments
    """

    instructions = []
    with open(file, 'r') as f:
        for line in f:
            parts = line.strip().split(' ')
            command = parts[0]
            arguments = parts[1:]  # Rest of the line as arguments
            instructions.append([command] + arguments)
    return instructions


# Set up argparse to accept command-line arguments
if __name__ == "__main__":
    
    parser = argparse.ArgumentParser(description="Simple virtual machine to execute instructions from a file.")
    parser.add_argument('file', type=str, help="The text file with instructions")
    args = parser.parse_args()

    # Read instructions from the file
    instructions = read_instructions_from_file(args.file)

    # Create an instance of the virtual machine
    machine = VirtualMachine()

    # Load the instructions and execute them
    machine.loadProgram(instructions)
    machine.execute()
