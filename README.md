# chromecast-button
Simple Raspberry Pi GPIO button to Chromecast pause/play

Attach a button to GPIO 4 (o whereever you like - but change the pin number in `button.py`) - pressing button will pause/play a chromecast (assuming it is device 4).

TODO: find the attached chromecast and target correctly - currently assume CC is `Playback 1`.  Another `Playback` device will move the ChromeCast address.
