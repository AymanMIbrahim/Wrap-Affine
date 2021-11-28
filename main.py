import cv2
import numpy as np
from math import atan
from math import degrees


def rotate_image(image, angle):
    image_center = tuple(np.array(image.shape[1::-1]) / 2)
    rot_mat = cv2.getRotationMatrix2D(image_center, angle, 1.0)
    result = cv2.warpAffine(image, rot_mat, image.shape[1::-1], flags=cv2.INTER_LINEAR)
    return result


def WrapAffine(img,pts1):
    WIDTH,HEIGHT,_ = img.shape
    pts2 = np.float32([[0,0],[WIDTH,0],[0,HEIGHT],[WIDTH,HEIGHT]])

    matrix = cv2.getPerspectiveTransform(pts1 , pts2)
    output = cv2.warpPerspective(img , matrix , (WIDTH , HEIGHT))

    return output


PolyLines = []
def click_event(event, x, y, flags, params):
    global PolyLines

    if event == cv2.EVENT_LBUTTONDOWN:

        print(x, ' ', y)
        PolyLines.append([x,y])

        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(img, str(x) + ',' +
                  str(y), (x,y), font,
                  1, (255, 0, 0), 2)
        cv2.namedWindow('Please Enter Your Corner Points', cv2.WINDOW_NORMAL)
        cv2.imshow('Please Enter Your Corner Points', img)

    # checking for right mouse clicks    
    if event==cv2.EVENT_RBUTTONDOWN:
        print(x, ' ', y)

        font = cv2.FONT_HERSHEY_SIMPLEX
        b = img[y, x, 0]
        g = img[y, x, 1]
        r = img[y, x, 2]
        cv2.putText(img, str(b) + ',' +
                  str(g) + ',' + str(r),
                  (x,y), font, 1,
                  (255, 255, 0), 2)
        cv2.namedWindow('Please Enter Your Corner Points', cv2.WINDOW_NORMAL)
        cv2.imshow('Please Enter Your Corner Points', img)


img = cv2.imread("test5.jpg")
img2 = cv2.imread("test5.jpg")
cv2.namedWindow('Please Enter Your Corner Points', cv2.WINDOW_NORMAL)
cv2.imshow('Please Enter Your Corner Points', img)
cv2.setMouseCallback('Please Enter Your Corner Points', click_event)
cv2.waitKey(0)
cv2.destroyAllWindows()

Aff = WrapAffine(img2 , np.float32(PolyLines))
cv2.namedWindow('Affined Image', cv2.WINDOW_NORMAL)
cv2.imshow('Affined Image', Aff)
cv2.waitKey(0)
cv2.destroyAllWindows()