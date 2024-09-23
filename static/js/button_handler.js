// *****************************************
// Author:   Emanuel A.
// Date:     09/22/2024
// Project:  Power-Model
// 
// Purpose:  JavaScript for handling button selections for configuration, voltage, and current type.
// *****************************************

document.addEventListener("DOMContentLoaded", function() {
    
    // Handle Configuration (Wye/Delta) buttons
    const configButtons = document.querySelectorAll('.config-button');
    configButtons.forEach(button => {
        button.addEventListener('click', function() {
            configButtons.forEach(btn => btn.classList.remove('selected')); // Remove selected class from all
            button.classList.add('selected'); // Add selected class to clicked button
            document.getElementById('connection').value = button.getAttribute('data-value'); // Set hidden form field
        });
    });

    // Handle Voltage type (Phase/Line) buttons
    const voltageButtons = document.querySelectorAll('.voltage-button');
    voltageButtons.forEach(button => {
        button.addEventListener('click', function() {
            voltageButtons.forEach(btn => btn.classList.remove('selected')); // Remove selected class from all
            button.classList.add('selected'); // Add selected class to clicked button
            document.getElementById('voltage_type').value = button.getAttribute('data-value'); // Set hidden form field
        });
    });

    // Handle Current type (Phase/Line) buttons
    const currentButtons = document.querySelectorAll('.current-button');
    currentButtons.forEach(button => {
        button.addEventListener('click', function() {
            currentButtons.forEach(btn => btn.classList.remove('selected')); // Remove selected class from all
            button.classList.add('selected'); // Add selected class to clicked button
            document.getElementById('current_type').value = button.getAttribute('data-value'); // Set hidden form field
        });
    });

});
