import numpy as np
import cv2
import pickle
import random
import time
import RPi.GPIO as GPIO
from time import sleep
import hashlib
from pyfingerprint.pyfingerprint import PyFingerprint
from pyfingerprint.pyfingerprint import FINGERPRINT_CHARBUFFER1

in1 = 24
in2 = 23
GPIO.setmode(GPIO.BCM)


def door(): #This function handles opening and closing of the door
    def ob_detect(channel):
        while p1!=1 and l1!=0:
            print("Obstacle detected while closing the door")


            GPIO.output(in1,GPIO.HIGH)
            GPIO.output(in2,GPIO.LOW)
            p1=GPIO.setup(22,GPIO.IN)
            l1=GPIO.setup(17,GPIO.IN)

        GPIO.add_event_detect(7, GPIO.RISING, callback=ob_detect, bouncetime=300)


        while l1==1:
            print("Door is opening Please Wait")

            GPIO.output(in1,GPIO.HIGH)
            GPIO.output(in2,GPIO.LOW)
            l1=GPIO.setup(17,GPIO.IN)


        while p1==1:
            print("Door stays open until user passes ")
            GPIO.output(in1,GPIO.LOW)
            GPIO.output(in2,GPIO.LOW)
            p1=GPIO.setup(22,GPIO.IN)


        while m1==1:
            print("Closing the door")
            GPIO.output(in1,GPIO.LOW)
            GPIO.output(in2,GPIO.HIGH)
            m1=GPIO.setup(5,GPIO.IN)

        GPIO.remove_event_detect(7)
        GPIO.cleanup()



def finger_Print(): #This function handles detecting the fingerPrint of individual


    try:
        f = PyFingerprint('/dev/ttyUSB0', 57600, 0xFFFFFFFF, 0x00000000)
        if ( f.verifyPassword() == False ):
            raise ValueError('The given fingerprint sensor password is wrong!')

    except Exception as e:
        print('The fingerprint sensor could not be initialized!')
         print('Exception message: ' + str(e))
         exit(1)

    try:
        print('Waiting for finger...')

        while ( f.readImage() == False ):
            pass

        f.convertImage(FINGERPRINT_CHARBUFFER1)
        result = f.searchTemplate()
        positionNumber = result[0]
        accuracyScore = result[1]

        if ( positionNumber == -1 ):
            print('No fingerPrint found ,Please try again thank you')
            exit(0)

        else:
            print("Finger print found, Welcome")
            door()



def face_recognition(): #This function used for facial recognition of individual
    face_cascade = cv2.CascadeClassifier('cascades/data/haarcascade_frontalface_alt2.xml')
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.read("trainer.yml")
    labels= {}

    with open("labels.pickle", 'rb') as f:
        og_labels= pickle.load(f)
        labels = {v:k for k,v in og_labels.items()}
    cap=cv2.VideoCapture(0)

    while(True):
        ret, frame =cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=5)
        for (x,y,h,w) in faces:
            roi_gray = gray[y:y+h, x:x+w]
            roi_color = frame[y:y+h, x:x+w]
            id_, conf= recognizer.predict(roi_gray)
            if (conf>=45 or conf <=85):
                print("Face Detected")
                finger_Print()


            else:
                print("Please Try again. Thank You")
                break

    cap.release()
    v2.destroyAllWindows()
    break


    def force_push():
        print("Buzzer Starts warning alaram begins for next 10 second")
        print("Please recognize your face to open the door. Thank You")
        GPIO.output(13,GPIO.HIGH)
        time.sleep(10)
        GPIO.output(13,GPIO.LOW)







while(True):

    GPIO.setup(in1,GPIO.OUT)
    GPIO.setup(in2,GPIO.OUT)
    GPIO.setup(en,GPIO.OUT)
    GPIO.setup(13,GPIO.OUT)
    f1=GPIO.setup(7,GPIO.IN) #FaceProximity
    p1=GPIO.setup(22,GPIO.IN) #Passed Value
    l1=GPIO.setup(17,GPIO.IN) #limit switch
    m1=GPIO.setup(5,GPIO.IN) #Magnetic Sensor
    l2=GPIO.setup(6,GPIO.IN) #limitSwitch for force push
    button=GPIO.setup(8,GPIO.IN)

    GPIO.output(in1,GPIO.LOW)
    GPIO.output(in2,GPIO.LOW)

    p=GPIO.PWM(en,1000)
    p.start(25)

    if f1==0:
        face_recognition()

    elif l2==0:
        force_push()

    elif button==0:
        door()


    else:
        print("Please show your face to unlock the door.")
