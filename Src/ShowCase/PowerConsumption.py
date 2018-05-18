###############################################################################
# PowerConsumption.py
#
# Contacts: Michael Glettig, Manuel Weber
# DATE: 16. May 2018														 
###############################################################################

from tinkerforge.ip_connection import IPConnection
from tinkerforge.bricklet_voltage_current import BrickletVoltageCurrent

class PowerConsumption:

    def __init__(self,ipcon: IPConnection,UID):
        self.voltageCurrent = BrickletVoltageCurrent(UID,ipcon)
        self.voltageCurrent.set_configuration(7,7,7)

    def getVoltage(self):
        return self.voltageCurrent.get_voltage()

    def getCurrent(self):
        return self.voltageCurrent.get_current()

    def getPower(self):
        return self.voltageCurrent.get_voltage() * self.voltageCurrent.get_current()
