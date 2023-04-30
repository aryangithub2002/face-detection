import cv2

#import the cascade
face_cascade=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# detecting faces from image  
#image=cv2.imread('image.jpeg')

# collect the video from webcam 
cap = cv2.VideoCapture(0)
while True:
     # read frame
    _, image = cap.read()

    #convert the image into grayscale image
    gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)


    #detect the faces
    faces=face_cascade.detectMultiScale(gray,1.1,4)

    #for drawing rectangle around the faces
    for(x,y,w,h) in faces:
        cv2.rectangle(image, (x,y), (x+w, y+h), (0,255,0), 2)

    #showing or displaying image
    cv2.imshow('image',image)
#cv2.waitKey()
    # esc for terminating loop
    k=cv2.waitKey(30) & 0xff
    if k==27:
     break

# to free capture object
cap.release()
