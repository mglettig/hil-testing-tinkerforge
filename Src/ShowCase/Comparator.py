#!/usr/bin/env python
# -*- coding: utf-8 -*-
from tinkerforge.ip_connection import IPConnection
from tinkerforge.bricklet_analog_in_v3 import BrickletAnalogInV3

class Comparator:

    def __init__(self,ipcon: IPConnection,UID,callback,threshold=20):
        self.callback = callback
        self.threshold = threshold
        self.analogIn = BrickletAnalogInV3(UID,ipcon)

        self.analogIn.register_callback(
         BrickletAnalogInV3.CALLBACK_VOLTAGE,
         self.cb_voltage)

        # Configure threshold for voltage "greater than threshold"
        # with a debounce period of 0.2s (200ms)
        self.analogIn.set_voltage_callback_configuration(200, True,
         BrickletAnalogInV3.THRESHOLD_OPTION_GREATER,
         self.threshold*1000, 0)

    def cb_voltage(self,voltage):
        print("Voltage: " + str(voltage/1000.0) + " V")

        # Disable Callback...
        self.analogIn.set_voltage_callback_configuration(0, True,
         BrickletAnalogInV3.THRESHOLD_OPTION_OFF,0,0)

        # Trigger listener
        self.callback(voltage)
