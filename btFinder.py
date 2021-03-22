#                    GNU GENERAL PUBLIC LICENSE
#                       Version 3, 29 June 2007
#
# Copyright (C) 2007 Free Software Foundation, Inc. <https://fsf.org/>
# Everyone is permitted to copy and distribute verbatim copies
# of this license document, but changing it is not allowed.
#=====================================================
#Library import in order to make the script works propertly
#Tested with python3
import bluetooth
targetName = "EVD" #My phone
targetAdd = "20:20:11:34:44:16" #MAC Address

#How many scans needed to be sure about discoverable device
for i in range(0,10):
 nearbyDevs = bluetooth.discover_devices(duration=10,flush_cache=True, lookup_names=False)
 print(nearbyDevs)
 if targetAdd in nearbyDevs:
  print("Encontrado en rango") #== bluetooth.lookup_name(bdaddr):
 else:
  print("No esta en rango")
