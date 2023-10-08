import serial
from flask import Flask

ser = serial.Serial("COM3", 115200)

def get_value():
    ser.write(b"getValue\n")

    while True:
        if data := ser.readline()[:-2]:
            return data


app = Flask(__name__)


@app.route("/")
def index():
    val = get_value().decode().strip()

    if val == "0":
        return "<h1>La porte est ouverte !</h1>"
    else:
        return "<h1>La porte est fermée</h1>"