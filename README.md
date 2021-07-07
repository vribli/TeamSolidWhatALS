# TeamSolidWhatALS
Adaptive Light Sensor project for HackAlliance

## Description
We are Team SolidWhat, presenting our project Adaptive Light Sensor project for HackAlliance 2021. Through our market research, we have identify a gap between individual brightness preferences under different lighting conditions and devices’ capability to automatically detect and adjust the brightness. Thus, we have come up with our solution, EnLIGHTen your screen, a dynamic brightness adjustment solution which captures the users preferences and adapt to the changes to provide a better user experience.

This folder contains all the python scripts for the implementation of the project.

## Installation
> $pip install -r requirements.txt


## Python Version
* Python 3.7.3

## Hardware Requirements

* BH1750
* Raspberry Pi Model 4
* Monitor with DDC capability and Enabled
* To Enable DDC on monitor use the physical buttons present on the monitor

## Implementation
This project is implemented by using an RPi Model 4 and a BH1750 Light Sensor. They are connected as bellow
* VCC to 5V on RPi
* GND to GND on RPi
* SDA to GPIO 2 (SDA) on RPi
* SCL to GPIO 3 (SCL) on Rpi

## Use the following command to run the code
> $python3 main.py

## Use the following command to manually set the brightness of the monitor
> $python3 manual.py

## Roadmap/Future Improvements
1) To have different brightness profile depending on the wifi address


