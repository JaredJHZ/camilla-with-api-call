import os
import numpy as np
import cv2

class YOLO(object):
    def __init__(self):

        self.labels = self.get_labels()
        self.colors = self.get_colors(self.labels)
        self.net = self.get_dnn()

    def get_labels(self):
        """
        load the COCO class labels our YOLO model was trained on
        """
        labels_path = os.path.sep.join(["yolo-dnn", "yolov3.names"])
        return open(labels_path).read().strip().split("\n")

    def get_colors(self, labels):
        """
        initialize a list of colors to represent each possible class label
        """
        np.random.seed(42)
        return np.random.randint(0, 255, size=(len(labels), 3),
        	dtype="uint8")

    def get_dnn(self):
        """
        derive the paths to the YOLO weights and model configuration.
        Load our YOLO object detector trained on COCO dataset (80 classes)
        """

        weightsPath = os.path.sep.join(["yolo-dnn", "yolov3.weights"])
        configPath = os.path.sep.join(["yolo-dnn", "yolov3.cfg"])
        print("[INFO] loading YOLO from disk...")
        return cv2.dnn.readNetFromDarknet(configPath, weightsPath)
