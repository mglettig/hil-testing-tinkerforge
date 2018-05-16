#!/usr/bin/env python
# -*- coding: utf-8 -*-
from tinkerforge.ip_connection import IPConnection
from tinkerforge.bricklet_dual_relay import BrickletDualRelay

class PowerSupply:

    def __init__(self,ipcon: IPConnection,UID):
        self.dRelay = BrickletDualRelay(UID,ipcon)

    def enable(self):
        self.dRelay.set_state(True, True)

    def disable(self):
        self.dRelay.set_state(False, False)
