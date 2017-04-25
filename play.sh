#!/bin/bash

device=`cat /home/pi/chromecast-button/device`
device=${device:=4}


you=`basename "$0"`
case $you in
stop*)
  echo "tx 1$device:42:03" | cec-client -s -d 1
  echo stop
  ;;
pause*)
  echo "tx 1$device:44:46" | cec-client -s -d 1
  echo bar
  ;;
*)
  echo "tx 1$device:44:44" | cec-client -s -d 1
  echo play
  ;;
esac
