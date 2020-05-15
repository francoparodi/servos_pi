import random

class SenseHatMock(object):

    def __init__(self):
        self.__low_light = False
        self.__pixels = []

    def get_temperature(self):
        return random.uniform(-20,50)

    def get_humidity(self):
        return random.uniform(0,99)

    def get_pressure(self):
        return random.uniform(800,1100)

    def show_message(self, msg):
        pass