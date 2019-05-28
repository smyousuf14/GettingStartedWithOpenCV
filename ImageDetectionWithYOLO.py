#import all the required pakages
import numpy as np
import argparse
import time
import cv2
import os

#Load the coco class labels that our YOLO  model was trained on.
labelsPath = "yolo-coco/coco.names"
LABELS = open(labelsPath).read().strip().split("\n")

# Initialize a list of colors to represent each posible class label
np.random.seed(42)
COLORS = np.random.randint(0, 255, size =(len(LABELS), 3), dtype = "uint8")

#Derive the paths to the YOLO weights and model configuration.
