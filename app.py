# *****************************************
# Author:   Emanuel A.
# Date:     09/22/2024
# Project:  Power-Model
# 
# Purpose:  Flask app for Power Electronics Model
# *****************************************

# Imports
from calculations import wye_voltages, wye_currents, delta_voltages, delta_currents
from flask import Flask, request, render_template

# Flask app
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    connection_type = request.form['connection']
    voltage_type = request.form['voltage_type']
    current_type = request.form['current_type']
    voltage = float(request.form['voltage']) if request.form['voltage'] else None
    current = float(request.form['current']) if request.form['current'] else None

    if connection_type == 'wye':
        if voltage_type == 'phase':
            voltage_result = wye_voltages(voltage_phase=voltage)
        elif voltage_type == 'line':
            voltage_result = wye_voltages(voltage_line=voltage)
        if current_type == 'phase':
            current_result = wye_currents(current_phase=current)
        elif current_type == 'line':
            current_result = wye_currents(current_line=current)

    elif connection_type == 'delta':
        if voltage_type == 'phase':
            voltage_result = delta_voltages(voltage_phase=voltage)
        elif voltage_type == 'line':
            voltage_result = delta_voltages(voltage_line=voltage)
        if current_type == 'phase':
            current_result = delta_currents(current_phase=current)
        elif current_type == 'line':
            current_result = delta_currents(current_line=current)

    return f"Voltage: Phase Voltage = {voltage_result[0]}V, Line Voltage = {voltage_result[1]:.2f}V <br> " \
           f"Current: Phase Current = {current_result[0]}A, Line Current = {current_result[1]:.2f}A"

if __name__ == "__main__":
    app.run(debug=True)