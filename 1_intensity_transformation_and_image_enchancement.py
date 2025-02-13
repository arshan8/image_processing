# Explanation of Spatial Domain and Frequency Domain

# Spatial Domain:
# In the spatial domain, images are represented by pixel values in a grid format.
# Each pixel holds information about the intensity (brightness) or color value.
# Image processing techniques in the spatial domain directly manipulate these pixel values.
# Example: Operations such as blurring, sharpening, and contrast adjustments are typically done in the spatial domain.

# Frequency Domain:
# The frequency domain represents an image in terms of its frequency components.
# An image can be transformed into the frequency domain using mathematical techniques like the Fourier Transform.
# In this domain, images are represented by sinusoidal waves (frequencies) instead of pixel values.
# Each frequency component represents a pattern of change in the image, where low frequencies correspond to smooth areas (slow intensity variations),
# and high frequencies correspond to sharp edges and fine details.
# Operations in the frequency domain include filtering to emphasize or suppress certain frequency components.
# Example: High-pass filters in the frequency domain are used to enhance edges.

# Image Enhancement and Intensity Transformation:

# Intensity Transformation:
# Intensity transformation refers to altering the pixel values of an image in the spatial domain to improve visual appearance or emphasize certain features.
# Common techniques include:
# - Contrast Stretching: Expanding or compressing the range of intensity values.
# - Log Transformation: Compresses the dynamic range of an image for better visibility of darker regions.
# - Gamma Correction: Adjusting image brightness for non-linear illumination correction.
# - Negative Transformation: Inverts the pixel values (e.g., making light areas dark and dark areas light).

# Example of Intensity Transformation
import numpy as np
import matplotlib.pyplot as plt
import cv2

# Load an image in grayscale (feel free to replace with your own image)
image = cv2.imread('image.jpg', 0)  # Grayscale image

# --- Negative Transformation ---
# This inverts the pixel intensities, making dark pixels bright and vice versa.
# Formula: I_out = L - 1 - I_in, where L is the max intensity (255 for 8-bit images)
negative_transformed = 255 - image

# --- Gamma Transformation ---
# Gamma transformation adjusts brightness using a non-linear mapping function.
# Formula: I_out = c * (I_in / 255) ** gamma
# If gamma < 1 -> enhances dark regions (brightens the image)
# If gamma > 1 -> enhances bright regions (darkens the image)
gamma = 3  # Try different values like 0.5, 1, 2, 3
gamma_transformed = np.array(255 * (image / 255) ** gamma, dtype=np.uint8)

# --- Log Transformation ---
# Expands dark pixel values and compresses bright ones.
# Formula: I_out = c * log(1 + I_in)
c = 255 / np.log(1 + np.max(image))  # Normalize constant based on the maximum pixel value
log_transformed = c * np.log(1 + image)

# --- Contrast Enhancement (Contrast Stretching) ---
# Expands intensity range to improve contrast.
# Formula: I_out = (I_in - min(I)) * (255 / (max(I) - min(I)))
contrast_stretched = cv2.normalize(image, None, 0, 255, cv2.NORM_MINMAX)

# --- Contrast Enhancement using Histogram Equalization ---
# Enhances contrast by redistributing intensity levels.
equalized_image = cv2.equalizeHist(image)

# --- Thresholding ---
# Converts an image to binary form based on a threshold.
# If pixel value > threshold, set to max (255), else set to min (0)
thresh_value = 127  # Change threshold value as needed
_, thresholded_image = cv2.threshold(image, thresh_value, 255, cv2.THRESH_BINARY)

# --- Visualizing the Transformations using Matplotlib ---
plt.figure(figsize=(12, 10))

# Original Image
plt.subplot(3, 3, 1)
plt.imshow(image, cmap='gray')
plt.title('Original Image')
plt.axis('off')

# Negative Transformation
plt.subplot(3, 3, 2)
plt.imshow(negative_transformed, cmap='gray')
plt.title('Negative Transformation')
plt.axis('off')

# Gamma Transformation
plt.subplot(3, 3, 3)
plt.imshow(gamma_transformed, cmap='gray')
plt.title(f'Gamma Transformation (gamma={gamma})')
plt.axis('off')

# Log Transformation
plt.subplot(3, 3, 4)
plt.imshow(log_transformed, cmap='gray')
plt.title('Log Transformation')
plt.axis('off')

# Contrast Enhancement (Stretching)
plt.subplot(3, 3, 5)
plt.imshow(contrast_stretched, cmap='gray')
plt.title('Contrast Enhancement (Stretching)')
plt.axis('off')

# Contrast Enhancement (Histogram Equalization)
plt.subplot(3, 3, 6)
plt.imshow(equalized_image, cmap='gray')
plt.title('Histogram Equalization')
plt.axis('off')

# Thresholding
plt.subplot(3, 3, 7)
plt.imshow(thresholded_image, cmap='gray')
plt.title(f'Thresholding (T={thresh_value})')
plt.axis('off')

plt.tight_layout()
plt.show()
