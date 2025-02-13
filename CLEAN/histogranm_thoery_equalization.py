"""Histogram Processing in Image Processing
Histogram processing is a technique used in image processing to analyze, enhance, 
or modify the distribution of pixel intensities in an image. It is widely used for 
contrast enhancement, thresholding, and image equalization.

🔹 What is a Histogram in Image Processing?
A histogram represents the frequency distribution of pixel intensity values in an image.

X-axis: Pixel intensity values (0 to 255 for an 8-bit grayscale image).
Y-axis: Number of pixels having a specific intensity.
A histogram helps us understand an image's brightness, contrast, and exposure.

🔹 Is Histogram Processing a Spatial or Frequency Operation?
✅ Histogram processing is a SPATIAL operation.

🔹 Why?

It only modifies pixel intensities based on their distribution in the image.
It does not involve Fourier Transform or frequency domain operations.
It works directly in the spatial domain by mapping pixel intensities.


🔹 Types of Histogram-Based Processing
Histogram Equalization: Enhances contrast by redistributing intensities.
Histogram Matching (Specification): Matches an image’s histogram to a desired histogram.
Contrast Stretching: Expands the range of pixel intensities for better visibility.
Thresholding: Converts an image to binary using histogram-based intensity thresholds."""


"""Yes, you're absolutely right! A histogram in image processing represents the frequency of 
each pixel intensity level in an image. However, there is a difference between 
"frequency of pixel intensities" and "frequency domain processing" (like Fourier Transform)."""


"""🔹 Why is Histogram Processing a Spatial Operation?

Even though the histogram counts the frequency of pixel intensities, 
it still operates in the spatial domain because:

It does not involve Fourier Transform or wave-based frequency components.

In frequency domain processing (like FFT), we analyze periodic patterns, not just pixel intensity counts.
Histogram processing modifies pixel intensities directly.

It changes brightness, contrast, and distributions without transforming to a frequency space.
Histograms deal with intensity frequency, not spatial frequency.

Intensity frequency means "how many times a certain brightness value appears in the image."
Spatial frequency (used in Fourier Transform) refers to "how rapidly intensity changes across pixels."""


import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the grayscale image
img = cv2.imread("C:/Users/ARSHAN/Desktop/5th/codes/trials/s.png", cv2.IMREAD_GRAYSCALE)

# Ensure the image is loaded
if img is None:
    raise FileNotFoundError("Image not found! Check the file path.")

# Step 1: Compute Histogram
hist, bins = np.histogram(img.flatten(), bins=256, range=[0, 256])

# Step 2: Compute PDF (Probability Density Function)
pdf = hist / np.sum(hist)  # Normalize histogram to get PDF

# Step 3: Compute CDF (Cumulative Distribution Function)
cdf = np.cumsum(pdf)  # CDF is the cumulative sum of PDF
cdf_normalized = cdf * 255  # Scale to range [0,255]

# Step 4: Use CDF to equalize image
equalized_img = np.interp(img.flatten(), bins[:-1], cdf_normalized).reshape(img.shape)

# Convert to uint8 (to match OpenCV image format)
equalized_img = np.uint8(equalized_img)

# Step 5: Display Original and Equalized Histograms
fig, axes = plt.subplots(2, 2, figsize=(12, 8))

# Original Image
axes[0, 0].imshow(img, cmap='gray')
axes[0, 0].set_title("Original Image")
axes[0, 0].axis("off")

# Histogram of Original Image
axes[0, 1].hist(img.flatten(), bins=256, range=[0, 256], color='gray')
axes[0, 1].set_title("Original Histogram")

# Equalized Image
axes[1, 0].imshow(equalized_img, cmap='gray')
axes[1, 0].set_title("Equalized Image")
axes[1, 0].axis("off")

# Histogram of Equalized Image
axes[1, 1].hist(equalized_img.flatten(), bins=256, range=[0, 256], color='gray')
axes[1, 1].set_title("Equalized Histogram")

plt.tight_layout()
plt.show()
