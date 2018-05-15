#!/usr/bin/env python
# -*- coding: utf-8 -*-
from tinkerforge.ip_connection import IPConnection
from tinkerforge.bricklet_analog_in_v3 import BrickletAnalogInV3

class Comparator:
    threshold = 20

    def __init__(self,ipcon: IPConnection,UID):
        # TODO

        analogIn = BrickletAnalogInV3(UID,ipcon)
        analogIn.register_callback(analogIn.CALLBACK_VOLTAGE, cb_voltage)

        # Configure threshold for voltage "greater than threshold"
        # with a debounce period of 0.2s (200ms)
        analogIn.set_voltage_callback_configuration(200, True,
        BrickletAnalogInV3.THRESHOLD_OPTION_GREATER,
        20000, 0)



def cb_voltage(voltage):
    print("Voltage: " + str(voltage/1000.0) + " V")
