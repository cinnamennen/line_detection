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
    # video = cv2.VideoCapture("videos/tape_video_" + str(num) + ".m4v")
    video = cv2.VideoCapture("videos/top_down" + ".m4v")

    while 1:
        ret, frame = video.read()
        if ret:
            frame = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
            frame = cv2.medianBlur(frame, 15)

            frame = cv2.adaptiveThreshold(frame, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)

            # At this point, the image should be black/white filtered

            edges = cv2.Canny(frame, 50, 150, apertureSize=3)
            lines = cv2.HoughLinesP(edges, 1, np.pi / 180, 100, minLineLength=100, maxLineGap=10)
            output = cv2.cvtColor(frame, cv2.COLOR_GRAY2RGB)
            if lines is None:
                continue
            for line in lines:
                x1, y1, x2, y2 = line[0]
                cv2.line(output, (x1, y1), (x2, y2), (0, 255, 0), 2)
            # print("I have ", len(lines))

            # This is displaying the image
            cv2.imshow('frame', output)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
            if cv2.waitKey(1) & 0xFF == ord('d'):
                exit()

        else:
            break


# for i in range(1, 6 + 1):
#     print("Showing you ", i)
#     method_name(i)
method_name(6)
