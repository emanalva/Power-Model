# *****************************************
# Author:   Emanuel A.
# Date:     09/22/2024
# Project:  Power-Model
# 
# Purpose:  Flask app for Power Electronics Model.
# *****************************************

# Imports
from flask import Flask, request, render_template
from calculations import wye_calculations, delta_calculations

# Flask app
app = Flask(__name__)

# Route for the home page
@app.route('/')
def home():
    return render_template('index.html')

# Route for the calculations
@app.route('/calculate', methods=['POST'])
def calculate():
    # Collect input from the form
    connection_type = request.form['connection']
    voltage_type = request.form.get('voltage_type')  # Phase or Line voltage
    current_type = request.form.get('current_type')  # Phase or Line current
    voltage = float(request.form['voltage']) if request.form['voltage'] else None
    current = float(request.form['current']) if request.form['current'] else None
    resistor = float(request.form['resistor']) if request.form['resistor'] else None
    power = float(request.form['power']) if request.form['power'] else None

    # Initialize variables for results
    result = None

    # Handle calculations based on the connection type
    if connection_type == 'wye':
        result = wye_calculations(
            voltage_phase=voltage if voltage_type == 'phase' else None,
            voltage_line=voltage if voltage_type == 'line' else None,
            current_phase=current if current_type == 'phase' else None,
            current_line=current if current_type == 'line' else None,
            R=resistor,
            power=power
        )
    elif connection_type == 'delta':
        result = delta_calculations(
            voltage_phase=voltage if voltage_type == 'phase' else None,
            voltage_line=voltage if voltage_type == 'line' else None,
            current_phase=current if current_type == 'phase' else None,
            current_line=current if current_type == 'line' else None,
            R=resistor,
            power=power
        )

    # Handle case where fewer than 2 variables are provided
    if isinstance(result, str):
        return result  # Return error message directly

    # Extract phasor results
    voltage_phase = result["voltage_phase"]
    voltage_line = result["voltage_line"]
    current_phase = result["current_phase"]
    current_line = result["current_line"]
    calculated_power = result["power"]
    calculated_resistor = result["resistance"]

    # Display the calculated results
    result_html = "<h3>Results:</h3>"

    # Iterate over phase A, B, C results
    for i, (vp, vl, cp, cl) in enumerate(zip(voltage_phase, voltage_line, current_phase or [], current_line or [])):
        result_html += f"<hr><h4>Phase {['A', 'B', 'C'][i]}:</h4>"
        result_html += f"<p>Phase Voltage: {vp[0]:,.2f} V at {vp[1]:,.2f}°</p>"
        result_html += f"<p>Line Voltage: {vl[0]:,.2f} V at {vl[1]:,.2f}°</p>"
        if cp:
            result_html += f"<p>Phase Current: {cp[0]:,.2f} A at {cp[1]:,.2f}°</p>"
        if cl:
            result_html += f"<p>Line Current: {cl[0]:,.2f} A at {cl[1]:,.2f}°</p>"

    # Final results for power and resistance
    result_html += f"<hr><h4>Overall Load Power and Resistance:</h4>"
    result_html += f"<p>Load Power Dissipation: {calculated_power:,.2f} W</p>"
    result_html += f"<p>Load Resistance: {calculated_resistor:,.2f} Ω</p>"

    return result_html

# Run the app
if __name__ == "__main__":
    app.run(debug=True)
