# *****************************************
# Author:   Emanuel A.
# Date:     09/22/2024
# Project:  Power-Model
# 
# Purpose:  Flask app for Power Electronics Model.
# *****************************************

# Imports
from flask import Flask, request, render_template
from calculations import wye_calculations, delta_calculations, generate_time_series, calculate_3phase_voltages, calculate_3phase_currents
from plotting import plot_3phase, plot_power  # Importing plotting functions

app = Flask(__name__)

# Route for the home page
@app.route('/')
def home():
    return render_template('index.html')

# Route for the calculations and plots
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

    # Perform calculations
    if connection_type == 'wye':
        result = wye_calculations(voltage_phase=voltage if voltage_type == 'phase' else None,
                                  voltage_line=voltage if voltage_type == 'line' else None,
                                  current_phase=current if current_type == 'phase' else None,
                                  current_line=current if current_type == 'line' else None,
                                  R=resistor,
                                  power=power)
    elif connection_type == 'delta':
        result = delta_calculations(voltage_phase=voltage if voltage_type == 'phase' else None,
                                    voltage_line=voltage if voltage_type == 'line' else None,
                                    current_phase=current if current_type == 'phase' else None,
                                    current_line=current if current_type == 'line' else None,
                                    R=resistor,
                                    power=power)

    # Handle errors
    if isinstance(result, str):
        return result  # Return the error message if there's an issue

    voltage_phase = result["voltage_phase"]
    voltage_line = result["voltage_line"]
    current_phase = result["current_phase"]
    current_line = result["current_line"]
    calculated_power = result["power"]
    calculated_resistor = result["resistance"]

    # Generate time points for 60Hz system using the new function
    time, theta_A, theta_B, theta_C = generate_time_series(frequency=60, period_count=1, time_steps=1000)

    # Calculate voltages and currents over time using the provided phase angles
    if voltage_type == 'phase':
        voltage_A, voltage_B, voltage_C = calculate_3phase_voltages(voltage_phase[0][0], time, theta_A, theta_B, theta_C)
    else:
        voltage_A, voltage_B, voltage_C = calculate_3phase_voltages(voltage_line[0][0], time, theta_A, theta_B, theta_C)

    if current_type == 'phase':
        current_A, current_B, current_C = calculate_3phase_currents(current_phase[0][0], time, theta_A, theta_B, theta_C)
    else:
        current_A, current_B, current_C = calculate_3phase_currents(current_line[0][0], time, theta_A, theta_B, theta_C)

    # Generate plots using the calculated voltages and currents
    voltage_plot = plot_3phase(time, voltage_A, voltage_B, voltage_C, label='Voltage')
    current_plot = plot_3phase(time, current_A, current_B, current_C, label='Current')

    # Power plot stays the same
    power_values = [calculated_power] * len(time)  # Assume power is constant for now
    power_plot = plot_power(time, power_values)

    # Render the results and plots in HTML
    return render_template('results.html',
                           voltage_phase=voltage_phase,
                           voltage_line=voltage_line,
                           current_phase=current_phase,
                           current_line=current_line,
                           calculated_power=calculated_power,
                           calculated_resistor=calculated_resistor,
                           voltage_plot=voltage_plot,
                           current_plot=current_plot,
                           power_plot=power_plot)

# Run the app
if __name__ == "__main__":
    app.run(debug=True)