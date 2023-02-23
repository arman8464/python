#1.read the image.
import cv2
img=cv2.imread('newphoto.jpeg')
cv2.imshow('OUTPUT1',img)
cv2.waitkey(3000)
cv2.destroyALLWindows()
#2.create a duplicate image.
import cv2
img=cv2.imread('newphoto.jpg')
cv2.imwrite('ameen.png',img)
cv2.waitkey(0)
cv2.destroyALLWindows()
#3.Reading the information of the image
import cv2
img=cv2
img=cv2.imread('newphoto.jpeg')
print(img.shape)
#4.grayscale image (Black and White)
import cv2
img=cv2.imread('newphoto.jpg')
gray=cv2.cvtColor(img,cv2.color.BGR2GRAY)
cv2.imshow('ORIGINAL IMAGE',img)
cv2.imshow('GRAY SCALE IMAGE',gray)
cv2.waitkey(0)
cv2.destroyAllWindows()
 
