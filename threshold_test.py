import cv2
import numpy as np
import os

try:
    os.remove("exp.m4v")
except FileNotFoundError:
    pass


def show_image(mat):
    cv2.namedWindow('image', cv2.WINDOW_NORMAL)
    cv2.imshow('image', mat)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


video_num = 2

cv2.namedWindow('frame', cv2.WINDOW_NORMAL)
cv2.resizeWindow('frame', 1080, 1920)


def method_name(num):
    video = cv2.VideoCapture("videos/tape_video_" + str(num) + ".m4v")
    while 1:
        ret, frame = video.read()
        if ret:
            frame = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY, frame)
            frame = cv2.medianBlur(frame, 5)
            frame = cv2.adaptiveThreshold(frame, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)

            cv2.imshow('frame', frame)
            # print("I am (", video.get(cv2.CAP_PROP_FRAME_HEIGHT), ", ", video.get(cv2.CAP_PROP_FRAME_WIDTH), ")")
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
            if cv2.waitKey(1) & 0xFF == ord('d'):
                exit()

        else:
            break


for i in range(1, 6 + 1):
    print("Showing you ", i)
    method_name(i)
