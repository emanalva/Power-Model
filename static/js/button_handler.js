// *****************************************
// Author:   Emanuel A.
// Date:     09/23/2024
// Project:  Power-Model
// 
// Purpose:  Combined JavaScript for handling button selections and form submission.
// *****************************************
document.addEventListener("DOMContentLoaded", function() {

    // Handle Configuration (Wye/Delta) buttons
    const configButtons = document.querySelectorAll('.config-button');
    configButtons.forEach(button => {
        button.addEventListener('click', function() {
            // Remove 'selected' state from all buttons
            configButtons.forEach(btn => {
                btn.classList.remove('bg-blue-500', 'text-white');
                btn.classList.add('bg-gray-200', 'text-black');
            });

            // Add 'selected' state to the clicked button
            button.classList.remove('bg-gray-200', 'text-black');
            button.classList.add('bg-blue-500', 'text-white');

            // Update hidden input value
            document.getElementById('connection').value = button.getAttribute('data-value');
        });
    });

    // Handle Voltage type (Phase/Line) buttons
    const voltageButtons = document.querySelectorAll('.voltage-button');
    voltageButtons.forEach(button => {
        button.addEventListener('click', function() {
            // Remove 'selected' state from all buttons
            voltageButtons.forEach(btn => {
                btn.classList.remove('bg-blue-500', 'text-white');
                btn.classList.add('bg-gray-200', 'text-black');
            });

            // Add 'selected' state to the clicked button
            button.classList.remove('bg-gray-200', 'text-black');
            button.classList.add('bg-blue-500', 'text-white');

            // Update hidden input value
            document.getElementById('voltage_type').value = button.getAttribute('data-value');
        });
    });

    // Handle Current type (Phase/Line) buttons
    const currentButtons = document.querySelectorAll('.current-button');
    currentButtons.forEach(button => {
        button.addEventListener('click', function() {
            // Remove 'selected' state from all buttons
            currentButtons.forEach(btn => {
                btn.classList.remove('bg-blue-500', 'text-white');
                btn.classList.add('bg-gray-200', 'text-black');
            });

            // Add 'selected' state to the clicked button
            button.classList.remove('bg-gray-200', 'text-black');
            button.classList.add('bg-blue-500', 'text-white');

            // Update hidden input value
            document.getElementById('current_type').value = button.getAttribute('data-value');
        });
    });

    // Handle Form Submission
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
});
