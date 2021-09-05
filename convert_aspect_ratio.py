import cv2
import imutils

# Function to convert 16:9 aspect ratio image to 4:3
# Based on the result of the image width/height division 

# 16:9 ---> 1.78
# 9:16 ---> 0.56

#4:3   ---> 1.33
#3:4   ---> 0.75

def convert_aspect_ratio(image_path):
    img = cv2.imread(image_path)
    img_resize = imutils.resize(img, width=320)
    cv2.imwrite(image_path, img_resize)
    
    a = img_resize.shape[0]/img_resize.shape[1]
    
    if 1.40 <= round(a, 2) <= 1.80:
        print('16:9')
        cv2.imwrite(image_path, img_resize[71:-71])
    elif 1.0 <= round(a, 2) <= 1.39:
        print('4:3')
    elif round(a, 2) < 1.0:
        print('horizontal image!')  
    else:
        print('invalid!')
        
# Example:
convert_aspect_ratio('C:/Images/16-9_Photo.png')
    


