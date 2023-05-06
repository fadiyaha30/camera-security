import numpy as np
import cv2

cap = cv2.VideoCapture(0) # video capture dari camera kalau di set 0. bisa di set yang lain contoh nya di kode program (kode motion di sagemaker.py)


out = cv2.VideoWriter('output31231321312312312321.mp4', -1, 20.0, (640,480)) #cv2 VideoWriter untuk save ke nama file itu


################################fungsi loop menampilkan frame tampilan camera ke laptop###########
while(cap.isOpened()):
    ret, frame = cap.read()
    if ret==True:
        frame = cv2.flip(frame,0)

        # write the flipped frame
        out.write(frame)

        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
##################################################################################################


# Release everything if job is finished
cap.release()
out.release()
cv2.destroyAllWindows()




# Define the codec and create VideoWriter object
#fourcc = cv2.cv.CV_FOURCC(*'DIVX')
#out = cv2.VideoWriter('output.avi',fourcc, 20.0, (640,480))