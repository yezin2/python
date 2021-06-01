import cv2

img = cv2.imread('gong.png')
black = cv2.cvtColor(img, cv2.COLOR_BGR2BGRA)


print(img)

cv2.imshow('testimage', black)  # 이미지를 화면에 보여준다.
cv2.waitKey(0)  # 키 입력할 때까지 무한 대기, 0 이면 무한대기
cv2.destroyAllWindows()