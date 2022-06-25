import serial
import time

SERIAL_PORT = serial.Serial('com13', 9600, timeout=0)
time.sleep(2)
print(SERIAL_PORT.name+"  is opened !")
print("\n")

while(1):
    INCOMING = SERIAL_PORT.read(26)
    INCOMING=INCOMING.decode()
    print(INCOMING)
    time.sleep(1)
    INCOMING=""
