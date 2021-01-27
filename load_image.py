from classes.arguments import Arguments
from classes.yolo import YOLO
from classes.image import Image
from classes.detector import Detector
from classes.monitor import Monitor

if __name__ == '__main__':

	# yolo = YOLO()
	
	# image = Image(yolo, './prueba/30.png')
	
	# detector = Detector(yolo, image)

	# print(detector.detect())

	monitor = Monitor()

	monitor.capture()