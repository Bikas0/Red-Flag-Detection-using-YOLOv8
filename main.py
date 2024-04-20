# from ultralytics import YOLO
# import cv2
# # from google.colab.patches import cv2_imshow

# # Initialize the YOLO model with the trained weights
# prediction_model = YOLO("best.pt")

# # Load a single image
# image_path = "348.jpg"
# frame = cv2.imread(image_path)

# # Perform inference using the YOLO model
# results = prediction_model(frame)

# for result in results:
#     boxes = result.boxes
#     for box in boxes:
#       conf = box.conf[0]
#       cls = box.cls[0]
#       print("Confidence :", conf)
#       print("Class :", cls)
#       print("=============")
#       print(box.xyxy)
#       x1, y1, x2, y2 = box.xyxy[0]
#       print(x1, y1, x2, y2)
#       # Do something with the bounding box coordinates
#     # Draw bounding box and label on the image
#     cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 2)
#     cv2.putText(frame, f"Class: red", (int(x1), int(y1) - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

# # Display the annotated image
# cv2.imshow("Detection", frame)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


from ultralytics import YOLO
import cv2
prediction_model = YOLO("/home/bikas/Desktop/Red-Flag-Detection-using-YOLOv8/red_flag_detection/content/runs/detect/train/weights/best.pt")

# Load a single image
image_path = "348.jpg"
frame = cv2.imread(image_path)

# Perform inference using the YOLO model
results = prediction_model(frame)

for result in results:
    boxes = result.boxes
    for box in boxes:
      conf = box.conf[0]
      cls = box.cls[0]
      x1, y1, x2, y2 = box.xyxy[0]
    cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 2)
    cv2.putText(frame, f"Red-Flag -> Conf:{conf:.2f}", (int(x1), int(y1) - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 255), 2)

# Display the annotated image
cv2.imshow("Detection", frame)
cv2.waitKey(0)
cv2.destroyAllWindows()