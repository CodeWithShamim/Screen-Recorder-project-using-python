from PIL import ImageGrab
import numpy as np
import cv2
from win32api import GetSystemMetrics
import datetime


width = GetSystemMetrics(0)
height  = GetSystemMetrics(1)
fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
time_stamp = datetime.datetime.now().strftime('%Y-%d-%m-%H-%M-%S')
name = f'{time_stamp}.mp4'
video_captured = cv2.VideoWriter(name, fourcc, 20.0, (width, height))

while True:
    img = ImageGrab.grab(bbox=(0, 0, width, height))
    img_array = np.array(img)
    img_original = cv2.cvtColor(img_array, cv2.COLOR_BGR2RGB)
    cv2.imshow("Screen Recorder..", img_original)
    video_captured.write(img_original)
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break
