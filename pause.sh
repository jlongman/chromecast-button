device=`cat ./device`
device=${device:=4}
echo "tx 1$device:44:46" | cec-client -s -d 1
