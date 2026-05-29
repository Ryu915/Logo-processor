import cv2
import os
import numpy as np

def generate_grayscale(input_path, output_path):
    image = cv2.imread(input_path)

    grayscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    cv2.imwrite(output_path, grayscale_image)

    return grayscale_image

def generate_border(grayscale_image, output_path):
    border_image = cv2.Canny(grayscale_image, 100, 200)

    cv2.imwrite(output_path, border_image)

def generate_silhouette(grayscale_image, output_path):
    _, threshold = cv2.threshold(
        grayscale_image,
        127,
        255,
        cv2.THRESH_BINARY
    )

    contours, _ = cv2.findContours(
        threshold,
        cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE
    )

    silhouette = np.zeros_like(grayscale_image)

    cv2.drawContours(
        silhouette,
        contours,
        -1,
        (255),
        thickness=cv2.FILLED
    )

    cv2.imwrite(output_path, silhouette)