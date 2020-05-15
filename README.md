# Servos_pi
Simple flask webapp running on [Raspberry Pi](https://www.raspberrypi.org/) to show
a sample of how to use a slider to control a servo motor (Micro Servo SG90)

## Getting Started

### Prerequisites
Micro Servo SG90 connected to Raspberry Pi

### Installing

From project root create virtual environment, activate it and install requirements:

```sh
~/Servos_pi$ python3 -m venv venv
~/Servos_pi$ source venv/bin/activate
~/Servos_pi$ pip install -r requirements.txt
```

## Running

__as app__

```sh
export FLASK_APP=flaskr
flask run
```

__as wsgi server__

```sh
gunicorn --worker-class eventlet -w 1 -b localhost:8080 wsgi
```

## Deployment

As seen above, as any wsgi app.

## Authors 

Franco Parodi <franco.parodi@aol.com>

## License

This project is licensed under the MIT License.
