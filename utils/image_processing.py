# pip install -U yolov5
import yolov5
import os
import shutil

def clean_save_path(folder_path):
    # Check if the folder exists
    if os.path.exists(folder_path):
        try:
            # Check if the folder is empty
            if not os.listdir(folder_path):
                # Remove the empty folder
                os.rmdir(folder_path)
                print("Empty folder removed successfully.")
            else:
                # Remove the folder and its contents recursively
                shutil.rmtree(folder_path)
                print("Folder and its contents removed successfully.")
        except OSError as e:
            print(f"Error: {folder_path} : {e.strerror}")
    else:
        print("Folder does not exist.")

def detect_blood_cell(img):
    # load model
    model = yolov5.load('keremberke/yolov5s-blood-cell')
  
    # set model parameters
    model.conf = 0.25  # NMS confidence threshold
    model.iou = 0.45  # NMS IoU threshold
    model.agnostic = False  # NMS class-agnostic
    model.multi_label = False  # NMS multiple labels per box
    model.max_det = 1000  # maximum number of detections per image

    # set image
    #img = 'data/image_001.jpg'

    # perform inference
    results = model(img, size=640)

    # inference with test time augmentation
    results = model(img, augment=True)

    # parse results
    predictions = results.pred[0]
    boxes = predictions[:, :4] # x1, y1, x2, y2
    scores = predictions[:, 4]
    categories = predictions[:, 5]

    # show detection bounding boxes on image
    #results.show()

    out_path = "processed_image/"
    clean_save_path(out_path)
    results.save(save_dir=out_path)