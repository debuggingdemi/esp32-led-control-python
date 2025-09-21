#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""


@author: demi
"""
import requests #library allows you to send HTTP requests 

mcu_ip = "192.168.X.X" #IP address of your microcontroller (MCU)
base_url = f"http://{mcu_ip}" 

print("ESP32 Wi-Fi LED Control (HTTP)")
print("Type 'on', 'off', or 'exit'")

while True: #runs inifinite loop until exit command

    command = input("Enter Command:").strip().lower()  #user command
    
    if command in ["exit"]: # exits loop closes program
        print("Exiting")
        break
           
    elif command in ["on", "off"]: 
        try:
            response = requests.get(f"{base_url}/{command}") # sends GET response to MCU
            if response.status_code == 200:                  # checks if MCU responds with 200 OK (success)
                print(f"LED turned {command.upper()}")
            else:                                            # MCU responds with something else (e.g. 404, 500)
                print("Error: Could not reach ESP32 (status code:", response.status_code, ")")
        except requests.exceptions.RequestException as e:
            print("Connection failed:", e)                      # 'e' prints the error message received 

    else:
        print("Invalid command. Please type 'on', 'off', or 'exit'.")


