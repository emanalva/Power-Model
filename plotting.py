# *****************************************
# Author:   Emanuel A.
# Date:     09/24/2024
# Project:  Power-Model
# 
# Purpose:  Functions for plotting.
# *****************************************

# Imports
import matplotlib.pyplot as plt
import matplotlib
import numpy as np
import io
import base64
import gc  # For garbage collection

# 
matplotlib.use('Agg')  # Use non-interactive backend

# *****************************************
# Helper Function: Convert plot to base64-encoded image
#
# *****************************************
def convert_plot_to_base64():
    """Converts the current Matplotlib plot to a base64 string to embed in HTML."""
    buf = io.BytesIO()
    plt.savefig(buf, format='png', bbox_inches='tight')
    buf.seek(0)
    img_base64 = base64.b64encode(buf.getvalue()).decode('utf-8')
    buf.close()
    plt.close()  # Close the plot after saving it
    gc.collect()  # Explicit garbage collection
    return img_base64
# end convert_plot_to_base64()


# *****************************************
# Plotting Function for 3-Phase Quantities (Voltages/Currents)
# 
# *****************************************
def plot_3phase(time, A_values, B_values, C_values, label):
    """
    Plots 3-phase quantities (either voltages or currents) over time.

    time: Time array
    A_values: Phase A values (voltage/current)
    B_values: Phase B values (voltage/current)
    C_values: Phase C values (voltage/current)
    label: 'Voltage' or 'Current' to differentiate the plot
    """
    plt.figure(figsize=(10, 6))
    plt.plot(time, A_values, label=f'{label} A', color='r')
    plt.plot(time, B_values, label=f'{label} B', color='g')
    plt.plot(time, C_values, label=f'{label} C', color='b')
    
    plt.title(f'3-Phase {label} Over Time')
    plt.xlabel('Time (s)')
    plt.ylabel(f'{label} (V or A)')
    plt.grid(True)
    plt.legend()
    
    # Return base64-encoded image
    img_base64 = convert_plot_to_base64()
    gc.collect()  # Explicit garbage collection
    return img_base64
# end plot_3phase()


# *****************************************
# Plotting Function for Power
# 
# *****************************************
def plot_power(time, power_values):
    """
    Plots power dissipation over time.

    time: Time array
    power_values: Power values over time (can be a constant array if power is constant)
    """
    plt.figure(figsize=(10, 6))
    plt.plot(time, power_values, label='Power', color='orange')
    
    plt.title('Power Dissipation Over Time')
    plt.xlabel('Time (s)')
    plt.ylabel('Power (W)')
    plt.grid(True)
    plt.legend()

    # Return base64-encoded image
    img_base64 = convert_plot_to_base64()
    gc.collect()  # Explicit garbage collection
    return img_base64
# end plot_power()
