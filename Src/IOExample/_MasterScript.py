import IndustrialQuadRelay
import time

IndustrialQuadRelay.setPins(True,True,True,False)
time.sleep(1)
IndustrialQuadRelay.setPins(False,True,True,False)

print("Master script finish...")
