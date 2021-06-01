import cv2

img = cv2.imread('gong.png')
print(len(img))
print(len(img[0]))

img_crop= img[50:200,250:500]
cv2.imwrite('face.png', img_crop)

print(len(img_crop))
print(len(img_crop[0]))

cv2.imshow('testimage_img', img)
cv2.imshow('testimage_crop', img_crop)

cv2.waitKey(0)  # 키 입력할 때까지 무한 대기, 0 이면 무한대기
cv2.destroyAllWindows()