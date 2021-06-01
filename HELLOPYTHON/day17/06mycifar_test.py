import cv2

img = cv2.imread('babsae.png', cv2.IMREAD_COLOR)
img_32 = cv2.resize(img, dsize=(32, 32))

cv2.imshow('testimage_img32', img_32)
# cv2.imshow('testimage_test', test_images[0])

img_32 = img_32.reshape((1, 32, 32, 3))

print(img_32)
cv2.waitKey(0)  # 키 입력할 때까지 무한 대기, 0 이면 무한대기
cv2.destroyAllWindows()