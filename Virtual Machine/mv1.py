import copy

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
    UPPER = "UPPER"
    LOWER = "LOWER"
    CLEAR = "CLEAR"
    REPLACE = "REPLACE"

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
        self.undoStack = []  # Stack to store states for undo
        self.redoStack = []  # Stack to store states for redo
        self.copyStack = []
        self.instructions = []
        self.messages = []

    def loadProgram(self, instructions):
        """
        Function in charge of loading the instructions on the virtual machine

        Args:
            instructions (list): List of instructions
            
        """
        self.reset()
        self.instructions = instructions

    def execute(self):
        """Execute the loaded instructions in the machine"""
        for instr in self.instructions:
            command = instr[0]
            if command.upper() == self.UNDO:
                self.undo()
            elif command.upper() == self.REDO:
                self.redo()
            elif command.upper() == self.COPY:
                word = instr[1] if len(instr) > 1 else ""
                self.copyWord(word)
            elif command.upper() == self.PASTE:
                self.pasteWord()
            elif command.upper() == self.WRITE:
                text = instr[1] if len(instr) > 1 else ""
                self.writeText(text)
            elif command.upper() == self.SHOW:
                self.showAddedText()
            elif command.upper() == self.UPPER:
                self.upper()
            elif command.upper() == self.LOWER:
                self.lower()
            elif command.upper() == self.CLEAR:
                self.clear()
            elif command.upper() == self.REPLACE:
                if len(instr) > 2:
                    original_word = instr[1]
                    new_word = instr[2]
                    self.replaceWord(original_word, new_word)
            else:
                self.messages.append("Invalid or empty command.")

    def reset(self):
        """
        Reset the stacks (changeStack, redoStack, copyStack) to their initial state.
        """
        self.changeStack = []
        self.undoStack = []
        self.redoStack = []
        self.copyStack = []
        self.messages = []

    # Stack operation methods

    def writeText(self, text):
        """
        Function writeText
        This fuction takes a word as a parameter, stack it and then print it.

        Args:
            text (string): This arg takes the word that is going to be write and append it inside the stack.
        """
        if text:
            self.saveToUndo()  # Save current state to undo stack
            self.changeStack.append(text)
            self.clearRedo()
            self.messages.append(f"Executing writeText function. Current text: {self.getCurrentText()}")

    def undo(self):
        """
        FUNCTION undo
        This function undoes the last action made in the main stack and storing it. 
        """
        if len(self.undoStack) > 0:
            # Move current state to redo stack before undoing
            self.redoStack.append(copy.deepcopy(self.changeStack))
            # Restore the last state from the undo stack
            self.changeStack = self.undoStack.pop()
            self.messages.append(f"Undo performed. Current text: {self.getCurrentText()}")
        else:
            self.messages.append("No more changes to undo.")

    def redo(self):
        """
        Function redo
        This function redoes the last undone action made in the main stack and stores it. 

        """
        if len(self.redoStack) > 0:
            # Save current state to undo stack before redoing
            self.undoStack.append(copy.deepcopy(self.changeStack))
            # Restore the state from the redo stack
            self.changeStack = self.redoStack.pop()
            self.messages.append(f"Redo performed. Current text: {self.getCurrentText()}")
        else:
            self.messages.append("No more changes to redo.")

    def copyWord(self, word):
        """
        Function copyWord
        This function takes a word as a parameter, searches for it in the current text, and if it is found, it is copied to the copy stack.

        Args:
            word (string): This arg takes the word to be searched and copied.
            
        """
        if word in self.getCurrentText():
            if len(self.copyStack) > 0:
                self.copyStack.pop()
            self.copyStack.append(word)
            self.messages.append(f"Word '{word}' copied.")
        else:
            self.messages.append(f"The word '{word}' is not found in the current text.")

    def pasteWord(self):
        """
        Function pasteWord
        This function takes the last copied word from the copy stack and adds it to the current text.
        
        """
        if len(self.copyStack) > 0:
            word = self.copyStack[-1]
            self.saveToUndo()  # Save current state to undo stack before pasting
            self.changeStack.append(word)
            self.messages.append(f"Word '{word}' pasted into the current text.")
        else:
            self.messages.append("There is no word copied.")

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
            self.messages.append(f"The current text is: '{self.getCurrentText()}'")
        else:
            self.messages.append("Cannot display the last element from the stack because it is empty.")

    def upper(self):
        self.saveToUndo()  # Save current state to undo stack before changing case
        upper_text = self.getCurrentText().upper()
        self.changeStack.clear()
        self.changeStack.append(upper_text)
        self.clearRedo()
        self.messages.append(f"Current text: {upper_text}")

    def lower(self):
        self.saveToUndo()  # Save current state to undo stack before changing case
        lower_text = self.getCurrentText().lower()
        self.changeStack.clear()
        self.changeStack.append(lower_text)
        self.clearRedo()
        self.messages.append(f"Current text: {lower_text}")

    def clear(self):
        """
        Clear everything from the change stack.

        This function deletes everything has been written in the stack.
        If the stack is empty, it notifies the user.
        """
        if len(self.changeStack) > 0:
            self.saveToUndo()  # Save current state to undo stack before clearing
            self.changeStack = []
            self.clearRedo()
            self.messages.append("Text has been deleted.")
        else:
            self.messages.append("There is no text in the stack.")

    def replaceWord(self, original, new_word):
        """
        Replace words
        
        This function searches for and replaces an existing word in the text stored in the stack with a new word.
        If the original word is not found, it returns an error message indicating that the word is not stored in the stack.

        Args:
            original (string): This arg is the word that is going to be replaced.
            new_word (string): This arg is the word that is going to replace.
        """
        current_text = self.changeStack
        encontrar = False

        # Save the current state to undo stack before modifying
        self.saveToUndo()

        # Create a temporary stack to hold the new words
        temp_stack = []
        
        # Iterate through the current stack
        for word in current_text:
            if word == original:
                temp_stack.append(new_word)  # Replace the word
                encontrar = True
            else:
                temp_stack.append(word)  # Keep the original word

        if encontrar:
            # Update the changeStack with the modified text
            self.changeStack = temp_stack
            self.clearRedo()  # Clear redo stack since this is a new change
            self.messages.append(f"Replaced '{original}' with '{new_word}'. Current text: {self.getCurrentText()}")
        else:
            self.messages.append(f"Word '{original}' not found in the current text.")



    def saveToUndo(self):
        """ Save the current state to the undo stack """
        self.undoStack.append(copy.deepcopy(self.changeStack))

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
    import argparse
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

