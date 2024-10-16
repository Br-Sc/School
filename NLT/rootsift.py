# kps = keypoints
# descs = descriptors

import numpy
import cv2


class RootSIFT:
    def __init__(self):
        self.extractor = cv2.SIFT_create()

    def compute(self, image, kps, eps=1e-7):
        (kps, descs) = self.extractor.compute(image, kps)
        if len(kps) == 0:
            return ([], None)
        descs /= (descs.sum(axis=1, keepdims=True) + eps)
        descs = numpy.sqrt(descs)
        
        return (kps, descs)