import cv2
import numpy as np 
import time

## programmer : Alireza Abolqasemi

user_name = input("please enter your name : \n")

t0 = time.time()

cap = cv2.VideoCapture(0)

width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
fps = cap.get(cv2.CAP_PROP_FPS)

w = int(width/2)   ##w = width/2 ==>integer
h = int(height/2)  ## h = height/2 ==> integer


print("width=", width, "height=", height, "fps=", fps)
print(w, h)

while True :
    ret, frame = cap.read()

    if ret : 
        t1 = round((time.time() - t0), 2)
        frame = cv2.flip(frame, 1)
        
        t1_str =str(t1)
        name_and_time = user_name+ "\n" + t1_str
        
        cv2.putText(frame, name_and_time, (100, 100), cv2.FONT_HERSHEY_PLAIN,
                    5, (0, 0, 0), 5) 

        #BGR
        BGR = cv2.resize(frame , (h, w))    

        #gray
        gray0 = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray0 = cv2.resize(gray0, (h, w))
        gray0 = np.expand_dims(gray0, axis = 2) ##add a dimention to gray picture
        gray = np.concatenate((gray0, gray0), axis = 2)
        gray = np.concatenate((gray, gray0), axis = 2) ##concat gray picture 2 times
        
        

        #inv
        inv = 255 - frame
        inv = cv2.resize(inv, (h, w))

        #red
        red = BGR.copy() 
        red[:, :, 2] = 255
        red = cv2.resize(red , (h, w))

        #concat images
        img_left = np.concatenate((BGR, inv), axis = 0)
        img_right = np.concatenate((red, gray), axis = 0)
        img = np.concatenate((img_left, img_right), axis = 1)

       
        

        cv2.imshow("webcam", img)

        q = cv2.waitKey(1) 
        

        if q == ord('q') :
            break

cv2.destroyAllWindows()
cap.release()




