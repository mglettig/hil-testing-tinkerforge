import Comparator
import time
from tinkerforge.ip_connection import IPConnection
import asyncio
import threading
from datetime import datetime

HOST = "localhost"
PORT = 4223

def callback(voltage):
    print("Callback triggered!")
    e.set()

def testExecution():

    # 1) Startup behaviour
    # - Setup callback on comparator input
    comparator = Comparator.Comparator(ipcon,UID_ANALOG_IN,callback,20)

    # - Store timestamp
    timeStart = datetime.now()

    # - Enable Power Supply via relay
    powerSupply = PowerSupply.PowerSupply(ipcon,UID_DUAL_RELAY)
    # - Store timestamp upon callback trigger
    # - Calculate timestamp difference
    # 10s timeout
    event_is_set = e.wait(10)

    if event_is_set == False:
        print("Timeout occurred!")
        return False

    timeEnd = datetime.now()
    deltaTime = timeEnd - timeStart
    print(deltaTime.total_seconds())

    # 2) Power Consumption
    # - Put DUT in right mode
    # - Measure power consumption
    # - Switch On Load
    # -- Measure power consumption
    # -- Measure voltage


    #loop = asyncio.get_event_loop()
    #loop.run_until_complete(hello_world())
    #loop.close()

    return True

ipcon = IPConnection()
ipcon.connect(HOST, PORT) # Connect to brickd

UID_ANALOG_IN="F8S"
UID_DUAL_RELAY="EaZ"

e = threading.Event()

if testExecution():
    print("Test successfull")

ipcon.disconnect()
print("Master script finish...")
