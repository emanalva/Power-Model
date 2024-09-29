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
    const resultsBox = document.getElementById('results'); // Select the results box
    const plottingSection = document.getElementById('plotting_section'); // Select the plotting section
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
        toggleButton.textContent = "Light Mode"; // Switch to Light Mode text when dark mode is enabled
    } else {
        disableDarkMode();
        toggleButton.textContent = "Dark Mode"; // Switch to Dark Mode text when dark mode is disabled
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
        resultsBox.classList.replace('text-black', 'text-white');
        submitButton.classList.replace('text-black', 'text-white');

        // Update calculator heading
        const calculatorHeading = document.getElementById('calculator-heading');
        calculatorHeading.classList.replace('text-black', 'text-white');

        // Update results container
        const resultsContainer = document.getElementById('results');
        resultsContainer.classList.replace('bg-gray-200', 'bg-uniqueDarkGray');
        resultsContainer.classList.replace('text-black', 'text-white');

        // Update plotting container and its heading
        const plottingContainer = document.getElementById('plotting_section');
        plottingContainer.classList.replace('bg-gray-200', 'bg-uniqueDarkGray');
        const plotsHeading = plottingContainer.querySelector('h3');
        plotsHeading.classList.replace('text-black', 'text-white');

        // Update text within plot containers
        const plotTexts = plottingContainer.querySelectorAll('h4');
        plotTexts.forEach(plotText => {
            plotText.classList.replace('text-black', 'text-white');
        });

        // Update result section backgrounds
        const resultSections = resultsContainer.querySelectorAll('.bg-gray-200');
        resultSections.forEach(section => {
            section.classList.replace('bg-gray-200', 'bg-uniqueDarkGray');
        });

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
        resultsBox.classList.replace('text-white', 'text-black');
        submitButton.classList.replace('text-white', 'text-black');

        // Update calculator heading
        const calculatorHeading = document.getElementById('calculator-heading');
        calculatorHeading.classList.replace('text-white', 'text-black');

        // Update results container
        const resultsContainer = document.getElementById('results');
        resultsContainer.classList.replace('bg-uniqueDarkGray', 'bg-gray-200');
        resultsContainer.classList.replace('text-white', 'text-black');

        // Update plotting container and its heading
        const plottingContainer = document.getElementById('plotting_section');
        plottingContainer.classList.replace('bg-uniqueDarkGray', 'bg-gray-200');
        const plotsHeading = plottingContainer.querySelector('h3');
        plotsHeading.classList.replace('text-white', 'text-black');

        // Update text within plot containers
        const plotTexts = plottingContainer.querySelectorAll('h4');
        plotTexts.forEach(plotText => {
            plotText.classList.replace('text-white', 'text-black');
        });

        // Update result section backgrounds
        const resultSections = resultsContainer.querySelectorAll('.bg-uniqueDarkGray');
        resultSections.forEach(section => {
            section.classList.replace('bg-uniqueDarkGray', 'bg-gray-200');
        });

        localStorage.setItem('darkMode', 'disabled');
    }

    // Handle Configuration (Wye/Delta) buttons
    const configButtons = document.querySelectorAll('.config-button');
    configButtons.forEach(button => {
        button.addEventListener('click', function() {
            configButtons.forEach(btn => {
                btn.classList.remove('bg-blue-400');
                btn.classList.add('bg-uniqueLightGray');
            });
            button.classList.remove('bg-uniqueLightGray');
            button.classList.add('bg-blue-400');
            document.getElementById('connection').value = button.getAttribute('data-value');
        });
    });

    // Handle Voltage type (Phase/Line) buttons
    const voltageButtons = document.querySelectorAll('.voltage-button');
    voltageButtons.forEach(button => {
        button.addEventListener('click', function() {
            voltageButtons.forEach(btn => {
                btn.classList.remove('bg-blue-400');
                btn.classList.add('bg-uniqueLightGray');
            });
            button.classList.remove('bg-uniqueLightGray');
            button.classList.add('bg-blue-400');
            document.getElementById('voltage_type').value = button.getAttribute('data-value');
        });
    });

    // Handle Current type (Phase/Line) buttons
    const currentButtons = document.querySelectorAll('.current-button');
    currentButtons.forEach(button => {
        button.addEventListener('click', function() {
            currentButtons.forEach(btn => {
                btn.classList.remove('bg-blue-400');
                btn.classList.add('bg-uniqueLightGray');
            });
            button.classList.remove('bg-uniqueLightGray');
            button.classList.add('bg-blue-400');
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
        document.getElementById('connection').value = randomConnection;
        document.getElementById('voltage_type').value = randomVoltageType;
        document.getElementById('current_type').value = randomCurrentType;

        // Update button visuals for Wye/Delta
        const configButtons = document.querySelectorAll('.config-button');
        configButtons.forEach(btn => {
            btn.classList.replace('bg-blue-400', 'bg-uniqueLightGray');
        });
        document.querySelector(`.config-button[data-value="${randomConnection}"]`).classList.replace('bg-uniqueLightGray', 'bg-blue-400');
        
        // Update button visuals for Voltage Type (Phase/Line)
        const voltageButtons = document.querySelectorAll('.voltage-button');
        voltageButtons.forEach(btn => {
            btn.classList.replace('bg-blue-400', 'bg-uniqueLightGray');
        });
        document.querySelector(`.voltage-button[data-value="${randomVoltageType}"]`).classList.replace('bg-uniqueLightGray', 'bg-blue-400');

        // Update button visuals for Current Type (Phase/Line)
        const currentButtons = document.querySelectorAll('.current-button');
        currentButtons.forEach(btn => {
            btn.classList.replace('bg-blue-400', 'bg-uniqueLightGray');
        });
        document.querySelector(`.current-button[data-value="${randomCurrentType}"]`).classList.replace('bg-uniqueLightGray', 'bg-blue-400');

        // Submit form with random values
        submitFormWithFetch();
    });

    // Submit Form with Fetch
    function submitFormWithFetch() {
        const formData = new FormData(document.getElementById('power-form'));
        const voltage = formData.get('voltage');
        const current = formData.get('current');
        const resistor = formData.get('resistor');
        const power = formData.get('power');
        let filledFields = 0;
    
        // Regular expression to check for valid numbers (integer or float)
        const validNumberRegex = /^-?\d+(\.\d+)?$/;

        // Check if fields are filled
        [voltage, current, resistor, power].forEach(field => {
            if (field) filledFields++;
        });

        if (filledFields < 2) {
            alert('Please fill two fields to calculate.');
            return;
        }

        // Check if inputs are valid numbers
        if ((voltage && !validNumberRegex.test(voltage)) || 
            (current && !validNumberRegex.test(current)) || 
            (resistor && !validNumberRegex.test(resistor)) || 
            (power && !validNumberRegex.test(power))) {
            alert('Please enter valid numbers in all fields.');
            return;
        }
    
        fetch('/calculate', {
            method: 'POST',
            body: formData
        })
        .then(response => response.text())
        .then(data => {
            document.getElementById('results').innerHTML = data;
            // Remove the hidden class to display the results
            document.getElementById('results').classList.remove('hidden');
            
            // Unhide the calculator heading
            document.getElementById('calculator-heading').classList.remove('hidden');
            
            // Unhide the plotting section
            plottingSection.classList.remove('hidden');
        })
        .catch(error => console.error('Error:', error));
    }
    
    document.getElementById('power-form').addEventListener('submit', function(event) {
        event.preventDefault();
        submitFormWithFetch();
    });    
});
