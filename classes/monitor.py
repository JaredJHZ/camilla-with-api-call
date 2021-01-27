from classes.arguments import Arguments
from classes.yolo import YOLO
from classes.image import Image
from classes.detector import Detector
from classes.communication import Communication

import cv2
import os

class Monitor:

    def __init__(self):
        self.title = "example"
        self.filename = ""
        self.ext = ""
        self.res = "720p"

        self.STD_DIMENSIONS =  {
            "480p": (640, 480),

            "720p": (1280, 720),

            "1080p": (1920, 1080),

            "4k": (3840, 2160),
        }

        self.VIDEO_TYPE = {
            'avi': cv2.VideoWriter_fourcc(*'XVID'),
            'mp4': cv2.VideoWriter_fourcc(*'XVID')
        }

        self.yolo = YOLO()

        self.communication = Communication("https://hcsj7t5isi.execute-api.us-west-2.amazonaws.com/test")
    
    def change_res(self, cap, width, height):
        cap.set(3, width)
        cap.set(4, height)

    def get_dims(self, cap, res='720p'):
        
        width, height = self.STD_DIMENSIONS[res]
        self.change_res(cap, width, height)
        return width, height
    
    def get_video_type(self,filename):
        self.filename, self.ext = os.path.splitext(filename)
        if self.ext in self.VIDEO_TYPE:
            return  self.VIDEO_TYPE[ext]
        return self.VIDEO_TYPE['avi']

    def capture(self):
        cap = cv2.VideoCapture(0)

        out = cv2.VideoWriter(self.filename, self.get_video_type(self.filename), 30, self.get_dims(cap, self.res ))

        count = 0

        while(True):
            ret, frame = cap.read()

            out.write(frame)

            if ret:
                count += 1
                if count % 100 == 0:
                    self.detect(frame, count)
            #cv2.imshow('frame', frame)

            if cv2.waitKey(1) & 0xFF == ord('q'): 
                break  

        cap.release()

        cv2.destroyAllWindows() 
    
    def detect(self, frame, count):
        image_with_extension = f"{count}.png"
        image_url = f"./prueba/{image_with_extension}"
        cv2.imwrite(os.path.join('./prueba', '%d.png') % count, frame)
        print(image_url)
        image = Image(self.yolo, image_url)
        detector = Detector(self.yolo, image)

        # si dentro de detector encuentro algo raro pues mando a llamar la api de aws
        array_of_labels = detector.detect()

        print(array_of_labels)

        if "cell phone" in array_of_labels:
            self.communication.post_image(image_url)