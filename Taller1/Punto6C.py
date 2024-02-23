import cv2

img=cv2.imread('logo1.jpg')
imgbinary = cv2.Canny(img,10,50)
contornos, jerarquia =cv2.findContours(imgbinary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
print(contornos)
cv2.drawContours(img,contornos,-1,(0,255,0),3)

cv2.imshow("imagen1",img)
cv2.imshow("escala gris",imgbinary)

cv2.waitKey(0)
cv2.destroyAllWindows()
