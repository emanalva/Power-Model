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
            configButtons.forEach(btn => {
                btn.classList.remove('bg-blue-500', 'text-white');
                btn.classList.add('bg-gray-200', 'text-black');
            });
            button.classList.remove('bg-gray-200', 'text-black');
            button.classList.add('bg-blue-500', 'text-white');
            document.getElementById('connection').value = button.getAttribute('data-value');
        });
    });

    // Handle Voltage type (Phase/Line) buttons
    const voltageButtons = document.querySelectorAll('.voltage-button');
    voltageButtons.forEach(button => {
        button.addEventListener('click', function() {
            voltageButtons.forEach(btn => {
                btn.classList.remove('bg-blue-500', 'text-white');
                btn.classList.add('bg-gray-200', 'text-black');
            });
            button.classList.remove('bg-gray-200', 'text-black');
            button.classList.add('bg-blue-500', 'text-white');
            document.getElementById('voltage_type').value = button.getAttribute('data-value');
        });
    });

    // Handle Current type (Phase/Line) buttons
    const currentButtons = document.querySelectorAll('.current-button');
    currentButtons.forEach(button => {
        button.addEventListener('click', function() {
            currentButtons.forEach(btn => {
                btn.classList.remove('bg-blue-500', 'text-white');
                btn.classList.add('bg-gray-200', 'text-black');
            });
            button.classList.remove('bg-gray-200', 'text-black');
            button.classList.add('bg-blue-500', 'text-white');
            document.getElementById('current_type').value = button.getAttribute('data-value');
        });
    });

    // Handle Random Values Button
    document.getElementById('random-values-button').addEventListener('click', function() {
        // Generate random values for voltage and current
        const randomVoltage = Math.floor(Math.random() * 241); // 0 to 240
        const randomCurrent = Math.floor(Math.random() * 101); // 0 to 100
    
        // Randomly select Wye (Y) or Delta (Δ)
        const randomConnection = Math.random() < 0.5 ? 'wye' : 'delta';
    
        // Randomly select Phase or Line for voltage
        const randomVoltageType = Math.random() < 0.5 ? 'phase' : 'line';
    
        // Randomly select Phase or Line for current
        const randomCurrentType = Math.random() < 0.5 ? 'phase' : 'line';
    
        // Set the random values in the input fields
        document.getElementById('voltage').value = randomVoltage;
        document.getElementById('current').value = randomCurrent;
    
        // Set the random values for connection, voltage type, and current type
        document.getElementById('connection').value = randomConnection;
        document.getElementById('voltage_type').value = randomVoltageType;
        document.getElementById('current_type').value = randomCurrentType;
    
        // Update button visuals for Wye/Delta
        configButtons.forEach(btn => {
            btn.classList.remove('bg-blue-600', 'text-white');
            btn.classList.add('bg-gray-200', 'text-black');
        });
        document.querySelector(`.${randomConnection}-button`).classList.add('bg-blue-600', 'text-white');
    
        // Update button visuals for Voltage Type (Phase/Line)
        voltageButtons.forEach(btn => {
            btn.classList.remove('bg-blue-600', 'text-white');
            btn.classList.add('bg-gray-200', 'text-black');
        });
        document.querySelector(`.${randomVoltageType}-button`).classList.add('bg-blue-600', 'text-white');
    
        // Update button visuals for Current Type (Phase/Line)
        currentButtons.forEach(btn => {
            btn.classList.remove('bg-blue-600', 'text-white');
            btn.classList.add('bg-gray-200', 'text-black');
        });
        document.querySelector(`.current-button.${randomCurrentType}-button`).classList.add('bg-blue-600', 'text-white');
    
        // Automatically submit the form after the random values are set
        submitFormWithFetch();
    });    

    // Function to handle form submission using fetch
    function submitFormWithFetch() {
        // Gather form data
        const formData = new FormData(document.getElementById('power-form'));

        // Check if at least two fields (voltage, current, resistor, power) are filled
        const voltage = formData.get('voltage');
        const current = formData.get('current');
        const resistor = formData.get('resistor');
        const power = formData.get('power');
        let filledFields = 0;

        // Increment for each filled field
        [voltage, current, resistor, power].forEach(field => {
            if (field) filledFields++;
        });

        // If fewer than 2 fields are filled, alert the user and don't submit
        if (filledFields < 2) {
            alert('Please fill two fields to calculate.');
            return;  // Exit the function without making the API call
        }

        // Check if all entered values are greater than 0 (if they are present)
        if ((voltage && voltage <= 0) || 
            (current && current <= 0) || 
            (resistor && resistor <= 0) || 
            (power && power <= 0)) {
            alert('Please enter positive values greater than zero for both intended fields.');
            return;  // Exit the function without making the API call
        }

        // Send data to Flask via fetch
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
    }

    // Handle Form Submission via the Calculate button
    document.getElementById('power-form').addEventListener('submit', function(event) {
        event.preventDefault(); // Prevent page reload

        // Call the same function to submit form via fetch
        submitFormWithFetch();
    });
});
