import Comparator
import time
from tinkerforge.ip_connection import IPConnection

HOST = "localhost"
PORT = 4223

ipcon = IPConnection()
ipcon.connect(HOST, PORT) # Connect to brickd

UID_ANALOG_IN="F8S"

comparator = Comparator.Comparator(ipcon,UID_ANALOG_IN)


# 1) Startup behaviour
# - Setup callback on comparator input
# - Store timestamp
# - Enable Power Supply via relay
# - Store timestamp upon callback trigger
# - Calculate timestamp difference

# 2) Power Consumption
# - Put DUT in right mode
# - Measure power consumption
# - Switch On Load
# -- Measure power consumption
# -- Measure voltage

input("Press key to exit\n")
ipcon.disconnect()

print("Master script finish...")
