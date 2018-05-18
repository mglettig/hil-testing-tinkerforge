###############################################################################
# _MasterScript.py
#
# Contacts: Michael Glettig, Manuel Weber
# DATE: 16. May 2018
###############################################################################

import Comparator
import PowerSupply
import PowerConsumption
import time
from tinkerforge.ip_connection import IPConnection
import asyncio
import threading
from datetime import datetime
import yaml

def read_from_yaml_file(filename):
    try:
        with open(filename, 'r') as f:
            data = yaml.load(f)
    except yaml.YAMLError as exc:
         print(exc)
    return data

def read_config():
    yaml_data = read_from_yaml_file("config.yml")
    global UID_ANALOG_IN
    UID_ANALOG_IN = yaml_data['UID_ANALOG_IN']
    global UID_DUAL_RELAY
    UID_DUAL_RELAY = yaml_data['UID_DUAL_RELAY']
    global UID_VOLTAGE_CURRENT
    UID_VOLTAGE_CURRENT = yaml_data['UID_VOLTAGE_CURRENT']
    global HOST
    HOST = yaml_data['HOST']
    global PORT
    PORT = yaml_data['PORT']

def callback(voltage):
    print("Callback triggered!")
    e.set()

def testExecution():

    # 1) Startup behaviour
    # - Setup callback on comparator input
    powerConsumption = PowerConsumption.PowerConsumption(ipcon,UID_VOLTAGE_CURRENT)
    # powerSupply.disable()
    comparator = Comparator.Comparator(ipcon,UID_ANALOG_IN,callback,20)

    # - Store timestamp
    timeStart = datetime.now()

    # - Enable Power Supply via relay
    powerSupply.enable()

    # - Store timestamp upon callback trigger
    # - Calculate timestamp difference
    # 10s timeout
    event_is_set = e.wait(10)

    if event_is_set == False:
        print("Timeout occurred!")
        return False

    timeEnd = datetime.now()
    deltaTime = timeEnd - timeStart
    print("Startup time in (s): ",deltaTime.total_seconds())

    # 2) Power Consumption
    # - Put DUT in right mode
    # - Measure power consumption
    print("Voltage in (V): ",powerConsumption.getVoltage()/1000)
    print("Current in (mA): ",powerConsumption.getCurrent())
    print("Power in (mW): ",powerConsumption.getPower()/1000)

    # - Switch On Load
    # -- Measure power consumption
    # -- Measure voltage


    #loop = asyncio.get_event_loop()
    #loop.run_until_complete(hello_world())
    #loop.close()



    return True

read_config()

ipcon = IPConnection()
ipcon.connect(HOST, PORT) # Connect to brickd

powerSupply = PowerSupply.PowerSupply(ipcon,UID_DUAL_RELAY)

e = threading.Event()

if testExecution():
    print("Test successfull")

input("Press key to exit\n")

powerSupply.disable()
ipcon.disconnect()
print("Master script finished...")
