import cv2

img = cv2.imread('gong.png')
color = cv2.cvtColor(img, cv2.COLOR_BGR2BGRA)
cv2.imwrite('gong3.png', color)

print(img)

cv2.imshow('testimage', color)
cv2.waitKey(0)  # 키 입력할 때까지 무한 대기, 0 이면 무한대기
cv2.destroyAllWindows()