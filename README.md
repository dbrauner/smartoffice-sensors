# smartoffice-sensors
Controlling interface of sensors of the building

<h2>Arduino</h2>

The code was made to run on Arduino Leonardo. 
Some ports are configured to read specific sensors:

**A0** Configured to read the value from a LDR sensor with 1k resistor in series.
**A2** Configured to read a distance sensor (Sharp model)
**A3** Configured to read a analog sound sensor.

The data is sent via USB (serial port), then read by an Raspbery PI. 
The raspberry PI sends the data to the final application via RESTful service.