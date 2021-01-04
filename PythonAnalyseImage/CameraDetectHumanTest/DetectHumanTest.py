# Dette script kommer fra geeksforgeeks.org, og jeg har brugt dette script 
# til at fforstå bedre hvordan man analysere billeder via OpenCV.

import cv2, imutils

# Initializing the HOG person detector 
hog = cv2.HOGDescriptor() 
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector()) 

# Nedenstående har jeg lavet video der henviser til hvor envideo ligger på min computer.
# Der bliver så analyseret på videoen frem for webkameraet, hvis man vil analysere 
# webkamera, så skal der stå '0' i stedet for 'video'.
video = 'C:/Users/Mark/Documents/datamatiker/TrainStation.mp4'
cap = cv2.VideoCapture(video)

while cap.isOpened(): 
    # Reading the video stream 
    ret, image = cap.read() 
    if ret: 
        image = imutils.resize(image,  
                               width=min(400, image.shape[1]))    
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

