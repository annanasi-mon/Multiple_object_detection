import cv2
import os

# Make photos using webcam to create a dataset, photos are made every 1 second
cam = cv2.VideoCapture(0)
num_images = 10

for img in range(num_images):

    result, image = cam.read()

    #write image
    im_path = os.path.join('raw_images', f'image_num_{img}.png')
    cv2.imwrite(im_path, image)

    # display image
    cv2.imshow('image', image)

    if cv2.waitKey(1000) == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()