# chromecast-button
Simple Raspberry Pi GPIO button to Chromecast pause/play

Attach a button to GPIO 4 (o whereever you like - but change the pin number in `button.py`) - pressing button will pause/play a chromecast (assuming it is device 4).

This code will find the attached chromecast and target correctly - currently deaults CC as `Playback 1`.  Another `Playback` device should move the ChromeCast address (not tested as my TV network is very simple, no DVD player etc).
