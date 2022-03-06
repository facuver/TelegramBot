import network
import utime


sta_if = network.WLAN(network.STA_IF); sta_if.active(True)
#sta_if.scan()                             # Scan for available access points
sta_if.connect("FRITZ!Box 7490", "28630543043598832676") # Connect to an AP
while not sta_if.isconnected():                      # Check for successful connection
    utime.sleep(1)
    print(".",end="")
print("Connected")
print(sta_if.ifconfig()[0])
