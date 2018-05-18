###############################################################################
# PowerSupply.py
#
# Contacts: Michael Glettig, Manuel Weber
# DATE: 16. May 2018														 
###############################################################################

from tinkerforge.ip_connection import IPConnection
from tinkerforge.bricklet_dual_relay import BrickletDualRelay

class PowerSupply:

    def __init__(self,ipcon: IPConnection,UID):
        self.dRelay = BrickletDualRelay(UID,ipcon)

    def enable(self):
        self.dRelay.set_state(True, True)

    def disable(self):
        self.dRelay.set_state(False, False)
