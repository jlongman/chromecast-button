# chromecast-button
Simple Raspberry Pi GPIO button to Chromecast pause/play

Attach a button to GPIO 4 (o whereever you like - but change the pin number in `button.py`) - pressing button will pause/play a chromecast (assuming it is device 4).

This code will find the attached chromecast and target correctly - currently deaults CC as `Playback 1`.  Another `Playback` device should move the ChromeCast address (not tested as my TV network is very simple, no DVD player etc).

## Sample setup:

<img src="https://cloud.githubusercontent.com/assets/1051995/24589933/2cedf5c0-17b1-11e7-962b-c11e362251a2.JPG" alt="pi with button" width="400" >

The red button is attached to pin 4, the mystery jack near the HDMI port is the IR blaster, the LED is visible as red plastic beside the blue power LED on the TV.  The whole with wires coming out of it will have the IR receiver (when received).  The component jack was physically removed from the Pi board to allow the IR receiver to take it's place.  

All leads are kept long and so the top of the case can be removed easily, as all components are added to the top portion of the case.  All contacts are done with wire-wrapping as it's fast, easy and good enough for this project.
