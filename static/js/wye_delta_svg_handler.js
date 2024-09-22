// *****************************************
// Author:   Emanuel A.
// Date:     09/22/2024
// Project:  Power-Model
// 
// Purpose:  JavaScript for handling wye_and_delta_diagram.svg.
// *****************************************

document.addEventListener("DOMContentLoaded", function() {
    // Select the object containing the SVG
    const svgObject = document.getElementById('wye_and_delta_diagram');

    // Ensure the object is loaded and ready
    svgObject.addEventListener('load', function() {
        const svgDocument = svgObject.contentDocument;  // Access the SVG's inner document
        
        // Get Wye elements
        const wyeVoltageVa = svgDocument.getElementById('wye-voltage-va');
        const wyeVoltageVb = svgDocument.getElementById('wye-voltage-vb');
        const wyeVoltageVc = svgDocument.getElementById('wye-voltage-vc');
        const wyeVoltageVab = svgDocument.getElementById('wye-voltage-vab');
        const wyeVoltageVbc = svgDocument.getElementById('wye-voltage-vbc');
        const wyeVoltageVca = svgDocument.getElementById('wye-voltage-vca');
        const wyeCurrentIa = svgDocument.getElementById('wye-current-ia');
        const wyeCurrentIb = svgDocument.getElementById('wye-current-ib');
        const wyeCurrentIc = svgDocument.getElementById('wye-current-ic');
        const wyeCurrentIn = svgDocument.getElementById('wye-current-in');
        const wyeResistanceRa = svgDocument.getElementById('wye-resistance-ra');
        const wyeResistanceRb = svgDocument.getElementById('wye-resistance-rb');
        const wyeResistanceRc = svgDocument.getElementById('wye-resistance-rc');
        
        // Get Delta elements
        const deltaVoltageVa = svgDocument.getElementById('delta-voltage-va');
        const deltaVoltageVb = svgDocument.getElementById('delta-voltage-vb');
        const deltaVoltageVc = svgDocument.getElementById('delta-voltage-vc');
        const deltaVoltageVab = svgDocument.getElementById('delta-voltage-vab');
        const deltaVoltageVbc = svgDocument.getElementById('delta-voltage-vbc');
        const deltaVoltageVca = svgDocument.getElementById('delta-voltage-vca');
        const deltaCurrentIline1 = svgDocument.getElementById('delta-current-iline1');
        const deltaCurrentIline2 = svgDocument.getElementById('delta-current-iline2');
        const deltaCurrentIline3 = svgDocument.getElementById('delta-current-iline3');
        const deltaCurrentIab = svgDocument.getElementById('delta-current-iab');
        const deltaCurrentIbc = svgDocument.getElementById('delta-current-ibc');
        const deltaCurrentIca = svgDocument.getElementById('delta-current-ica');
        const deltaResistanceRab = svgDocument.getElementById('delta-resistance-rab');
        const deltaResistanceRbc = svgDocument.getElementById('delta-resistance-rbc');
        const deltaResistanceRca = svgDocument.getElementById('delta-resistance-rca');
        
        // Form submission handling
        document.getElementById('power-form').addEventListener('submit', function(event) {
            event.preventDefault();  // Prevent form submission
            
            // Get values from the form
            const enteredVoltage = parseFloat(document.querySelector('[name="voltage"]').value) || 120;
            const enteredCurrent = parseFloat(document.querySelector('[name="current"]').value) || (enteredVoltage / 10).toFixed(2);
            const enteredResistor = parseFloat(document.querySelector('[name="resistor"]').value) || 10;
            const enteredPower = parseFloat(document.querySelector('[name="power"]').value);
            const connectionType = document.querySelector('[name="connection"]').value;
            
            // Calculate missing values if power is provided
            let calculatedCurrent;
            if (enteredPower && !enteredCurrent) {
                calculatedCurrent = (enteredPower / enteredVoltage).toFixed(2);
            }

            // Update the Wye values
            if (connectionType === 'wye') {
                if (wyeVoltageVa) wyeVoltageVa.textContent = `V_a = ${enteredVoltage} V`;
                if (wyeVoltageVb) wyeVoltageVb.textContent = `V_b = ${(enteredVoltage).toFixed(2)} V`;
                if (wyeVoltageVc) wyeVoltageVc.textContent = `V_c = ${(enteredVoltage).toFixed(2)} V`;
                if (wyeVoltageVab) wyeVoltageVab.textContent = `V_ab = ${(Math.sqrt(3) * enteredVoltage).toFixed(2)} V`;
                if (wyeVoltageVbc) wyeVoltageVbc.textContent = `V_bc = ${(Math.sqrt(3) * enteredVoltage).toFixed(2)} V`;
                if (wyeVoltageVca) wyeVoltageVca.textContent = `V_ca = ${(Math.sqrt(3) * enteredVoltage).toFixed(2)} V`;
                if (wyeCurrentIa) wyeCurrentIa.textContent = `I_a = ${enteredCurrent} A`;
                if (wyeCurrentIb) wyeCurrentIb.textContent = `I_b = ${enteredCurrent} A`;
                if (wyeCurrentIc) wyeCurrentIc.textContent = `I_c = ${enteredCurrent} A`;
                if (wyeCurrentIn) wyeCurrentIn.textContent = `I_n = 0 A`;
                if (wyeResistanceRa) wyeResistanceRa.textContent = `R_a = ${enteredResistor} Ω`;
                if (wyeResistanceRb) wyeResistanceRb.textContent = `R_b = ${enteredResistor} Ω`;
                if (wyeResistanceRc) wyeResistanceRc.textContent = `R_c = ${enteredResistor} Ω`;
            }
            
            // Update the Delta values
            if (connectionType === 'delta') {
                if (deltaVoltageVa) deltaVoltageVa.textContent = `V_a = ${enteredVoltage} V`;
                if (deltaVoltageVb) deltaVoltageVb.textContent = `V_b = ${(enteredVoltage).toFixed(2)} V`;
                if (deltaVoltageVc) deltaVoltageVc.textContent = `V_c = ${(enteredVoltage).toFixed(2)} V`;
                if (deltaVoltageVab) deltaVoltageVab.textContent = `V_ab = ${(Math.sqrt(3) * enteredVoltage).toFixed(2)} V`;
                if (deltaVoltageVbc) deltaVoltageVbc.textContent = `V_bc = ${(Math.sqrt(3) * enteredVoltage).toFixed(2)} V`;
                if (deltaVoltageVca) deltaVoltageVca.textContent = `V_ca = ${(Math.sqrt(3) * enteredVoltage).toFixed(2)} V`;
                if (deltaCurrentIline1) deltaCurrentIline1.textContent = `I_line1 = ${enteredCurrent} A`;
                if (deltaCurrentIline2) deltaCurrentIline2.textContent = `I_line2 = ${enteredCurrent} A`;
                if (deltaCurrentIline3) deltaCurrentIline3.textContent = `I_line3 = ${enteredCurrent} A`;
                if (deltaCurrentIab) deltaCurrentIab.textContent = `I_ab = ${(Math.sqrt(3) * enteredCurrent).toFixed(2)} A`;
                if (deltaCurrentIbc) deltaCurrentIbc.textContent = `I_bc = ${(Math.sqrt(3) * enteredCurrent).toFixed(2)} A`;
                if (deltaCurrentIca) deltaCurrentIca.textContent = `I_ca = ${(Math.sqrt(3) * enteredCurrent).toFixed(2)} A`;
                if (deltaResistanceRab) deltaResistanceRab.textContent = `R_ab = ${enteredResistor} Ω`;
                if (deltaResistanceRbc) deltaResistanceRbc.textContent = `R_bc = ${enteredResistor} Ω`;
                if (deltaResistanceRca) deltaResistanceRca.textContent = `R_ca = ${enteredResistor} Ω`;
            }
        });
    });
});
