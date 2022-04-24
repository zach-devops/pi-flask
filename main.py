'''

Adapted excerpt from Getting Started with Raspberry Pi by Matt Richardson

Modified by Rui Santos
Complete project details: https://randomnerdtutorials.com

'''

from gpiozero import LED
from time import sleep
from flask import Flask, render_template, request


pin = LED(18)


app = Flask(__name__)

@app.route("/SmMGs491s4rKd&X&X$aqT&2kH$1rTQ23zJjMka33O@gQzg$Ny55y^do8GrtFcXxnGU&u4EY93VFC5996MuuPc8lvXHoVl@IyIQl")
def main():
   pin.on()
   sleep(2)
   pin.off()
   return "<p>gate open</p>"

if __name__ == "__main__":
   app.run(host='0.0.0.0', port=80, debug=True)