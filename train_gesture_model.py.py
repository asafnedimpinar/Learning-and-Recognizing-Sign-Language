import pandas as pd
import numpy as np 
import os 
from sklearn.model_selection import train_test_split 
import cv2


DATA_DIR  = "./data"

if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)

number_of_class= 3  
data_size = 100 

cap = cv2.VideoCapture(0)

for j in range(number_of_class):    
    
    if not os.path.exists(os.path.join(DATA_DIR, str(j))):
        os.makedirs(os.path.join(DATA_DIR, str(j)))

    print("data class {}", format(j)) 

    while True:
        _, frame = cap.read()  
        cv2.putText(frame, "hazır olunca q bass ", (100, 50), cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 0, 255), 3)

        cv2.imshow("frame", frame) 
        if cv2.waitKey(25) & 0xFF == ord("q"):  
            break
    
    counter = 0  

    while counter < data_size:
        
        _, frame = cap.read()
        cv2.imshow("frame", frame)  
        cv2.waitKey(25)  
        cv2.imwrite(os.path.join(DATA_DIR, str(j), "{}.jpg".format(counter)), frame)
        
        counter += 1  
        if cv2.waitKey(1) == 27:  # press esc: close
           cv2.destroyAllWindows()
           cap.release()
           break

cap.release()
cv2.destroyAllWindows()
