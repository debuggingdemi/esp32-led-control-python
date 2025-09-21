#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""


@author: demi
"""
import serial
import time    # if you want to add delays
import csv
from datetime import datetime 
import serial.tools.list_ports


ser = serial.Serial(port='/dev/cu.usbserial-1410', baudrate = 115200, timeout = 1) # pointing to your port, choose baudrate speed and a timeout = wait 1 second max


filename = f"led_log_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
with open(filename,mode='w') as file:
    writer = csv.writer(file)
    writer.writerow(["Timestamp", "Command","Response"])

if not ser.is_open: # condition checks if serial connection and reopens if exit command used
    ser.open()
while True:
    with open(filename,mode='a') as file:
        writer = csv.writer(file)
        command = input("Enter command (on/off/exit): ").strip().lower() # a litte note: [strip] removes empty spaces; [lower] makes entries lowcase
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        if command in ["on", "off"]:
            ser.write((command + "\n").encode()) #encode converts to byte
            response = ser.readline().decode().strip() # decode converts byte to string 
            print("ESP32:", response)
            
            writer.writerow([timestamp, command, response])
               
        elif command == "exit":
            print("Closing connection...")
            ser.close() #closes serial communication 
            break     # exits while loop 
        else:
            writer.writerow([timestamp, command, "Invalid command"])
            print("Invalid command.")
            
        
        
        
        
        
        