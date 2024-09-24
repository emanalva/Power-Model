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
    # Ensure at least two inputs are provided
    if sum([x is not None for x in [voltage_phase, voltage_line, current_phase, current_line, R, power]]) < 2:
        return "Error: At least two variables are required to calculate the others."
    
    # Ensure all provided values are greater than 0
    if any(x is not None and x <= 0 for x in [voltage_phase, voltage_line, current_phase, current_line, R, power]):
        return "Error: All input values must be greater than zero."

    if power and voltage_phase:
        voltage_line = math.sqrt(3) * voltage_phase
        current_phase = power / (3* voltage_phase)
        current_line = current_phase
        R = voltage_phase / current_phase

    elif power and voltage_line:
        voltage_phase = voltage_line / math.sqrt(3)
        current_phase = power / (3* voltage_phase)
        current_line = current_phase
        R = voltage_phase / current_phase

    elif power and current_phase:
        voltage_phase = power / (3 * current_phase)
        voltage_line = math.sqrt(3) * voltage_phase
        current_line = current_phase
        R = voltage_phase / current_phase

    elif power and current_line:
        current_phase = current_line
        voltage_phase = power / (3 * current_phase)
        voltage_line = math.sqrt(3) * voltage_phase
        R = voltage_phase / current_phase

    elif power and R:
        current_phase = math.sqrt(power / (3 * R))
        voltage_phase = current_phase * R
        voltage_line = math.sqrt(3) * voltage_phase
        current_line = current_phase

    elif voltage_phase and current_phase:
        power = 3 * voltage_phase * current_phase
        voltage_line = math.sqrt(3) * voltage_phase
        current_line = current_phase
        R = voltage_phase / current_phase

    elif voltage_phase and current_line:
        current_phase = current_line
        power = 3 * voltage_phase * current_phase
        voltage_line = math.sqrt(3) * voltage_phase
        R = voltage_phase / current_phase

    elif voltage_phase and R:
        current_phase = voltage_phase / R
        power = 3 * voltage_phase * current_phase
        voltage_line = math.sqrt(3) * voltage_phase
        current_line = current_phase

    elif voltage_line and current_phase:
        voltage_phase = voltage_line / math.sqrt(3)
        power = 3 * voltage_phase * current_phase
        current_line = current_phase
        R = voltage_phase / current_phase

    elif voltage_line and current_line:
        current_phase = current_line
        voltage_phase = voltage_line / math.sqrt(3)
        power = 3 * voltage_phase * current_phase
        R = voltage_phase / current_phase

    elif voltage_line and R:
        voltage_phase = voltage_line / math.sqrt(3)
        current_phase = voltage_phase / R
        current_line = current_phase
        power = 3 * voltage_phase * current_phase

    elif current_phase and R:
        voltage_phase = current_phase * R
        voltage_line = math.sqrt(3) * voltage_phase
        current_line = current_phase
        power = 3 * voltage_phase * current_phase
    
    elif current_line and R:
        current_phase = current_line
        voltage_phase = current_phase * R
        voltage_line = math.sqrt(3) * voltage_phase
        power = 3 * voltage_phase * current_phase
        
    return voltage_phase, voltage_line, current_phase, current_line, power, R
# end wye_calculations()


# *****************************************
# Delta Connection Calculations
#
# *****************************************
def delta_calculations(voltage_phase=None, voltage_line=None, current_phase=None, current_line=None, R=None, power=None):
    # Ensure at least two inputs are provided
    if sum([x is not None for x in [voltage_phase, voltage_line, current_phase, current_line, R, power]]) < 2:
        return "Error: At least two variables are required to calculate the others."
    
    # Ensure all provided values are greater than 0
    if any(x is not None and x <= 0 for x in [voltage_phase, voltage_line, current_phase, current_line, R, power]):
        return "Error: All input values must be greater than zero."

    if power and voltage_phase:
        voltage_line = voltage_phase  # In delta, voltage_phase = voltage_line
        current_phase = power / (3 * voltage_phase)
        current_line = math.sqrt(3) * current_phase
        R = voltage_phase / current_phase

    elif power and voltage_line:
        voltage_phase = voltage_line  # In delta, voltage_phase = voltage_line
        current_phase = power / (3 * voltage_phase)
        current_line = math.sqrt(3) * current_phase
        R = voltage_phase / current_phase

    elif power and current_phase:
        voltage_phase = power / (3 * current_phase)
        voltage_line = voltage_phase  # In delta, voltage_phase = voltage_line
        current_line = math.sqrt(3) * current_phase
        R = voltage_phase / current_phase

    elif power and current_line:
        current_phase = current_line / math.sqrt(3)
        voltage_phase = power / (3 * current_phase)
        voltage_line = voltage_phase  # In delta, voltage_phase = voltage_line
        R = voltage_phase / current_phase

    elif power and R:
        current_phase = math.sqrt(power / (3 * R))
        voltage_phase = current_phase * R
        voltage_line = voltage_phase  # In delta, voltage_phase = voltage_line
        current_line = math.sqrt(3) * current_phase

    elif voltage_phase and current_phase:
        power = 3 * voltage_phase * current_phase
        voltage_line = voltage_phase  # In delta, voltage_phase = voltage_line
        current_line = math.sqrt(3) * current_phase
        R = voltage_phase / current_phase

    elif voltage_phase and current_line:
        current_phase = current_line / math.sqrt(3)
        power = 3 * voltage_phase * current_phase
        voltage_line = voltage_phase  # In delta, voltage_phase = voltage_line
        R = voltage_phase / current_phase

    elif voltage_phase and R:
        current_phase = voltage_phase / R
        power = 3 * voltage_phase * current_phase
        voltage_line = voltage_phase  # In delta, voltage_phase = voltage_line
        current_line = math.sqrt(3) * current_phase

    elif voltage_line and current_phase:
        voltage_phase = voltage_line  # In delta, voltage_phase = voltage_line
        power = 3 * voltage_phase * current_phase
        current_line = math.sqrt(3) * current_phase
        R = voltage_phase / current_phase

    elif voltage_line and current_line:
        current_phase = current_line / math.sqrt(3)
        voltage_phase = voltage_line  # In delta, voltage_phase = voltage_line
        power = 3 * voltage_phase * current_phase
        R = voltage_phase / current_phase

    elif voltage_line and R:
        voltage_phase = voltage_line  # In delta, voltage_phase = voltage_line
        current_phase = voltage_phase / R
        current_line = math.sqrt(3) * current_phase
        power = 3 * voltage_phase * current_phase

    elif current_phase and R:
        voltage_phase = current_phase * R
        voltage_line = voltage_phase  # In delta, voltage_phase = voltage_line
        current_line = math.sqrt(3) * current_phase
        power = 3 * voltage_phase * current_phase

    elif current_line and R:
        current_phase = current_line / math.sqrt(3)
        voltage_phase = current_phase * R
        voltage_line = voltage_phase  # In delta, voltage_phase = voltage_line
        power = 3 * voltage_phase * current_phase

    return voltage_phase, voltage_line, current_phase, current_line, power, R
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