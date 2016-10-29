import numpy as np
import cv2

img_1 = 'pictures/drone_picture_1.JPG'
img = cv2.imread(img_1, cv2.IMREAD_COLOR)

# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


edges = cv2.Canny(img, 50, 150, apertureSize=3)


lines = cv2.HoughLinesP(edges, 1, np.pi / 180, 500, minLineLength=300, maxLineGap=1000)
for line in lines:
    x1, y1, x2, y2 = line[0]
    cv2.line(img, (x1, y1), (x2, y2), (0, 0, 255), 2)
    print("hi")

cv2.imwrite('houghlines5.jpg', img)
