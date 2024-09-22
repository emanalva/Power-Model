// *****************************************
// Author:   Emanuel A.
// Date:     09/22/2024
// Project:  Power-Model
// 
// Purpose:  JavaScript for handling form submission.
// *****************************************

document.getElementById('power-form').addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent page reload

    // Gather form data
    const formData = new FormData(this);

    // Send data to Flask
    fetch('/calculate', {
        method: 'POST',
        body: formData
    })
    .then(response => response.text()) // Get the response from Flask
    .then(data => {
        // Insert the results into the results div
        document.getElementById('results').innerHTML = data;
    })
    .catch(error => console.error('Error:', error));
});
