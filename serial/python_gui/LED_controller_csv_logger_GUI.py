#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""


@author: demi
"""

import tkinter as tk
import serial 
import csv
from datetime import datetime 

ser = serial.Serial(port='/dev/cu.usbserial-1410', baudrate = 115200, timeout = 1)

#Create main window
window = tk.Tk()
window.title("ESP32 LED Controller")
window.geometry("300x180")

filename = f"led_log_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
with open(filename,mode='w') as file:
    writer = csv.writer(file)
    writer.writerow(["Timestamp", "Command","Response"])
    
def led_command(command):
    
    with open(filename,mode='a') as file:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        ser.write((command+"\n").encode())
        response = ser.readline().decode().strip()
        
        writer = csv.writer(file)
        writer.writerow([timestamp,command,response])
        
        if command == "on":
            led_status_update.config(text="ON", fg= 'green')
        if command == "off":
            led_status_update.config(text="OFF", fg= 'red')
        
def exit_button():
    ser.close()
    
                        

#Header Label
label_title = tk.Label(window, text="TURN LED:", font=('Arial',14))
label_title.grid(row = 0, columnspan=2, pady= 10)


# ON button
on_button = tk.Button(window, text = "ON", command = lambda:led_command("on"), width = 10)
on_button.grid(row = 1, column=0, padx= 10, pady = 5)

# OFF button
off_button = tk.Button(window,text= "OFF", command= lambda:led_command("off") ,width = 10)
off_button.grid(row = 1, column=1, padx= 10, pady = 5)

# LED status
led_status = tk.Label(window, text= "LED STATUS:")
led_status.grid(row=2, column = 0, padx=10, pady =5)

led_status_update = tk.Label(window, text = " ")
led_status_update.grid(row=2, column = 1, padx=10, pady =5)

# Save log Data button
log_button = tk.Button(window, text = "SAVE LOG DATA", command=exit_button, width = 10)
log_button.grid(row=3, columnspan=2, pady= 10)
window.mainloop()





