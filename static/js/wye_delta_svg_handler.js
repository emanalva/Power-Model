// *****************************************
// Author:   Emanuel A.
// Date:     09/22/2024
// Project:  Power-Model
// 
// Purpose:  JavaScript for handling wye_and_delta_diagram.svg.
// *****************************************

document.addEventListener("DOMContentLoaded", function() {
    // Listen for form submission
    document.getElementById('power-form').addEventListener('submit', function(event) {
        event.preventDefault();  // Prevent the form from refreshing the page

        // Get the results from the calculation or form
        const enteredVoltage = document.querySelector('[name="voltage"]').value || 120; // Default 120V if empty
        const enteredCurrent = document.querySelector('[name="current"]').value || (enteredVoltage / 10).toFixed(2); // Default if current is empty
        const enteredResistor = document.querySelector('[name="resistor"]').value || 10; // Default 10Ω if empty

        // Update the Wye voltage and current values in the SVG
        document.getElementById('wye-voltage-va').textContent = `V_a = ${enteredVoltage} V`;
        document.getElementById('wye-current-ia').textContent = `I_a = ${enteredCurrent} A`;
        document.getElementById('wye-resistance-ra').textContent = `R_a = ${enteredResistor} Ω`;

        // Similarly, update other elements like Wye, Delta values depending on the configuration
        const connectionType = document.querySelector('[name="connection"]').value;
        
        if (connectionType === 'delta') {
            document.getElementById('delta-voltage-va').textContent = `V_a = ${enteredVoltage} V`;
            document.getElementById('delta-current-iline1').textContent = `I_line1 = ${enteredCurrent} A`;
            document.getElementById('delta-resistance-rab').textContent = `R_ab = ${enteredResistor} Ω`;
        }
    });
});