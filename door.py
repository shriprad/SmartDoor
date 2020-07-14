
import RPi.GPIO as GPIO
import time
motorDelay=4

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7,GPIO.IN)


def func():


    while k!=1 and f!=0:
        GPIO.output(in1,GPIO.HIGH)
        GPIO.output(in2,GPIO.LOW)
        print("Obstacle detected while closing the door")

GPIO.add_event_detect(7, GPIO.RISING, callback=func, bouncetime=3)



while f==1:
    GPIO.output(in1,GPIO.HIGH)
    GPIO.output(in2,GPIO.LOW)

while k==1:                     #1 is no detection
    GPIO.output(in1,GPIO.LOW)
    GPIO.output(in2,GPIO.LOW)


while j==1:
    GPIO.output(in1,GPIO.LOW)                   #0 is door not locked state
    GPIO.output(in2,GPIO.HIGH)



GPIO.remove_event_detect(7)
GPIO.cleanup()
print("Done")
