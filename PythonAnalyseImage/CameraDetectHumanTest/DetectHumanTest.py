# Dette script kommer fra geeksforgeeks.org, og jeg har brugt dette script 
# til at forstå bedre hvordan man analysere billeder via OpenCV.

import cv2, imutils

# Initializing the HOG person detector 
hog = cv2.HOGDescriptor() 
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector()) 

# Nedenstående har jeg lavet video der henviser til hvor envideo ligger på min computer.
# Der bliver så analyseret på videoen frem for webkameraet, hvis man vil analysere 
# webkamera, så skal der stå '0' i stedet for 'video'.
video = 'C:/Users/Mark/Documents/datamatiker/TrainStation.mp4'
cap = cv2.VideoCapture(video)

def detect(frame):
    bounding_box_cordinates, weights =  hog.detectMultiScale(frame, winStride = (1, 1), padding = (8, 8), scale = 2.03)
    
    person = 1
    for x,y,w,h in bounding_box_cordinates:
        cv2.rectangle(frame, (x,y), (x+w,y+h), (0,255,0), 2)
        cv2.putText(frame, f'person {person}', (x,y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,255), 1)
        person += 1
    
    cv2.putText(frame, 'Status : Detecting ', (40,40), cv2.FONT_HERSHEY_DUPLEX, 0.5, (0,129,255), 2)
    cv2.putText(frame, f'Total Persons : {person-1}', (40,70), cv2.FONT_HERSHEY_DUPLEX, 0.5, (0,129,255), 2)
    cv2.imshow('output', frame)
    return frame

while cap.isOpened(): 
    # Reading the video stream 
    ret, image = cap.read() 
    if ret: 
        image = imutils.resize(image, width=min(1200, image.shape[1]))  
        image = detect(image)  #
        # Detecting all the regions  
        # in the Image that has a  
        # pedestrians inside it 
        (regions, _) = hog.detectMultiScale(image, 
                                            winStride=(4, 4), 
                                            padding=(4, 4), 
                                            scale=1.05)    
        # Drawing the regions in the  
        # Image 
        for (x, y, w, h) in regions: 
            cv2.rectangle(image, (x, y), 
                          (x + w, y + h),  
                          (0, 0, 255), 2)    
        # Showing the output Image 
        cv2.imshow("Image", image) 
        if cv2.waitKey(25) & 0xFF == ord('q'): 
            break
    else: 
        break  
cap.release() 
cv2.destroyAllWindows() 

