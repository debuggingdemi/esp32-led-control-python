#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""


@author: demi
"""
import requests

import tkinter as tk

#Create main window
window = tk.Tk()
window.title("ESP32 LED Controller")
#window.geometry("300x180")

mcu_ip = "192.168.X.X" #IP address of your microcontroller (MCU)
base_url = f"http://{mcu_ip}" 

def led_command(command):
      
    try:
        response = requests.get(f"{base_url}/{command}") # sends GET response to MCU
        if response.status_code == 200:
            
            if command == "on":
                led_status_update.config(text="ON", fg= 'green')
                led_error.config(text= " ")
            elif command == "off":
                led_status_update.config(text="OFF",fg = "red")
                led_error.config(text= " ")
        else:                                                                                                   
            led_error.config(text=f"Error code: {response.status_code}", fg="orange")
   
    except requests.exceptions.RequestException as e:
        print("Connection failed:", e) 
        led_status_update.config(text= "Connection failed", fg='red')
        led_error.config(text="Device not reachable", fg="orange")

#Header Label
label_title = tk.Label(window, text="TURN LED:", font=('Arial',14))
label_title.grid(row = 0, columnspan=2, pady= 10)


# ON button
on_button = tk.Button(window, text = "ON", command = lambda: led_command("on") , width = 10)
on_button.grid(row = 1, column=0, padx= 10, pady = 5)

# OFF button
off_button = tk.Button(window,text= "OFF", command= lambda: led_command("off") ,width = 10)
off_button.grid(row = 1, column=1, padx= 10, pady = 5)

# LED status
led_status = tk.Label(window, text= "LED STATUS:")
led_status.grid(row=2, column = 0, padx=10, pady =5)

led_status_update = tk.Label(window, text = " ")
led_status_update.grid(row=2, column = 1, padx=10, pady =5)

led_error = tk.Label(window, text = " ")
led_error.grid(row=3, columnspan = 2, padx = 10, pady = 5)


window.mainloop()
