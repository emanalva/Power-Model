# *****************************************
# Author:   Emanuel A.
# Date:     09/22/2024
# Project:  Power-Model
# 
# Purpose:  Functions for calculations.
# *****************************************

# Imports
import math
import cmath

# *****************************************
# Utility Functions for Phasors
#
# *****************************************
def polar_to_rect(magnitude, angle_deg):
    """Converts polar form (magnitude, angle) to rectangular form (complex number)."""
    angle_rad = math.radians(angle_deg)
    return cmath.rect(magnitude, angle_rad)

def rect_to_polar(complex_number):
    """Converts rectangular form (complex number) to polar form (magnitude, angle)."""
    magnitude = abs(complex_number)
    angle_rad = cmath.phase(complex_number)
    angle_deg = math.degrees(angle_rad)
    return magnitude, angle_deg

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
    
    # Base angles for phasor representation (phase shift of 120 degrees)
    phase_angles = [0, 120, 240]  # degrees for 3 phases

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
        
    # Phasor calculations
    phase_voltages = [polar_to_rect(voltage_phase, angle) for angle in phase_angles]
    line_voltages = [polar_to_rect(voltage_line, angle + 30) for angle in phase_angles]
    phase_currents = [polar_to_rect(current_phase, angle) for angle in phase_angles] if current_phase else []
    line_currents = phase_currents if current_phase else []

    return {
        "voltage_phase": [rect_to_polar(vp) for vp in phase_voltages],
        "voltage_line": [rect_to_polar(vl) for vl in line_voltages],
        "current_phase": [rect_to_polar(cp) for cp in phase_currents] if current_phase else None,
        "current_line": [rect_to_polar(cl) for cl in line_currents] if line_currents else None,
        "power": power,
        "resistance": R
    }
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
    
    # Base angles for phasor representation (phase shift of 120 degrees)
    phase_angles = [0, 120, 240]  # degrees for 3 phases

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

    # Phasor calculations
    phase_voltages = [polar_to_rect(voltage_phase, angle) for angle in phase_angles]
    line_currents = [polar_to_rect(current_line, angle + 30) for angle in phase_angles]
    phase_currents = [polar_to_rect(current_phase, angle) for angle in phase_angles]

    return {
        "voltage_phase": [rect_to_polar(vp) for vp in phase_voltages],
        "voltage_line": [rect_to_polar(vl) for vl in phase_voltages],  # Same in delta
        "current_phase": [rect_to_polar(cp) for cp in phase_currents] if current_phase else None,
        "current_line": [rect_to_polar(cl) for cl in line_currents] if line_currents else None,
        "power": power,
        "resistance": R
    }
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