# ⚡ Power-Model

## 📝 Overview
Power-Model is a dynamic web-based application designed to help visualize and interact with **Wye (Y)** and **Delta (Δ)** power system configurations. This tool allows users to input electrical parameters and receive calculations for **voltage**, **current**, **resistance**, and **power** in real time. It is a resource designed for students, engineers, and professionals working in the field of power systems.

## 🌟 Features
- Interactive **Wye** and **Delta** **balanced** configuration model
- Easy-to-use web interface
- Live calculations based on user input for:
  - Phase/Line Voltage
  - Phase/Line Current
  - Resistance
  - Power Dissipation
- **Clear and detailed** results displayed directly on the web page
- **Graphs**: Display chosen Phase/Line voltage, current, and power plots over time
- **Dark mode** for comfortable viewing in low-light environments
- **Random value generation** for quick testing and exploration
- A Flask app that runs locally or can be deployed to a server

## 🛠️ Future Enhancements
- **3D Visualization**: Add **phasor diagrams** with magnitude and phase angles, including 3D models for advanced visualization of power systems.
- **Dynamic Response**: Real-time response for adjusting values on the fly, updating outputs instantly.

## 🚀 Installation & Setup
You can run the Power-Model locally on your machine by following these steps:

1. **Clone the repository**:
    ```bash
    git clone https://github.com/emanalva/Power-Model.git
    cd Power-Model
    ```

2. **Install the required dependencies**:
    ```bash
    pip install -r required.txt
    ```

3. **Run the app**:
    ```bash
    python3 app.py
    ```

4. **Open your browser** and go to:
    ```
    http://127.0.0.1:5000
    ```
Enjoy visualizing your power system configurations!

---

## 🙏 Acknowledgments
Special thanks to **Inkscape**, a free and open-source vector graphics editor, for allowing the creation of custom SVG diagrams used in this project to visualize Wye and Delta configurations. You can find more about Inkscape at [https://inkscape.org](https://inkscape.org).

---

© 2024 Emanuel Alvarez