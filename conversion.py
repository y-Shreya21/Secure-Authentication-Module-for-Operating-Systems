from skimage.filters import threshold_otsu
from skimage.morphology import disk
from skimage import morphology

def preprocess_iris(image):
    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply Otsu thresholding for binarization
    thresh_val = threshold_otsu(gray)
    binary_image = gray > thresh_val

    # Remove small noise using morphological opening
    processed_image = morphology.opening(binary_image, disk(3))

    return processed_image

# Test
preprocessed = preprocess_iris(eye_region)
cv2.imshow("Preprocessed Iris", preprocessed)
cv2.waitKey(0)
cv2.destroyAllWindows()
