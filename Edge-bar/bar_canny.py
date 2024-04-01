import cv2


def funtion(x):
    pass

img = cv2.imread("Edge-bar/rascacielos.jpeg") # read image
img2 = cv2.resize(img,(800,650)) # resize image for window
cv2.namedWindow("img") # name for window

#rgb color
cv2.createTrackbar("Canny Lower","img",0,255,funtion) #canny lower bar
cv2.createTrackbar("Canny Upper","img",0,255,funtion) #canny upper bar

#switch
switch = "0:OFF \n1:ON"
cv2.createTrackbar(switch,"img",0,1,funtion) #switch bar

while (1):
    k = cv2.waitKey(1) & 0xFF
    if k == 27: #ASCCI conversion (ESC)
        break
    #position bar
    l = cv2.getTrackbarPos("Canny Lower","img")
    up = cv2.getTrackbarPos("Canny Upper","img")
    s = cv2.getTrackbarPos(switch,"img")


    if s==0: #switch off
        cv2.imshow("img",img2)  

    else: #switch on
        canny_img=cv2.Canny(img2,l,up)# canny function
        cv2.imshow("img",canny_img) #canny image

cv2.destroyAllWindows()
