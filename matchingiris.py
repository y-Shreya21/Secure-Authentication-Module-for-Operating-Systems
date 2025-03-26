import numpy as np
import cv2
def encode_iris(image):
    # Resize image to fixed size
    resized = cv2.resize(image, (256, 256))

    # Convert to binary representation
    iris_template = np.where(resized > np.mean(resized), 1, 0).flatten()

    return iris_template

def match_iris(template1, template2):
    """Compare two iris templates using Hamming Distance"""
    hamming_dist = np.sum(template1 != template2) / len(template1)
    return hamming_dist < 0.3  # Acceptable threshold

# Encode stored and live iris
stored_iris_template = encode_iris(filtered_iris)
live_iris_template = encode_iris(filtered_iris)

if match_iris(stored_iris_template, live_iris_template):
    print("Iris Match - Authentication Successful!")
else:
    print("Authentication Failed")
