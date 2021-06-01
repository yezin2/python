import cv2

img = cv2.imread('gong.png', cv2.IMREAD_COLOR)
cv2.imshow('testimage_img', img)  # 이미지를 화면에 보여준다.

height, width, channel = img.shape

M = cv2.getRotationMatrix2D((width/2, height/2), -10, 1)
rotated = cv2.warpAffine(img, M, (width, height))
cv2.imshow("testimage_img_Rotated by 10 Degrees", rotated)

cv2.waitKey(0)  # 키 입력할 때까지 무한 대기, 0 이면 무한대기
cv2.destroyAllWindows()