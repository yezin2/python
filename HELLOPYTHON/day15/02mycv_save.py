import cv2

img = cv2.imread('gong.png', cv2.IMREAD_GRAYSCALE)
cv2.imwrite('gongla.png', img)

print(img.shape)
print(img)
 
cv2.imshow('Test Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()