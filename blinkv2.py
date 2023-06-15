import cv2
import cvzone
from cvzone.FaceMeshModule import FaceMeshDetector
from cvzone.PlotModule import LivePlot
import macmouse as m
import time
import serial
from multiprocessing import Process
import textui as tui
from tkinter import *
import word_generator as word


def blink():
    cap = cv2.VideoCapture(0)
    detector = FaceMeshDetector(maxFaces=1)
    plotY = LivePlot(640, 360, [25, 40], invert=True)

    idList = \
    [22, 23, 24, 26, 110, 157, 158, 159, 160, 161, 130, 243, 
    252, 253, 254, 256, 339, 384, 385, 386, 387, 388, 359, 463
    ]
    
    r_ratioList = []
    l_ratioList = []
    blinkCounter = 0
    counter = 0

    while True:
        success, img = cap.read()
        img, faces = detector.findFaceMesh(img, draw=False)

        if faces:
            face = faces[0]
            for id in idList:
                cv2.circle(img,face[id], 5, (255, 0, 255), cv2.FILLED)

            rightUp = face[386]
            rightDown = face[253]
            rightLeft = face[359]
            rightRight = face[463]
            leftUp = face[159]
            leftDown = face[23]
            leftLeft = face[130]
            leftRight = face[243]
            y_length_r, _ = detector.findDistance(rightUp, rightDown)
            x_length_r, _ = detector.findDistance(rightRight, rightLeft)
            y_length_l, _ = detector.findDistance(leftUp, leftDown)
            x_length_l, _ = detector.findDistance(leftRight, leftLeft)
            cv2.line(img, rightUp, rightDown, (0, 200, 0), 3)
            cv2.line(img, rightRight, rightLeft, (0, 200, 0), 3)
            cv2.line(img, leftUp, leftDown, (0, 200, 0), 3)
            cv2.line(img, leftRight, leftLeft, (0, 200, 0), 3)
            eye_ratio_r = int((y_length_r/x_length_r) * 100)
            eye_ratio_l = int((y_length_l/x_length_l) * 100)
            r_ratioList.append(eye_ratio_r)
            l_ratioList.append(eye_ratio_l)
            if len(r_ratioList) > 3: 
                r_ratioList.pop(0)
            r_ratioAvg = sum(r_ratioList)/len(r_ratioList)
            if len(l_ratioList) > 3: 
                l_ratioList.pop(0)
            l_ratioAvg = sum(l_ratioList)/len(l_ratioList)

            if (l_ratioAvg + r_ratioAvg)//2 <= 26 and counter == 0:
                blinkCounter += 1
                counter = 1

            if blinkCounter == 2:
                m.click(button='left');
                blinkCounter = 0
            
            if counter != 0:
                counter += 1
                if counter > 5:
                    counter = 0

            cvzone.putTextRect(img, f"Blink Count: {blinkCounter}", (50, 100))

            imgPlot = plotY.update((l_ratioAvg+r_ratioAvg)//2)
            img = cv2.resize(img, (640, 360))
            imgStack = cvzone.stackImages([img, imgPlot], 2, 1)
        else:
            img = cv2.resize(img, (640, 360))
            imgStack = cvzone.stackImages([img, img], 2, 1)

        cv2.imshow("Image", imgStack)
        cv2.waitKey(10)


def mouse_function():
    arduino = serial.Serial('/dev/cu.usbserial-14440')
    arduino.baudrate = 9600

    print("Initializing...")
    time.sleep(2)

    print("Mouse activated")
    while True:
        data = arduino.readline().split()
        m.move(720 + int(data[1]) / 8, -500 - int(data[0]) / 5)
        time.sleep(0.0005)

if __name__ == '__main__':
    p1 = Process(target=mouse_function)
    p2 = Process(target=blink)
    p3 = Process(target=tui.user_interface)
    p1.start()
    p2.start()
    p3.start()
    p1.join()
    p2.join()
    p3.join()