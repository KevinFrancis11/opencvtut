import cv2 as cv

img1 = cv.imread('bird.jpg')

img1Resize = cv.resize(img1, (600,700))

cv.imshow('binary', img1Resize)

print(type(img1))
print(img1Resize.shape)
print(img1Resize.dtype)
print(img1Resize.size)

print(img1Resize)

cv.waitKey(0)

cv.destroyAllWindows()