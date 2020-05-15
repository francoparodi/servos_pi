import json
from datetime import datetime

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Settings(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, default=datetime.now)
    temperatureUm = db.Column(db.String(2), unique=False, default='°C')
    humidityUm = db.Column(db.String(1), unique=False, default='%')
    pressureUm = db.Column(db.String(6), unique=False, default='mBar')
    readFromSensorInterval = db.Column(db.Integer(), unique=False, default=10)
    minDeltaDataTrigger = db.Column(db.Float(1), unique=False, default=1)
    temperatureCorrection = db.Column(db.Float(1), unique=False, default=0.0)
    humidityCorrection = db.Column(db.Integer, unique=False, default=0)
    pressureCorrection = db.Column(db.Integer, unique=False, default=0)
    storeStatsDataLimit = db.Column(db.Integer(), unique=False, default=0)
    showLastEvent = db.Column(db.Boolean, unique=False, default=False)
    sensorSimulation = db.Column(db.Boolean, unique=False, default=False)

    def __repr__(self):
        repr = "{0}, {1}, {2}, {3}, {4}, {5}, {6}".format(
            { self.id },
            { self.created_at },
            { self.temperatureUm },
            { self.humidityUm },
            { self.pressureUm },
            { self.readFromSensorInterval },
            { self.minDeltaDataTrigger },
            { self.temperatureCorrection },
            { self.humidityCorrection },
            { self.pressureCorrection },
            { self.storeStatsDataLimit },
            { self.showLastEvent },
            { self.sensorSimulation }

        )
        return repr

class Stats(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, default=datetime.now)
    temperature = db.Column(db.Float(1), unique=False, default=0.0)
    humidity = db.Column(db.Integer, unique=False, default=0)
    pressure = db.Column(db.Integer, unique=False, default=0)
    temperatureUm = db.Column(db.String(2), unique=False, default='°C')
    humidityUm = db.Column(db.String(1), unique=False, default='%')
    pressureUm = db.Column(db.String(6), unique=False, default='mBar')
    sensorSimulation = db.Column(db.Boolean, unique=False, default=False)

    def __repr__(self):
        repr = "{0}, {1}, {2}, {3}, {4}, {5}, {6}".format(
            { self.id },
            { self.created_at },
            { self.temperature },
            { self.humidity },
            { self.pressure },
            { self.temperatureUm },
            { self.humidityUm },
            { self.pressureUm },
            { self.sensorSimulation }
        )
        return repr

class EnvironmentData(object):
    def __init__(self):
        self.__dateTime = str(datetime.now())
        self.__temperature = 0.0
        self.__humidity = 0.0
        self.__pressure = 0
        self.__temperatureUm = '°C'  
        self.__humidityUm = '%'
        self.__pressureUm = 'mBar'
        self.__sensorSimulation = False

    # getters
    def get_dateTime(self):
        return self.__dateTime
    
    def get_temperature(self):
        return self.__temperature
    
    def get_humidity(self):
        return self.__humidity

    def get_pressure(self):
        return self.__pressure
    
    def get_temperatureUm(self):
        return self.__temperatureUm

    def get_humidityUm(self):
        return self.__humidityUm
    
    def get_pressureUm(self):
        return self.__pressureUm
    
    def get_sensorSimulation(self):
        return self.__sensorSimulation

    # setters
    def set_dateTime(self, value):
        self.__dateTime = value
    
    def set_temperature(self, value):
        self.__temperature = value
    
    def set_humidity(self, value):
        self.__humidity = value

    def set_pressure(self, value):
        self.__pressure = value
    
    def set_temperatureUm(self, value):
        self.__temperatureUm = value

    def set_humidityUm(self, value):
        self.__humidityUm = value
    
    def set_pressureUm(self, value):
        self.__pressureUm = value

    def set_sensorSimulation(self, value):
        self.__sensorSimulation = value

    def __repr__(self):
        repr = "{0}, {1}, {2}, {3}, {4}, {5}, {6}".format(
            { self.__dateTime },
            { self.__temperature },
            { self.__humidity },
            { self.__pressure },
            { self.__temperatureUm },
            { self.__humidityUm },
            { self.__pressureUm },
            { self.__sensorSimulation }
        )
        return repr

    def toJson(self):
        return json.dumps(self.__dict__)