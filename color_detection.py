import cv2
import numpy as np

video = cv2.VideoCapture("videos/top_down" + ".m4v")

# cv2.namedWindow('frame', cv2.WINDOW_NORMAL)
cv2.namedWindow('mask', cv2.WINDOW_NORMAL)
# cv2.namedWindow('res', cv2.WINDOW_NORMAL)

# cv2.namedWindow('linesP', cv2.WINDOW_NORMAL)
cv2.namedWindow('linesH', cv2.WINDOW_NORMAL)
while True:
    _, frame = video.read()
    if not _:
        break
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    color_min = np.array([30, 0, 240])
    color_max = np.array([80, 70, 255])

    mask = cv2.inRange(hsv, color_min, color_max)
    # res = cv2.bitwise_and(frame, frame, mask=mask)

    # edges = cv2.Canny(mask, 50, 150, apertureSize=3)
    edges = cv2.Canny(mask, 50, 150, apertureSize=3)
    # lines = cv2.HoughLinesP(edges, 1, np.pi / 180, 100, minLineLength=500, maxLineGap=10)
    lines = cv2.HoughLines(edges, 1, np.pi / 180, 200)
    output = frame

    if lines is None:
        continue
    # print("I have " + str(len(lines)) + " lines")
    im2 = frame

    sorted_things = []
    for line in lines:
        rho, theta = line[0]
        angle = np.rad2deg(theta)
        # normalizing the angles
        if angle > 90:
            angle -= 180
            rho *= -1
        if angle < -90:
            angle += 180
            rho *= -1

        sorted_things.append((angle, rho))
    sorted_things.sort()
    # print(sorted_things)
    new_sort = []
    tmp_list = []
    # print("I only have to work on")
    while sorted_things:
        to_manipulate = sorted_things.pop(0)
        # print("working with " + str(to_manipulate))

        if not tmp_list:
            tmp_list.append(to_manipulate)
            # print("moving on")
            continue
        else:
            # print("I have something to do!")
            if np.absolute(tmp_list[-1][0] - to_manipulate[0]) < 20:
                # the angles are similar
                tmp_list.append(to_manipulate)
            else:
                # new set of lines
                # TODO: process tmp_list
                new_sort.append(tuple([sum(x) / len(x) for x in zip(*tmp_list)]))

                # exit()
                tmp_list = [to_manipulate]
    new_sort.append(tuple([sum(x) / len(x) for x in zip(*tmp_list)]))

    if len(new_sort) >= 2: print(new_sort)
    # print(sorted_things)
    # print("=========")
    # continue
    # exit()
    for item in new_sort:
        theta, rho = item
        theta = np.deg2rad(theta)
        a = np.cos(theta)
        b = np.sin(theta)
        x0 = a * rho
        y0 = b * rho
        x1 = int(x0 + 1000 * (-b))
        y1 = int(y0 + 1000 * a)
        x2 = int(x0 - 1000 * (-b))
        y2 = int(y0 - 1000 * a)
        cv2.line(im2, (x1, y1), (x2, y2), (0, 0, 255), 20)

    # cv2.imshow('frame', frame)
    cv2.imshow('mask', mask)
    # cv2.imshow('res', res)
    # cv2.imshow('linesP', output)
    cv2.imshow('linesH', im2)

    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break
cv2.destroyAllWindows()
video.release()
