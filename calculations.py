# *****************************************
# Author:   Emanuel A.
# Date:     09/22/2024
# Project:  Power-Model
# 
# Purpose:  Functions for calculations.
# *****************************************
import math

# Wye Connection Calculations
def wye_voltages(voltage_phase=None, voltage_line=None):
    if voltage_phase:
        voltage_line = math.sqrt(3) * voltage_phase
        return voltage_phase, voltage_line
    elif voltage_line:
        voltage_phase = voltage_line / math.sqrt(3)
        return voltage_phase, voltage_line
    else:
        raise ValueError("Either phase or line voltage must be provided.")

def wye_currents(current_phase=None, current_line=None):
    if current_phase:
        current_line = current_phase
        return current_phase, current_line
    elif current_line:
        current_phase = current_line
        return current_phase, current_line
    else:
        raise ValueError("Either phase or line current must be provided.")

# Delta Connection Calculations
def delta_voltages(voltage_phase=None, voltage_line=None):
    if voltage_phase:
        voltage_line = voltage_phase
        return voltage_phase, voltage_line
    elif voltage_line:
        voltage_phase = voltage_line
        return voltage_phase, voltage_line
    else:
        raise ValueError("Either phase or line voltage must be provided.")

def delta_currents(current_phase=None, current_line=None):
    if current_phase:
        current_line = math.sqrt(3) * current_phase
        return current_phase, current_line
    elif current_line:
        current_phase = current_line / math.sqrt(3)
        return current_phase, current_line
    else:
        raise ValueError("Either phase or line current must be provided.")