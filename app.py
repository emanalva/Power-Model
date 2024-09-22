# *****************************************
# Author:   Emanuel A.
# Date:     09/22/2024
# Project:  Power-Model
# 
# Purpose:  Flask app for Power Electronics Model
# *****************************************

from calculations import wye_voltages, wye_currents, delta_voltages, delta_currents
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Power Electronics Model!"

if __name__ == "__main__":
    app.run(debug=True)
