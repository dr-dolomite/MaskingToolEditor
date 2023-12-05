import cv2
import os
import numpy as np

def draw_brush(event, x, y, flags, param):
    global drawing
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        cv2.circle(img, (x, y), brush_size, (0, 0, 0), -1)
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing:
            cv2.circle(img, (x, y), brush_size, (0, 0, 0), -1)
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False

# Create a new folder for modified images
output_folder = 'modified_masks'
os.makedirs(output_folder, exist_ok=True)

# Load images from the folder
image_folder = 'train_masks'
image_files = sorted([f for f in os.listdir(image_folder) if f.lower().endswith(('.png', '.jpg', '.jpeg'))])

for image_file in image_files:
    img_path = os.path.join(image_folder, image_file)
    img = cv2.imread(img_path)

    # Create a window and set the callback function for mouse events
    cv2.namedWindow('Image')
    cv2.setMouseCallback('Image', draw_brush)

    drawing = False
    brush_size = 10

    while True:
        # Print the current image file name
        print(f"Current Image: {image_file}")
        
        cv2.imshow('Image', img)
        key = cv2.waitKey(1) & 0xFF

        # Press 's' to save the modified image and move to the next one
        if key == ord('s'):
            output_path = os.path.join(output_folder, image_file)
            cv2.imwrite(output_path, img)
            print(f"Image {image_file} saved successfully!")
            break

        # Press 'q' to quit
        elif key == ord('q'):
            cv2.destroyAllWindows()
            exit()

        # Press 'esc' to exit
        elif key == 27:
            cv2.destroyAllWindows()
            break

cv2.destroyAllWindows()
