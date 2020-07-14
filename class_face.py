import numpy as np
import cv2
import pickle
import random
import time
import RPi.GPIO as GPIO
from time import sleep
in1 = 24
in2 = 23
en = 25




class Face(object):
    def __init__(self):

        face_cascade = cv2.CascadeClassifier('cascades/data/haarcascade_frontalface_alt2.xml')
        recognizer = cv2.face.LBPHFaceRecognizer_create()
        recognizer.read("trainer.yml")
        labels= {}


        with open("labels.pickle", 'rb') as f:
            og_labels= pickle.load(f)
            labels = {v:k for k,v in og_labels.items()}
        cap=cv2.VideoCapture(0)


        while(True):

            #print(v)
            ret, frame =cap.read()
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=5)
            for (x,y,h,w) in faces:
                roi_gray = gray[y:y+h, x:x+w]
                roi_color = frame[y:y+h, x:x+w]
                id_, conf= recognizer.predict(roi_gray)
                if (conf>=45 or conf <=85):
                    print("Welcome")

                    p2= Door(p1,l1,m1)

                else:
                    print("Please Try again. Thank You")
                    break

            cv2.imshow('frame', frame)
            if cv2.waitKey(20) & 0xFF == ord('q'):
                break


        cap.release()
        cv2.destroyAllWindows()
        break



class Door(Face):
    def __init__(self):
        def ob_detect(self,channel):
            while self.p1!=1 and self.l1!=0:
                print("Obstacle detected while closing the door")
                self.p1=GPIO.setup(22,GPIO.IN)
                self.l1=GPIO.setup(17,GPIO.IN)
                GPIO.output(in1,GPIO.HIGH)
                GPIO.output(in2,GPIO.LOW)


        GPIO.add_event_detect(7, GPIO.RISING, callback=ob_detect, bouncetime=300)

        while self.l1==1:
            print("Door has been opened")
            self.l1=GPIO.setup(17,GPIO.IN)
            GPIO.output(in1,GPIO.HIGH)
            GPIO.output(in2,GPIO.LOW)

        while self.p1==1:
            print("Door stays open until user passes ")
            self.p1=GPIO.setup(22,GPIO.IN)
            GPIO.output(in1,GPIO.LOW)
            GPIO.output(in2,GPIO.LOW)

        while self.m1==1:
            print("Closing the door")
            self.m1=GPIO.setup(5,GPIO.IN)
            GPIO.output(in1,GPIO.LOW)
            GPIO.output(in2,GPIO.HIGH)

        GPIO.remove_event_detect(7)
        GPIO.cleanup()








class ForcePush():
    def __init__(self):
        print("Buzzer Starts warning alaram begins for next 10 second")
        print("Please recognize your face to open the door. Thank You")
        GPIO.output(13,GPIO.HIGH)
        time.sleep(10)
        GPIO.output(13,GPIO.LOW)

def pushButton():


def forcePush():
    print("Buzzer Starts warning alaram begins for next 10 second")
    print("Please recognize your face to open the door. Thank You")
    GPIO.output(13,GPIO.HIGH)
    time.sleep(10)
    GPIO.output(13,GPIO.LOW)



        ##Here include the buzzer for next 10 seconds if someone tries to open the door forcefully


while(True):
    GPIO.setmode(GPIO.BCM)
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
        front=Face(p1,l1,m1)

    elif l2==0:
        ForcePush()

    else:
        print("Please show your face to unlock the door.")
