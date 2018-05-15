#!/usr/bin/env python
# -*- coding: utf-8 -*-
from tinkerforge.ip_connection import IPConnection
from tinkerforge.bricklet_dual_relay import BrickletDualRelay

class PowerSupply:

    def __init__(self,ipcon: IPConnection,UID):
        self.dRelay = BrickletDualRelay(UID,ipcon)

    def enable():
        # TODO
        #self.dRelay.

    def disable():
        # TODO
