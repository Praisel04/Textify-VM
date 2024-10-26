 // Create a variable to save all the messages
 var messagesList = [];


 function executeInstructions() {
     const instructionsText = document.getElementById('instructions').value;
     const instructions = instructionsText.split('\n').map(line => line.split(' '));

     fetch('/execute', {
         method: 'POST',
         headers: {
             'Content-Type': 'application/json',
         },
         body: JSON.stringify({ instructions: instructions })
     })
         .then(response => response.json())
         .then(data => {
             document.getElementById('output').textContent = data.result;
             messagesList = data.messages;
             document.getElementById('messages').innerHTML = data.messages.join('<br>');
         })
         .catch(error => {
             console.error('Error:', error);
         });


 }

 function saveFile() {
     const text = document.getElementById('instructions').value;
     const blob = new Blob([text], { type: 'text/plain' });
     const link = document.createElement('a');
     link.href = URL.createObjectURL(blob);
     link.download = 'instructions.tfy';
     link.click();
 }

 function loadFile(event) {
     const file = event.target.files[0];
     if (file) {
         const reader = new FileReader();
         reader.onload = function (e) {
             document.getElementById('instructions').value = e.target.result;
         }
         reader.readAsText(file);
     }
 }

 function downloadPDF() {
     // Create a new PDF
     const { jsPDF } = window.jspdf;
     // Create the document
     const doc = new jsPDF(
     );

     // Default text of the PDF
     const defaultText = "Thanks for using our Text Editor. We hope you enjoyed it.\n\nFor more info about the project, visit: \nhttps://github.com/Praisel04/VirtualMachine";

     // Obtain the text of the field with the ID selected
     const outputText = document.getElementById('output').textContent;
     // Replace the BR of the previous fuction with \n
     const messageText = document.getElementById('messages').textContent.replace("<br>", "\n");



     // Add the Default text to the designated coordinates
     doc.text(defaultText, 10, 20);

     // Add the Output text to the desiganted coordinates
     doc.text("Output:", 10, 60);
     doc.text(outputText, 10, 70);

     // Add the Command Control messages to the designated coordinates
     doc.text("Messages:", 10, 100);
     // Use FOR to print the messages in different Y positions
     for (i in messagesList) {
         doc.text(messagesList[i], 10, 110 + i * 10);
     }



     // Download the PDF
     doc.save('soria.pdf');
 }