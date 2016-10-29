import cv2
import numpy as np

video = cv2.VideoCapture("videos/top_down_4" + ".m4v")

cv2.namedWindow('linesH', cv2.WINDOW_NORMAL)
while True:
    _, frame = video.read()
    if not _:
        break
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # These are calculated by hand, super iffy on if they will break or not
    color_min = np.array([30, 0, 240])
    color_max = np.array([80, 70, 255])

    mask = cv2.inRange(hsv, color_min, color_max)
    edges = cv2.Canny(mask, 50, 200, apertureSize=3)

    lines = cv2.HoughLinesP(mask, 1, np.pi / 180, 100, minLineLength=100, maxLineGap=10)

    if lines is None:
        continue
    for x1, y1, x2, y2 in lines[0]:
        cv2.line(frame, (x1, y1), (x2, y2), (0, 0, 255), 5)
        cv2.line(frame, (0, 0), (100, 100), (0, 0, 255), 5)

    cv2.imshow('linesH', frame)

    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break
cv2.destroyAllWindows()
video.release()
