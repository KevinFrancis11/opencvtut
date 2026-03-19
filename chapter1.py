import cv2 as cv

img = cv.imread("bird.jpg",33)

resizedImg = cv.resize(img, (700,500))


cv.imshow("Image", resizedImg)

cv.imwrite('new.jpg', resizedImg)

cv.waitKey(0)

cv.destroyAllWindows()