from datetime import datetime
import sys
import threading, time, json, random
from flask import current_app as app
from flask import Blueprint, render_template, request, redirect

try:
    import RPi.GPIO
except (RuntimeError, ModuleNotFoundError):
    import fake_rpi
    sys.modules['RPi'] = fake_rpi.RPi     # Fake RPi
    sys.modules['RPi.GPIO'] = fake_rpi.RPi.GPIO # Fake GPIO
    sys.modules['smbus'] = fake_rpi.smbus # Fake smbus (I2C)

view = Blueprint("view", __name__)

@view.route("/")
def homepage():
    return render_template("homepage.html")

@view.route("/update", methods=["POST"])
def update():
    sliderValue = request.form.get('sliderInput')
    print('Slider value: {0}'.format(sliderValue))
    return render_template("homepage.html", sliderValue = sliderValue)
