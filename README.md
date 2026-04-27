# Tektronix PWS4205 DC Power Supply Automation

##  Overview

This project demonstrates automation of a Tektronix PWS4205 DC Power Supply using Python, PyVISA, and a simple GUI.
It performs voltage sweep operations and logs measured values.

##  Features

* Automated voltage sweep
* GUI-based control (Tkinter)
* Real-time output display
* SCPI command-based instrument control
* Easy to extend for DMM integration

##  Technologies Used

* Python
* PyVISA
* Tkinter (GUI)
* SCPI Commands

##  Hardware Used

* Tektronix PWS4205 Power Supply
* USB Interface (USBTMC)

##  Project Structure

* sweep.py → main automation script
* gui.py → GUI application (optional)
* README.md → documentation

##  How to Run

### 1. Install dependencies

pip install pyvisa pyvisa-py

### 2. Connect PSU via USB

### 3. Run script

python sweep.py

##  Example Output

Voltage: 0V
Voltage: 1V
Voltage: 2V

##  Future Improvements

* Integrate Digital Multimeter (DMM7510)
* Save results to CSV/Excel
* Add graph plotting
* Error handling & logging

##  Author

Riyaz
