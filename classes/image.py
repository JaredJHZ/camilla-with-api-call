import cv2
import time


class Image(object):
    def __init__(self, obj_yolo, image_url):

        self.net = obj_yolo.net
        self.image = None
        self.image_H = ""
        self.image_W = ""
        self.layer_names = []
        self.layer_outputs = None

        self.load_spatial_dimensions(image_url)
        self.load_layer_names()
        self.load_blob()


    def load_blob(self):
        """
        Construct a blob from the input image and then perform a forward.
        pass of the YOLO object detector, giving us our bounding boxes and
        associated probabilities.
        """

        blob = cv2.dnn.blobFromImage(self.image, 1 / 255.0, (416, 416),
        	swapRB=True, crop=False)
        self.net.setInput(blob)
        start = time.time()
        self.layer_outputs = self.net.forward(self.layer_names)
        end = time.time()
        print("[INFO] YOLO took {:.6f} seconds".format(end - start))


    def load_layer_names(self):
        """
        determine only the *output* layer names that we need from YOLO
        """
        ln = self.net.getLayerNames()
        self.layer_names = [ln[i[0] - 1] for i in self.net.getUnconnectedOutLayers()]


    def load_spatial_dimensions(self, image_url):
        """
        load our input image and grab its spatial dimensions
        """
        self.image = cv2.imread(image_url)
        (self.image_H, self.image_W) =  self.image.shape[:2]
