# Load image, convert to grayscale, threshold and find contours
import cv2

img = cv2.imread('pictures/drone_picture_1.JPG', cv2.IMREAD_COLOR)
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = cv2.imread('pictures/drone_picture_1.JPG', cv2.IMREAD_GRAYSCALE)
ret, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
image, contours, hier = cv2.findContours(thresh, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
cnt = contours[0]

# then apply fitline() function
[vx, vy, x, y] = cv2.fitLine(cnt, cv2.DIST_L2, 0, 0.01, 0.01)

# Now find two extreme points on the line to draw line
lefty = int((-x * vy / vx) + y)
righty = int(((gray.shape[1] - x) * vy / vx) + y)

# Finally draw the line
cv2.line(img, (gray.shape[1] - 1, righty), (0, lefty), 0, 2)
cv2.namedWindow('image', cv2.WINDOW_NORMAL)
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
