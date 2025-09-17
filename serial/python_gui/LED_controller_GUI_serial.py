#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 16 14:34:57 2025

@author: demittria
"""
import tkinter as tk
import serial 

ser = serial.Serial(port='/dev/cu.usbserial-1410', baudrate = 115200, timeout = 1)

#Create main window
window = tk.Tk()
window.title("ESP32 LED Controller")
window.geometry("300x150")

def led_on():
    ser.write(("on" + "\n").encode())
    led_status_update.config(text="ON", fg= 'green')
    
def led_off():
    ser.write(("off" + "\n").encode())
    led_status_update.config(text="OFF",fg = "red")

#Header Label
label_title = tk.Label(window, text="TURN LED:", font=('Arial',14))
label_title.grid(row = 0, columnspan=2, pady= 10)


# ON button
on_button = tk.Button(window, text = "ON", command = led_on, width = 10)
on_button.grid(row = 1, column=0, padx= 10, pady = 5)

# OFF button
off_button = tk.Button(window,text= "OFF", command= led_off ,width = 10)
off_button.grid(row = 1, column=1, padx= 10, pady = 5)

# LED status
led_status = tk.Label(window, text= "LED STATUS:")
led_status.grid(row=2, column = 0, padx=10, pady =5)

led_status_update = tk.Label(window, text = " ")
led_status_update.grid(row=2, column = 1, padx=10, pady =5)

window.mainloop()