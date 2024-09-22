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
def wye_voltages(voltage_phase=None, voltage_line=None):
    if voltage_phase:
        voltage_line = math.sqrt(3) * voltage_phase
        return voltage_phase, voltage_line
    elif voltage_line:
        voltage_phase = voltage_line / math.sqrt(3)
        return voltage_phase, voltage_line
    else:
        raise ValueError("Either phase or line voltage must be provided.")

# end wye_voltages

def wye_currents(current_phase=None, current_line=None):
    if current_phase:
        current_line = current_phase
        return current_phase, current_line
    elif current_line:
        current_phase = current_line
        return current_phase, current_line
    else:
        raise ValueError("Either phase or line current must be provided.")

# end wye_currents

# *****************************************
# Delta Connection Calculations
#
# *****************************************
def delta_voltages(voltage_phase=None, voltage_line=None):
    if voltage_phase:
        voltage_line = voltage_phase
        return voltage_phase, voltage_line
    elif voltage_line:
        voltage_phase = voltage_line
        return voltage_phase, voltage_line
    else:
        raise ValueError("Either phase or line voltage must be provided.")
# end delta_voltages

def delta_currents(current_phase=None, current_line=None):
    if current_phase:
        current_line = math.sqrt(3) * current_phase
        return current_phase, current_line
    elif current_line:
        current_phase = current_line / math.sqrt(3)
        return current_phase, current_line
    else:
        raise ValueError("Either phase or line current must be provided.")
# end delta_currents
    
# ************************************
# Uncomment to test calculations
# 
# ************************************
# # Testing wye voltage calculations
# phase_voltage = 120  # Phase voltage of 120V
# result = wye_voltages(voltage_phase=phase_voltage)
# print(f"Wye connection: Phase Voltage = {result[0]}V, Line Voltage = {result[1]:.2f}V")

# # Testing wye current calculations
# phase_current = 10  # Phase current of 10A
# result = wye_currents(current_phase=phase_current)
# print(f"Wye connection: Phase Current = {result[0]}A, Line Current = {result[1]:.2f}A")

# # Testing delta voltage calculations
# line_voltage = 240  # Line voltage of 240V
# result = delta_voltages(voltage_line=line_voltage)
# print(f"Delta connection: Line Voltage = {result[1]}V, Phase Voltage = {result[0]}V")

# # Testing delta current calculations
# line_current = 15  # Line current of 15A
# result = delta_currents(current_line=line_current)
# print(f"Delta connection: Line Current = {result[1]}A, Phase Current = {result[0]:.2f}A")