from ultralytics import YOLO
import cv2

# load model
model = YOLO("yolov8n.pt")
# load video

cap = cv2.VideoCapture(r"E:\2024PHD0053\car detection\Driving on busy side roads.mp4")

if not cap.isOpened():
    print("❌ Error: Could not open video.")
    exit()


# save output 
save_output = True
if save_output:
  width  = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
  height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
  fps    = int(cap.get(cv2.CAP_PROP_FPS))
  out    = cv2.VideoWriter('tracked_output.avi',cv2.VideoWriter_fourcc(*'XVID'),fps,(width,height))

# start video loop
while cap.isOpened():
  ret,frame = cap.read()
  if not ret:
        break
  
  # Run detection and tracking
  results = model.track(source=frame, persist=True, conf=0.3)

  # Plot results
  annonted_frame = results[0].plot()

  # show the frame
  cv2.imshow("YOLO Object Tracking",annonted_frame)

  # Save if enabled
  if save_output:
    out.write(annonted_frame)

  # Press 'q' to quit
  if cv2.waitKey(1) & 0xFF == ord('q'):
    break

# clean up
cap.release()
if save_output:
  out.release()
cv2.destroyAllWindows()

