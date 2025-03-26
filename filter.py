import numpy as np
import cv2

def apply_gabor_filter(image):
    g_kernel = cv2.getGaborKernel((21, 21), 8.0, np.pi/4, 10.0, 0.5, 0, ktype=cv2.CV_32F)
    filtered_img = cv2.filter2D(image, cv2.CV_8UC3, g_kernel)
    return filtered_img

filtered_iris = apply_gabor_filter(preprocessed)
cv2.imshow("Filtered Iris", filtered_iris)
cv2.waitKey(0)
cv2.destroyAllWindows()
