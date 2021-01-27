import numpy as np
import cv2


class Detector(object):
    def __init__(self, obj_yolo, obj_image):
        """
        initialize our lists of detected bounding boxes, confidences, and
        class IDs, respectively
        """

        self.image = obj_image.image
        self.image_H = obj_image.image_H
        self.image_W = obj_image.image_W
        self.layer_outputs = obj_image.layer_outputs
        self.boxes = []
        self.confidences = []
        self.class_ids = []
        self.idxs = None
        self.colors = obj_yolo.colors
        self.labels = obj_yolo.labels

        #self.detect()
        #self.show_results()


    def show_results(self):
        """
        Loop over the indexes we are keeping.
        Extract the bounding box coordinates.
        Draw a bounding box rectangle and label on the image.
        Show the output image
        """

        if len(self.idxs) > 0:

        	for i in self.idxs.flatten():

        		(x, y) = (self.boxes[i][0], self.boxes[i][1])
        		(w, h) = (self.boxes[i][2], self.boxes[i][3])

        		color = [int(c) for c in self.colors[self.class_ids[i]]]
        		cv2.rectangle(self.image, (x, y), (x + w, y + h), color, 2)
        		text = "{}: {:.4f}".format(self.labels[self.class_ids[i]], self.confidences[i])
        		cv2.putText(self.image, text, (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX,
        			0.5, color, 2)

        cv2.imshow("Image", self.image)
        cv2.waitKey(0)


    def detect(self):

        array_labels = []

        for output in self.layer_outputs:
            for detection in output:
                scores = detection[5:]
                classID = np.argmax(scores)
                confidence = scores[classID]

                if confidence > 0.001:
                    array_labels.append(self.labels[classID])
        
        return array_labels

        # for output in self.layer_outputs:
            
        # 	for detection in output:
        # 		scores = detection[5:]
        # 		classID = np.argmax(scores)
        # 		confidence = scores[classID]
                

        #  		if confidence > 0.05:
        # 			box = detection[0:4] * np.array([self.image_W, self.image_H, self.image_W, self.image_H])
        # 			(centerX, centerY, width, height) = box.astype("int")
        # 			x = int(centerX - (width / 2))
        # 			y = int(centerY - (height / 2))
        # 			self.boxes.append([x, y, int(width), int(height)])
        # 			self.confidences.append(float(confidence))
        # 			self.class_ids.append(classID)


        # self.idxs = cv2.dnn.NMSBoxes(self.boxes, self.confidences, 0.15,
        # 	0.1)
