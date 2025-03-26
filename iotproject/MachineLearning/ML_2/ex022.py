import cv2 as cv
Original = cv.imread('test3.png', cv.IMREAD_GRAYSCALE)
Original = 255 - Original
image = cv.resize(Original, (28,28))
image = 255 - image
image = image.astype('float32')
image = image.reshape(-1, 784)  # 평탄화
image = image / 255.0   # 예측할 이미지
# cv.imshow('Original', Original)
# cv.imshow("test", image)
# cv.waitKey(0)
# cv.destroyWindow()