import sys, atexit, time
from flask import current_app as app
from flask import Blueprint, render_template, request

try:
    import RPi.GPIO as GPIO
except (RuntimeError, ModuleNotFoundError):
    import fake_rpi
    GPIO = fake_rpi.RPi.GPIO
    sys.modules['RPi'] = fake_rpi.RPi
    sys.modules['RPi.GPIO'] = fake_rpi.RPi.GPIO
    sys.modules['smbus'] = fake_rpi.smbus

view = Blueprint("view", __name__)

GPIO.setmode(GPIO.BOARD)
#pin 11
GPIO.setup(11,GPIO.OUT)
#pin 11, 50Hz pulse
servo = GPIO.PWM(11,50)
servo.start(0)
time.sleep(2)

values = {'0.00':2, '36.00':4, '72.00':6, '108.00':8, '144.00':10, '180.00':12}

@view.route("/")
def homepage():
    return render_template("homepage.html")

@view.route("/", methods=["POST"])
def update():
    sliderValue = request.form.get('sliderInput')
    dutyCycle = values[sliderValue]
    move(dutyCycle)
    return render_template("homepage.html", sliderValue = sliderValue)

def move(dutyCycle=2):
    servo.ChangeDutyCycle(dutyCycle)
    time.sleep(1)
    servo.ChangeDutyCycle(0)
    time.sleep(0.5)

def cleanUp():
    print('Safe terminating.')
    move()
    GPIO.cleanup()

atexit.register(cleanUp)