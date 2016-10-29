import cv2

im = cv2.imread('pictures/drone_picture_1.JPG', cv2.IMREAD_COLOR)

imgray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
# ret, thresh = cv2.threshold(imgray, 127, 255, 0)
ret, thresh = cv2.adaptiveThreshold(imgray, 127, 255, 0)


# im2, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# cnt = contours[4]
# cv2.drawContours(im, [cnt], 0, (255, 0, 0), 30)


def show_image(mat):
    cv2.namedWindow('image', cv2.WINDOW_NORMAL)
    cv2.imshow('image', mat)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


show_image(imgray)
show_image(ret)
show_image(thresh)
