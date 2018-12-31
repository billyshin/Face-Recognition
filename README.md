# Face-Recognition

## Description:
This is a real-time face recognition program using openCV written in Python. Face is detected via webcam.

## Related Readings:
  - Paul Viola & Michael Jones, 2001
  
    <a href="http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.10.6807&rep=rep1&type=pdf">Rapid Object Detection using a Boosted Cascade of Simple Features</a>
    
    - Constantine P. Papageorgiou et al, 1998
    
    <a href="https://www.researchgate.net/publication/3766402_General_framework_for_object_detection">A General Framework for Object Detection</a>
    
    - Kinh Tieu & Paul Viola, 2000
    
    <a href="http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.136.2419&rep=rep1&type=pdf">Boosting Image Retrieval</a>
    
## Required Library:
  - openCV
  
## Algorithm overview:
  - The program takes the image in black and white (gray) and the original image (frame) as input, and that will return the same image with the detector rectangles.
  
  - Detect function:
    
        - Apply the detectMultiScale method from the face cascade to locate one or several faces in the image
        - For each detected face:
          - Paint a rectangle around the face
          - Get the region of interest in the black and white image
          - Get the region of interest in the colored image
          - Apply the detectMultiScale method to locate one or several eyes in the image
          - For each detected eyes:
              - Paint a rectangle around the eyes, but inside the referential of the face
        - Return the image with the detector rectangles
        
  - Main function:

        - Capture the last frame using webcam
        - Do some colour transformations by calling function cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        - Get the output of our detect function
        - Display the outputs
