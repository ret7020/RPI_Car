import RPi.GPIO as GPIO
from time import sleep

# Pins for Motor Driver Inputs
Motor1A = 24
Motor1B = 23
Motor1E = 18#25

Motor2A = 16
Motor2B = 20
Motor2E = 21


def setup():
    GPIO.setmode(GPIO.BCM)				# GPIO Numbering
    GPIO.setup(Motor1A, GPIO.OUT)  # All pins as Outputs
    GPIO.setup(Motor1B, GPIO.OUT)
    GPIO.setup(Motor1E, GPIO.OUT)

    GPIO.setup(Motor2A, GPIO.OUT)
    GPIO.setup(Motor2B, GPIO.OUT)
    GPIO.setup(Motor2E, GPIO.OUT)


def forward():
    GPIO.output(Motor1A, GPIO.HIGH)
    GPIO.output(Motor1B, GPIO.LOW)
    GPIO.output(Motor1E, GPIO.HIGH)


def backward():
    GPIO.output(Motor1A, GPIO.LOW)
    GPIO.output(Motor1B, GPIO.HIGH)
    GPIO.output(Motor1E, GPIO.HIGH)

def steering_right():
    GPIO.output(Motor2A, GPIO.HIGH)
    GPIO.output(Motor2B, GPIO.LOW)
    GPIO.output(Motor2E, GPIO.HIGH)

def steering_left():
    GPIO.output(Motor2A, GPIO.LOW)
    GPIO.output(Motor2B, GPIO.HIGH)
    GPIO.output(Motor2E, GPIO.HIGH)


def clear():
    GPIO.output(Motor1E, GPIO.LOW)
    GPIO.output(Motor2E, GPIO.LOW)

def pwmable():
     pwm = GPIO.PWM(Motor1E, 100)
     pwm.start(0)
     GPIO.output(Motor1A, GPIO.HIGH)
     GPIO.output(Motor1B, GPIO.LOW)
     pwm.ChangeDutyCycle(80)
     GPIO.output(Motor1E, True)
     sleep(2)
     GPIO.output(Motor1E, False)
     pwm.ChangeDutyCycle(0)


def destroy():
    GPIO.cleanup()


if __name__ == "__main__":
    setup()
    print("Manual debug mode")
    while True:
        cmd = input("Cmd>")
        if cmd == "sr":
            steering_right()
            sleep(0.7)
        elif cmd == "sl":
            steering_left()
            sleep(2)
        elif cmd == "f":
            forward()
            sleep(0.5)
        elif cmd == "b":
            backward()
            sleep(0.5)
        elif cmd == "srf":
            steering_right()
            forward()
            sleep(1)
        elif cmd == "pwm":
            pwmable()
        elif cmd == "exit":
            break
        clear()
    destroy()

