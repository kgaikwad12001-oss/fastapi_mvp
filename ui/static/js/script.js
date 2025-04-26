// generate code for the script.js file
// This script handles the functionality of the web application
// including the form submission, displaying the results, and handling errors.

// Function to handle form submission
function handleFormSubmit(event) {
    event.preventDefault(); // Prevent the default form submission behavior

    // Get the input values from the form
    const inputText = document.getElementById('inputText').value;
    const inputFile = document.getElementById('inputFile').files[0];

    // Validate the input values
    if (!inputText && !inputFile) {
        alert('Please provide either text or a file.');
        return;
    }

    // Create a FormData object to send the data to the server
    const formData = new FormData();
    if (inputText) {
        formData.append('text', inputText);
    }
    if (inputFile) {
        formData.append('file', inputFile);
    }

    // Send the data to the server using fetch API
    fetch('/process', {
        method: 'POST',
        body: formData,
    })
        .then(response => response.json())
        .then(data => {
            // Display the results in the results section
            displayResults(data);
        })
        .catch(error => {
            console.error('Error:', error);
            alert('An error occurred while processing your request. Please try again later.');
        });
}

