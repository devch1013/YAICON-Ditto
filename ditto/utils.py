import cv2
import numpy
import numpy as np

def convert_uploaded_file_to_numpy(img):
    return cv2.imdecode(np.frombuffer(img.read(), numpy.uint8), cv2.IMREAD_COLOR)