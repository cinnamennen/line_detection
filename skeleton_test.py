import cv2
import numpy as np

img_1 = 'pictures/drone_picture_1.JPG'
img = cv2.imread(img_1, cv2.IMREAD_GRAYSCALE)

# Output dtype = cv2.CV_8U
sobelx8u = cv2.Sobel(img, cv2.CV_8U, 1, 0, ksize=5)
# Output dtype = cv2.CV_64F. Then take its absolute and convert to cv2.CV_8U
sobelx64f = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=5)
abs_sobel64f = np.absolute(sobelx64f)
sobel_8u = np.uint8(abs_sobel64f)

laplacian = cv2.Laplacian(img, cv2.CV_64F)
sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=5)
sobely = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=5)


def show_image(mat):
    cv2.namedWindow('image', cv2.WINDOW_NORMAL)
    cv2.imshow('image', mat)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# show_image(img)
show_image(laplacian)
show_image(sobelx)
show_image(sobely)
# show_image()
