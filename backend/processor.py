import cv2
import os

def generate_grayscale(input_path, output_path):
    image = cv2.imread(input_path)

    grayscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    cv2.imwrite(output_path, grayscale_image)
