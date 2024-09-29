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
import numpy as np

# *****************************************
# Utility Functions for Phasors
#
# *****************************************
def polar_to_rect(magnitude, angle_deg):
    """Converts polar form (magnitude, angle) to rectangular form (complex number)."""
    angle_rad = math.radians(angle_deg)
    return cmath.rect(magnitude, angle_rad)
# end polar_to_rect()

def rect_to_polar(complex_number):
    """Converts rectangular form (complex number) to polar form (magnitude, angle)."""
    magnitude = abs(complex_number)
    angle_rad = cmath.phase(complex_number)
    angle_deg = math.degrees(angle_rad)
    return magnitude, angle_deg
# end rect_to_polar()

# *****************************************
# Wye Connection Calculations
#
# *****************************************
def wye_calculations(voltage_phase=None, voltage_line=None, current_phase=None, current_line=None, R=None, power=None):
    # Count how many parameters are provided
    provided_params = sum(param is not None for param in [voltage_phase, voltage_line, current_phase, current_line, R, power])
    
    if provided_params != 2:
        return {"error": "Please input exactly 2 variables"}
    
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
    # Count how many parameters are provided
    provided_params = sum(param is not None for param in [voltage_phase, voltage_line, current_phase, current_line, R, power])
    
    if provided_params != 2:
        return {"error": "Please input exactly 2 variables"}
    
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
    line_currents = [polar_to_rect(current_line, angle - 30) for angle in phase_angles]
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

# *****************************************
# Time Series Generation for Plotting

# *****************************************
def generate_time_series(frequency=60, period_count=5, time_steps=500):
    """
    Generates time values and phase angles for phasors over several periods of a 3-phase system.
    
    frequency: Frequency of the AC system (default: 60Hz).
    period_count: Number of periods to plot (default: 5 periods).
    time_steps: Number of points per period (default: 500 points).
    
    Returns: 
    - time array
    - angles for Phase A, Phase B, and Phase C
    """
    # Time array from 0 to 'period_count' periods
    total_time = period_count * (1 / frequency)
    time = np.linspace(0, total_time, time_steps)
    
    # Phase angles (120 degrees apart for a balanced 3-phase system)
    theta_A = 2 * np.pi * frequency * time            # Phase A (0°)
    theta_B = theta_A - (2 * np.pi / 3)               # Phase B (120° behind A)
    theta_C = theta_A + (2 * np.pi / 3)               # Phase C (120° ahead of A)
    
    return time, theta_A, theta_B, theta_C


def calculate_3phase_voltages(voltage_magnitude, time, theta_A, theta_B, theta_C):
    """
    Calculates the 3-phase voltages over time based on the phase angles.

    voltage_magnitude: The amplitude of the phase/line voltage.
    time: Time array.
    theta_A, theta_B, theta_C: Phase angles for Phases A, B, and C.
    
    Returns: 
    - Voltage A
    - Voltage B
    - Voltage C
    """
    voltage_A = voltage_magnitude * np.cos(theta_A)
    voltage_B = voltage_magnitude * np.cos(theta_B)
    voltage_C = voltage_magnitude * np.cos(theta_C)
    
    return voltage_A, voltage_B, voltage_C


def calculate_3phase_currents(current_magnitude, time, theta_A, theta_B, theta_C):
    """
    Calculates the 3-phase currents over time based on the phase angles.

    current_magnitude: The amplitude of the phase/line current.
    time: Time array.
    theta_A, theta_B, theta_C: Phase angles for Phases A, B, and C.
    
    Returns: 
    - Current A
    - Current B
    - Current C
    """
    current_A = current_magnitude * np.cos(theta_A)
    current_B = current_magnitude * np.cos(theta_B)
    current_C = current_magnitude * np.cos(theta_C)
    
    return current_A, current_B, current_C

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