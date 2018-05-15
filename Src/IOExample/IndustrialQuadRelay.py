#!/usr/bin/env python
# -*- coding: utf-8 -*-

# File:     IndustrialQuadRelay.py
# Author:   Michael Glettig
# Date:     15.05.2018
#
# Usage:    IndustrialQuadRelay.setPins(True,True,True,False)

HOST = "localhost"
PORT = 4223
UID_RELAY = "By2" # Change to the UID of your Industrial Quad Relay Bricklet

import sys
import time

from tinkerforge.ip_connection import IPConnection
from tinkerforge.bricklet_industrial_quad_relay import BrickletIndustrialQuadRelay

def setPins(output1,output2,output3,output4):
      ipcon = IPConnection() # Create IP connection
      relay = BrickletIndustrialQuadRelay(UID_RELAY, ipcon) # Create device object

      ipcon.connect(HOST, PORT) # Connect to brickd
      # Don't use device before ipcon is connected

      relayValue = 0

      if output1:
          relayValue |= (1 << 0)

      if output2:
          relayValue |= (1 << 1)

      if output3:
          relayValue |= (1 << 2)

      if output4:
          relayValue |= (1 << 3)

      relay.set_value(relayValue)

      ipcon.disconnect()
