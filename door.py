import serial

ser = serial.Serial("COM3", 115200)

def getState():
    ser.write(b"getValue\n")

    while True:
        line = ser.readline().decode().strip()
        print(line)

        if line == "0":
            return "door_open"
        elif line == "1":
            return "door_close"
