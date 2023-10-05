import cv2
import numpy as np
from ocr import extract_plate_no

# Read input image
img = cv2.imread("BH-SERIES-NUMBER-PLATES-FEATURED-IMAGE.jpg")

# convert input image to grayscale  
gray = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# read haarcascade for number plate detection
cascade = cv2.CascadeClassifier('haarcascade_russian_plate_number.xml')

# Detect license number plates
plates = cascade.detectMultiScale(gray, 1.2, 5)
print('Number of detected license plates:', len(plates))

# loop over all plates
for (x,y,w,h) in plates:
   
   # draw bounding rectangle around the license number plate
   cv2.rectangle(img, (x,y), (x+w, y+h), (0,255,0), 2)
   gray_plates = gray[y:y+h, x:x+w]
   color_plates = img[y:y+h, x:x+w]
   
   # save number plate detected
   cv2.imwrite('Numberplate.jpg', gray_plates)
   plate_no = extract_plate_no('Numberplate.jpg')
   print(f"Plate No is {plate_no}")
   cv2.imshow('Number Plate Image', img)
   cv2.waitKey(0)
cv2.destroyAllWindows()