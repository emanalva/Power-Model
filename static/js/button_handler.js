// *****************************************
// Author:   Emanuel A.
// Date:     09/23/2024
// Project:  Power-Model
// 
// Purpose:  Combined JavaScript for handling button selections and form submission.
// *****************************************
document.addEventListener("DOMContentLoaded", function() {
    // Dark Mode Toggle Logic
    const toggleButton = document.getElementById('toggle-dark-mode');
    const body = document.body; // Reference the body directly
    const titleBox = document.querySelector('.title-box'); // Selects the title box
    const calculatorBox = document.querySelector('.calculator-box'); // Selects the calculator box
    const labels = document.querySelectorAll('label'); // Selects all labels
    const buttons = document.querySelectorAll('button'); // Select all buttons
    const inputs = document.querySelectorAll('input[type="text"]'); // Selects all text inputs
    const title = document.querySelector('h1'); // Select the title (Power System Calculator)
    const submitButton = document.querySelector('input[type="submit"]'); // Select the "Calculate" button

    // Load previously saved mode from localStorage
    const savedMode = localStorage.getItem('darkMode');
    if (savedMode === 'enabled') {
        enableDarkMode();
    } else {
        disableDarkMode();
    }

    // Toggle button click event listener
    toggleButton.addEventListener('click', function () {
        const darkModeEnabled = body.classList.contains('bg-uniqueGrayBlack');

        if (darkModeEnabled) {
            disableDarkMode();
            toggleButton.textContent = "Dark Mode"; // Switch to Dark Mode text when dark mode is disabled
        } else {
            enableDarkMode();
            toggleButton.textContent = "Light Mode"; // Switch to Light Mode text when dark mode is enabled
        }
    });

    // Enable dark mode function
    function enableDarkMode() {
        // Update background and text color for body and components
        body.classList.replace('bg-white', 'bg-uniqueGrayBlack');
        titleBox.classList.replace('bg-gray-200', 'bg-uniqueDarkGray');
        calculatorBox.classList.replace('bg-gray-200', 'bg-uniqueDarkGray');

        // Change text color to white for all labels
        labels.forEach(label => {
            label.classList.replace('text-black', 'text-white');
        });

        // Change button text color and background
        buttons.forEach(button => {
            button.classList.replace('text-black', 'text-white');
        });

        // Change input boxes' background and keep text black
        inputs.forEach(input => {
            input.classList.replace('bg-white', 'bg-gray-300');
        });

        // Change title and submit button text color to white
        title.classList.replace('text-black', 'text-white');
        submitButton.classList.replace('text-black', 'text-white');

        localStorage.setItem('darkMode', 'enabled');
    }

    // Disable dark mode function
    function disableDarkMode() {
        // Revert background and text color for body and components
        body.classList.replace('bg-uniqueGrayBlack', 'bg-white');
        titleBox.classList.replace('bg-uniqueDarkGray', 'bg-gray-200');
        calculatorBox.classList.replace('bg-uniqueDarkGray', 'bg-gray-200');

        // Revert text color to black for all labels
        labels.forEach(label => {
            label.classList.replace('text-white', 'text-black');
        });

        // Revert button text color and background
        buttons.forEach(button => {
            button.classList.replace('text-white', 'text-black');
        });

        // Revert input boxes' background to white
        inputs.forEach(input => {
            input.classList.replace('bg-gray-300', 'bg-white');
        });

        // Revert title and submit button text color to black
        title.classList.replace('text-white', 'text-black');
        submitButton.classList.replace('text-white', 'text-black');

        localStorage.setItem('darkMode', 'disabled');
    }

    // Handle Configuration (Wye/Delta) buttons
    const configButtons = document.querySelectorAll('.config-button');
    configButtons.forEach(button => {
        button.addEventListener('click', function() {
            configButtons.forEach(btn => {
                btn.classList.remove('bg-blue-400', 'text-white');
                btn.classList.add('bg-uniqueLightGray', 'text-black');
            });
            button.classList.remove('bg-uniqueLightGray', 'text-black');
            button.classList.add('bg-blue-400', 'text-white');
            document.getElementById('connection').value = button.getAttribute('data-value');
        });
    });

    // Handle Voltage type (Phase/Line) buttons
    const voltageButtons = document.querySelectorAll('.voltage-button');
    voltageButtons.forEach(button => {
        button.addEventListener('click', function() {
            voltageButtons.forEach(btn => {
                btn.classList.remove('bg-blue-400', 'text-white');
                btn.classList.add('bg-uniqueLightGray', 'text-black');
            });
            button.classList.remove('bg-uniqueLightGray', 'text-black');
            button.classList.add('bg-blue-400', 'text-white');
            document.getElementById('voltage_type').value = button.getAttribute('data-value');
        });
    });

    // Handle Current type (Phase/Line) buttons
    const currentButtons = document.querySelectorAll('.current-button');
    currentButtons.forEach(button => {
        button.addEventListener('click', function() {
            currentButtons.forEach(btn => {
                btn.classList.remove('bg-blue-400', 'text-white');
                btn.classList.add('bg-uniqueLightGray', 'text-black');
            });
            button.classList.remove('bg-uniqueLightGray', 'text-black');
            button.classList.add('bg-blue-400', 'text-white');
            document.getElementById('current_type').value = button.getAttribute('data-value');
        });
    });

    // Handle Random Values Button
    document.getElementById('random-values-button').addEventListener('click', function() {
        // Generate random values for voltage and current
        const randomVoltage = Math.floor(Math.random() * 240) + 1; // 1 to 240
        const randomCurrent = Math.floor(Math.random() * 100) + 1; // 1 to 100
    
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
            btn.classList.remove('bg-blue-400', 'text-white');
            btn.classList.add('bg-uniqueLightGray', 'text-black');
        });
        document.querySelector(`.${randomConnection}-button`).classList.add('bg-blue-400', 'text-white');
    
        // Update button visuals for Voltage Type (Phase/Line)
        voltageButtons.forEach(btn => {
            btn.classList.remove('bg-blue-400', 'text-white');
            btn.classList.add('bg-uniqueLightGray', 'text-black');
        });
        document.querySelector(`.${randomVoltageType}-button`).classList.add('bg-blue-400', 'text-white');
    
        // Update button visuals for Current Type (Phase/Line)
        currentButtons.forEach(btn => {
            btn.classList.remove('bg-blue-400', 'text-white');
            btn.classList.add('bg-uniqueLightGray', 'text-black');
        });
        document.querySelector(`.current-button.${randomCurrentType}-button`).classList.add('bg-blue-400', 'text-white');
    
        // Automatically submit the form after the random values are set
        submitFormWithFetch();
    }); 

    // Function to handle form submission using fetch
    function submitFormWithFetch() {
        const formData = new FormData(document.getElementById('power-form'));
        const voltage = formData.get('voltage');
        const current = formData.get('current');
        const resistor = formData.get('resistor');
        const power = formData.get('power');
        let filledFields = 0;

        [voltage, current, resistor, power].forEach(field => {
            if (field) filledFields++;
        });

        if (filledFields < 2) {
            alert('Please fill two fields to calculate.');
            return; 
        }

        if ((voltage && voltage <= 0) || 
            (current && current <= 0) || 
            (resistor && resistor <= 0) || 
            (power && power <= 0)) {
            alert('Please enter positive values greater than zero for both intended fields.');
            return;
        }

        fetch('/calculate', {
            method: 'POST',
            body: formData
        })
        .then(response => response.text())
        .then(data => {
            document.getElementById('results').innerHTML = data;
        })
        .catch(error => console.error('Error:', error));
    }

    document.getElementById('power-form').addEventListener('submit', function(event) {
        event.preventDefault(); 
        submitFormWithFetch();
    });
});