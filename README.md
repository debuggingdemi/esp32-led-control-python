ESP32 LED Control using UART (Serial) and HTTP (Wi-Fi) Communication Protocols

---

💡 Python + Arduino IDE Project

This beginner-friendly project demonstrates how to control the onboard LED of an ESP32 microcontroller using Python and Arduino, communicating over two protocols:

	1. UART (Serial via USB)
	2. HTTP (via Wi-Fi)

---

🔧 What You'll Learn

- Sending serial commands from Python (CLI & GUI)

- Creating a basic HTTP server on ESP32 using Arduino

- Sending GET requests using Python requests and Bash curl

- Building Python GUIs with tkinter

- Logging hardware responses to CSV (like validation reports)

- Connecting firmware, scripting, and physical control

---

📁 Project Structure

📦 Serial (USB)

Folder	Description

serial/arduino_firmware - Arduino sketch to handle UART commands (on/off)
serial/python_cli 	- CLI interface to send commands and log responses
serial/python_gui	- GUI interface with tkinter for button control and 'SAVE LOG' button
serial/bash		- Manual Bash commands (e.g., echo, screen)

🌐 Wi-Fi (HTTP)

Folder	Description

wifi/arduino_firmware 	- Arduino sketch hosting a web server (routes: /on, /off)
wifi/python_cli		- CLI with requests.get() to toggle via IP
wifi/python_gui		- GUI with tkinter over HTTP
wifi/bash		- Use curl to send HTTP commands via terminal

---

🛠️ Tools & Technologies

Microcontroller: ESP32-C6-WROOM-1

Languages: Arduino C++, Python 3

Libraries Used: serial, requests, csv, tkinter

Protocols: UART, HTTP

Platforms: macOS (primary), compatible with Linux/Windows

Dev Tools: Arduino IDE, Terminal, Python Spyder

---


🚀 Getting Started

**For Wi-Fi: Replace the SSID, password, and IP in the .ino sketch before uploading to the MCU.**

1. Upload the correct .ino firmware to the MCU

2. For Serial (USB):
	- Connect via USB (onboard UART/USB port)
	- Run Python script:
	in terminal: python LED_controller_CLI_serial.py or LED_controller_GUI_serial.py
		python LED_controller_CLI_serial_logger.py or LED_controller_csv_logger_GUI.py

3. For Wi-Fi (HTTP):
	- Connect ESP32 to your local 2.4GHz network
	- Access LED control via:
		1. Browser: http://<esp32_ip>/on or /off
		2. Bash: curl http://<esp32_ip>/on
		3. Python (in terminal): python led_wifi_cli.py or led_wifi_GUI.py

✅ Observe the LED toggle and log response (if enabled)

---

💬 Reflections

This project mimics real-world embedded automation tasks:

Validating command response logging to CSV 

Verifying microcontroller behaviour from user input

Exploring communication protocols in embedded systems

Combining low-level firmware logic with high-level scripting

It’s also beginner-friendly and helps break the “embedded systems = scary” myth 💪🏾

---

📜 License

This project is for educational and demonstrative use.
You're welcome to fork, adapt, or build upon it. 💙

---

👩🏾‍💻 Author

Demittria Mtenga
Electrical Engineer | Embedded Systems & Automation
🔗 [LinkedIn](https://www.linkedin.com/in/demittria-mtenga-20b162206)
