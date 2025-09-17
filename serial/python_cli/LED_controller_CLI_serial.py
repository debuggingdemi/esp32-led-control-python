#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 14 14:54:08 2025

@author: demittria
"""
import serial
import time    # if you want to add delays

import serial.tools.list_ports

ports = serial.tools.list_ports.comports()
#for port in ports:
    #print(f"Device: {port.device}, Description: {port.description}") #this is check your serial ports 

ser = serial.Serial(port='/dev/cu.usbserial-1410', baudrate = 115200, timeout = 1) # pointing to your port, choose baudrate speed and a timeout = wait 1 second max



# UNCOMMENT this to check LED ON and ESP32 response should return "LED turned ON"
#ser.write(b"on\n")  
#response = ser.readline().decode().strip()
#print(response)

# UNCOMMENT this to check LED OFF and ESP32 response should return "LED turned OFF"
#ser.write(b"off\n")  # "b" converts/encodes unicode input to a literal byte 
#response = ser.readline().decode().strip()
#print(response)

if not ser.is_open: # condition checks if serial connection and reopens if exit command used
    ser.open()
while True:
    command = input("Enter command (on/off/exit): ").strip().lower() # a litte note: [strip] removes empty spaces; [lower] makes entries lowcase
    if command in ["on", "off"]:
        ser.write((command + "\n").encode()) #encode converts to byte
        response = ser.readline().decode().strip() # decode converts byte to string 
        print("ESP32:", response)
    elif command == "exit":
        print("Closing connection...")
        ser.close() #closes serial communication 
        break     # exits while loop 
    else:
        print("Invalid command.")