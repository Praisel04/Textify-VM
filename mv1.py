import argparse
from googletrans import Translator  #We added the library to be able to use the Google translator

# CODIGO REALIZADO POR :
#     Iván Seco
#     Mario Suarez del Hierro
#     Javier Poza Garijo
# FECHA DE INICIO: 14/10/2024 
# ULTIMA MODIFICACION: 21/10/2024

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
    TRANSLATE = "TRANSLATE"
    HELP = "HELP"

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
        self.changereplaceWord = []
        self.changeStack = []
        self.redoStack = []         
        self.copyStack = []         
        self.instructions = []    
        self.messages = [] 
        self.translator = Translator()

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
            elif command.upper() == self.HELP:
                self.help()
            elif command.upper() == self.REPLACE:
                if len(instr) > 2:
                    original_word = instr[1]
                    new_word = instr[2]
                    self.replaceWord(original_word, new_word)
            elif command.upper() == self.TRANSLATE:
                target_lang = instr[1] if len(instr) > 1 else "en"
                self.translateText(target_lang)
                
            else:
                self.messages.append("Invalid or empty command.")

    def reset(self):
        """
        Reset the stacks (changeStack, redoStack, copyStack) to their initial state.
        """
        self.changereplaceWord = []
        self.changeStack = []
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
            self.changeStack.append(text)
            self.messages.append(f"Executing writeText fuction. Text has been written. Current text: {self.getCurrentText()}")

    def undo(self):
        """
        FUNCTION undo
        This function undoes the last action made in the main stack and storing it. 
        """

        if len(self.changeStack) > 0:
            if len(self.changereplaceWord) > 0:     #   I check if the changereplaceWord variable has something
                self.redoStack.append(self.changeStack.copy())  # Save the removed change for redo
                self.changeStack = self.changereplaceWord.pop()  # Restore the last full state
                self.messages.append(f"Undo performed. Current text: {self.getCurrentText()}")
            else:
                last_change = self.changeStack.pop()  # Remove last change
                self.redoStack.append(last_change)  # Save the removed change for redo
                self.messages.append(f"Undo performed. Current text: {self.getCurrentText()}")
        else:
            self.messages.append("Executing undo function. No more changes to undo.")

    def redo(self):
        
        """
        Function redo
        This function redoes the last undone action made in the main stack and stores it. 

        """
        if len(self.redoStack) > 0:
            if self.redoStack and isinstance(self.redoStack[-1], list): # I check if the last element in copy is a full state (a list)
                self.changeStack = self.redoStack.pop()  #Redo last change
                self.messages.append(f"Undo to previous state. Current text: {self.getCurrentText()}")
            else:
                redone_text = self.redoStack.pop()  # Redo last change
                self.changeStack.append(redone_text)  # Save in changes
                self.messages.append(f"Executing redo fuction. Redo performed. Current text: {self.getCurrentText()}")
        else:
             self.messages.append("Executing redo fuction. No more changes to redo.")

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
            self.messages.append(f"Executing copyWord fuction. Word '{word}' copied.")
        else:
            self.messages.append(f"Executing copyWord fuction. The word '{word}' is not found in the current text.")

    def pasteWord(self):
        """
        Function pasteWord
        This function takes the last copied word from the copy stack and adds it to the current text.
        
        """
        if len(self.copyStack) > 0:
            word = self.copyStack[-1]
            self.changeStack.append(word)
            self.messages.append(f"Executing pasteWord fuction. Word '{word}' pasted into the current text.")
        else:
           self.messages.append("Executing pasteWord fuction. There is no word copied.")

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
            self.messages.append(f"Executing showAddedText fuction. The current text is: '{self.getCurrentText()}'")
        else:
            self.messages.append("Executing showAddedText fuction. Cannot display the last element from the stack because it is empty.")

    def upper(self):
        
        """
        Upper function
        This function converts the current text to uppercase and stores it in the stack.
        It clears the current stack and adds the new uppercase text to it.
        """
        mayustext = self.getCurrentText().upper()
        self.changeStack.clear()
        self.changeStack.append(mayustext)
        self.messages.append(f"Executing mayus fuction. Current text: {mayustext}")

    def lower(self):
        
        
        """
        Lower function
        This function converts the current text to lowercase and stores it in the stack.
        It clears the current stack and adds the new lowercase text to it.
        """
        lowertext = self.getCurrentText().lower()
        self.changeStack.clear()
        self.changeStack.append(lowertext)
        self.messages.append(f"Executing lower fuction. Current text: {lowertext}")

    def clear(self):
        """
        Clear everything from the change stack.

        This function deletes everything has been written in the stack.
        If the stack is empty, it notifies the user.
        """

        if len(self.changeStack) > 0:
           self.changeStack.clear()
           self.messages.append("Executing clear function. Text has been deleted correctly")
        else:
            self.messages.append("Executing clear function. There is not text in the stack.")  
            
    
    def replaceWord(self, original, new_word):
        """
        Replace words
        
        This function searches for and replaces an existing word in the text stored in the stack with a new word.
        If the original word is not found, it returns an error message indicating that the word is not stored in the stack.

        Args:
            original (string): This arg is the word that is going to be replaced.
            new_word (string): This arg is the word that is going to replace.
        """
        
        encontrar = False 
            
        # Save the complete state of the changeStack before performing the replacement
        previous_state = self.changeStack.copy()

        
        for i in range(len(self.changeStack)):
            if self.changeStack[i] == original:
                self.changeStack[i] = new_word  # Replace the word
                encontrar = True

        if encontrar:
            self.changereplaceWord = []  # Clean changereplaceWord
            self.changereplaceWord.append(previous_state)  # Save previous state in changereplaceWord
            self.messages.append(f"Replaced '{original}' with '{new_word}'. Current text: {self.getCurrentText()}")
        else:
            self.messages.append(f"Word '{original}' not found in the current text.")


    def translateText(self, target_language):
            """
            Function to translate the current text to the specified language.
            
            Args:
                target_language (string): Target language code (e.g., 'en' for English, 'es' for Spanish).
            """
            
            valid_languages = {
            'af', 'sq', 'ar', 'hy', 'az', 'be', 'bg', 'ca', 'cs', 'zh-CN', 'zh-TW',
            'hr', 'da', 'sk', 'sl', 'es', 'et', 'tl', 'fi', 'fr', 'gl', 'ka', 'de',
            'el', 'he', 'hi', 'hu', 'is', 'it', 'ja', 'jv', 'ko', 'lv', 'lt', 'mk',
            'ms', 'mt', 'nl', 'no', 'fa', 'pl', 'pt', 'ro', 'ru', 'sr', 'sv', 'th',
            'tr', 'uk', 'ur', 'vi', 'cy', 'xh', 'yo', 'zu'}
                
            # Save the complete state of the changeStack before performing the replacement
            previous_state2 = self.changeStack.copy()
            target_lower = target_language.lower()
            
            if target_lower not in valid_languages:  # We verify that the chosen language is valid
                self.messages.append(f"Invalid target language: '{target_lower}'. Please use a valid language code.")
            else:
                if self.changeStack:    #If the language is valid
                    
                    current_text = self.getCurrentText()    
                    translation = self.translator.translate(current_text, dest=target_lower).text
                    translated_words = translation.split() # Split the translated text into words
                    
                    self.changeStack.clear()  # Clean changeStack
                    self.changeStack.extend(translated_words)  # Add the translate text to changeStack
                    
                    self.changereplaceWord = []  # Clean changereplaceWord
                    self.changereplaceWord.append(previous_state2)  # Save previous state in changereplaceWord
                    self.messages.append(f"Text translated to {target_lower}. Translated text: {translation}")
                else:
                    self.messages.append("No text to translate.")



    def help(self):
        """
        Help function
        This function shows the available arguments for the program.
        The arguments are: writeText <text> | undo | redo | copyWord <word> | pasteWord | clear | show | upper | lower | clear | help | exit
        """
        self.messages.append("Arguments availables: writeText <text> | undo | redo | copyWord <word> | pasteWord | clear | show | upper | lower | clear | help | exit")
        self.messages.append("For more information, please refer to the README.md file in the QR code.")


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
