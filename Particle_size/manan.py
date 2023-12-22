import torch
import cv2
import math

model = torch.hub.load(
    'ultralytics/yolov5', 'custom',
    r'C:\Users\chira\OneDrive\Desktop\ml-ai\rad_yolo_train\UGP_Project\detect-circles-in-an-image\models\1300_images.pt', force_reload=True
)
img_path = r"C:\Users\chira\AppData\Local\Temp\992761d6-e763-4b60-a5d5-7c834b97007d_data data.rar.07d\data data\new_test_data\IMG-20230406-WA0010.jpg"

img = cv2.imread(img_path)
results = model(img_path)
#results.show()


useful_results = results.xyxy[0].numpy()
for result in useful_results:
    xmin, ymin, xmax, ymax, confidence, clas = result
    x_centre = math.floor((xmin + xmax) / 2)
    y_centre = math.floor((ymin + ymax) / 2)
    radius = math.floor(min((xmax - xmin - 10)/2, (ymax - ymin - 10)/2))
    cv2.circle(img, (x_centre, y_centre), radius, (0, 255, 0), 2)

# cv2.imwrite('./test_results/' + name, img)
cv2.namedWindow('some')
cv2.imshow('some', img)
cv2.waitKey(0)

# Define the mouse callback function
def mouse_callback(event, x, y, flags, param):
    # Check if the left mouse button is clicked
    if event == cv2.EVENT_LBUTTONDOWN:
        # Loop through the useful_results array
        for result in useful_results:
            xmin, ymin, xmax, ymax, confidence, clas = result
            x_centre = math.floor((xmin + xmax) / 2)
            y_centre = math.floor((ymin + ymax) / 2)
            radius = math.floor(min((xmax - xmin - 10)/2, (ymax - ymin - 10)/2))
            # Check if the clicked point is inside the circle
            if (x - x_centre)*2 + (y - y_centre)*2 <= radius*2:
                # Print the radius of the circle
                print(f'The radius of the circle is {radius} pixels')
                # Break the loop
                break

# Bind the mouse callback function to the image window
cv2.setMouseCallback('some', mouse_callback)