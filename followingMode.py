import cv2
import numpy as np
import serial
import RPi.GPIO as GPIO
import pygame
import time

ser = serial.Serial('/dev/ttyUSB0')
ser.write(b'X90Y90')

pygame.mixer.init()
pygame.mixer.music.load("denemesesi.mp3")
pygame.mixer.music.play()


GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)
GPIO.setwarnings(False)
GPIO.output(18, GPIO.HIGH)


cap = cv2.VideoCapture(0)

cap.set(3, 480)
cap.set(4, 320)

_, frame = cap.read()
img2=cv2.rotate(frame,cv2.ROTATE_90_COUNTERCLOCKWISE)
rows, cols, _ = img2.shape

x_medium = int(cols / 2)
y_medium = int(rows / 2)
centerX = int(cols / 2)
centerY = int(rows / 2)
positionX = 90 
positionY = 90
while True:
    _, frame = cap.read()
    img2=cv2.rotate(frame,cv2.ROTATE_90_COUNTERCLOCKWISE)
    hsv_frame = cv2.cvtColor(img2, cv2.COLOR_BGR2HSV)
    
    low_red = np.array([20, 110, 110])
    high_red = np.array([40, 255, 255])
    red_mask = cv2.inRange(hsv_frame, low_red, high_red)
    _, contours, _ = cv2.findContours(red_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contours = sorted(contours, key=lambda x:cv2.contourArea(x), reverse=True)
    
    for cnt in contours:
        area = cv2.contourArea(cnt)
        
        if (area > 3):
            x,y,w,h = cv2.boundingRect(cnt)
        
            x_medium = int((x + x + w) / 2)
            y_medium = int((y + y + w) / 2)
            
            cv2.line(img2, (x_medium, 0), (x_medium, 480), (0, 255, 0), 2)
            cv2.line(img2, (0, y_medium), (320, y_medium), (0, 255, 0), 2)
            
        
        break
    
    
    
    cv2.imshow("Frame", img2)
    
    
    key = cv2.waitKey(1)
    
    if key == 27:
        break
    
    
    if x_medium < centerX -25:
        if positionX < 120:
            positionX += 1
    
    elif x_medium > centerX + 25:
        if positionX > 30:
            positionX -= 1
    
    if y_medium < centerY -25:
        if positionY < 120:
            positionY += 1
    elif y_medium > centerY + 25:
        if positionY > 60:
            positionY -= 1

    
    
    valx = str(positionX)
    valy = str(positionY)
    print("X"+valx+"Y"+valy)
    
    ser.write(("X"+valx+"Y"+valy).encode())
        
    
    
cap.release()
cv2.destroyAllWindows()