import pyvisa
import time

rm=pyvisa.ResourceManager()
psu=rm.open_resource("USB0::0x0699::0x0390::C010946::INSTR")
print(psu.query("*IDN?"))

psu.write("OUTP ON")

for v in range(0,5):
    psu.write(f"VOLT {v}")
    time.sleep(5)

    measured=psu.query("MEAS:VOLT?")
    print(F"Set: {v}V |Measured:{measured}")
psu.write("OUTP OFF")
