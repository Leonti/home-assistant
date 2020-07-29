import serial
from time import sleep

with serial.Serial(port = '/dev/ttyUSB0', baudrate=9600) as ser:
  print("Sending serial command")
  str(ser.readline(), 'ascii')
  ser.write('on;'.encode(encoding = 'ascii'))
  ser.flush()
  line = str(ser.readline(), 'ascii')
  print(line)