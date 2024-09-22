# *****************************************
# Author:   Emanuel A.
# Date:     09/22/2024
# Project:  Power-Model
# 
# Purpose:  Functions for calculations.
# *****************************************

# Imports
import math

# *****************************************
# Wye Connection Calculations
#
# *****************************************
def wye_calculations(voltage_phase=None, voltage_line=None, current_phase=None, current_line=None, R=None, power=None):
    # Check how many variables are provided
    provided_inputs = [voltage_phase, voltage_line, current_phase, current_line, R, power]
    provided_count = sum([1 for i in provided_inputs if i is not None])

    if provided_count < 2:
        return "Error: At least two variables are required to calculate the others."

    # Calculate missing variables based on inputs
    if voltage_phase and current_phase and not power:
        power = 3 * voltage_phase * current_phase  # Calculate power from voltage and current
    elif power and voltage_phase and not current_phase:
        current_phase = power / (3 * voltage_phase)  # Calculate current from power and voltage
    elif power and current_phase and not voltage_phase:
        voltage_phase = power / (3 * current_phase)  # Calculate voltage from power and current

    # Calculate voltage line from voltage phase
    if voltage_phase and not voltage_line:
        voltage_line = math.sqrt(3) * voltage_phase

    # Calculate current phase from current line
    if current_line and not current_phase:
        current_phase = current_line

    # Calculate resistance if voltage and current are provided
    if voltage_phase and current_phase and not R:
        R = voltage_phase / current_phase

    # Calculate current from voltage and resistance
    if voltage_phase and R and not current_phase:
        current_phase = voltage_phase / R

    power = power or 3 * current_phase**2 * R  # Recalculate power if missing

    return voltage_phase, voltage_line, current_phase, power, R
# end wye_calculations()

# *****************************************
# Delta Connection Calculations
#
# *****************************************
def delta_calculations(voltage_phase=None, voltage_line=None, current_phase=None, current_line=None, R=None, power=None):
    # Check how many variables are provided
    provided_inputs = [voltage_phase, voltage_line, current_phase, current_line, R, power]
    provided_count = sum([1 for i in provided_inputs if i is not None])

    if provided_count < 2:
        return "Error: At least two variables are required to calculate the others."

    # Calculate missing variables based on inputs
    if voltage_phase and current_phase and not power:
        power = 3 * voltage_phase * current_phase  # Calculate power from voltage and current
    elif power and voltage_phase and not current_phase:
        current_phase = power / (3 * voltage_phase)  # Calculate current from power and voltage
    elif power and current_phase and not voltage_phase:
        voltage_phase = power / (3 * current_phase)  # Calculate voltage from power and current

    # In delta, line voltage is the same as phase voltage
    if voltage_phase and not voltage_line:
        voltage_line = voltage_phase

    # Calculate line current from phase current
    if current_phase and not current_line:
        current_line = math.sqrt(3) * current_phase

    # Calculate resistance if voltage and current are provided
    if voltage_phase and current_phase and not R:
        R = voltage_phase / current_phase

    # Calculate current from voltage and resistance
    if voltage_phase and R and not current_phase:
        current_phase = voltage_phase / R

    power = power or 3 * current_line**2 * R  # Recalculate power if missing

    return voltage_phase, voltage_line, current_phase, power, R
# end delta_calculations()
    
# ************************************
# Uncomment to test calculations
# 
# ************************************
# Test wye calculations with voltage and resistance
# result = wye_calculations(voltage_phase=120, R=10)
# print(result)  # Should calculate current, power, and voltage line

# # Test delta calculations with power and current
# result = delta_calculations(power=500, current_phase=10)
# print(result)  # Should calculate voltage, resistance, and current line