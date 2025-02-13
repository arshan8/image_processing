import cv2
import numpy as np
import matplotlib.pyplot as plt

"""
🔹 SPATIAL FILTERING BASICS 🔹
Spatial filtering is a technique used in image processing where a filter (or kernel) is applied to an image to modify its appearance.
Each pixel in the output image is determined by a function of the pixels in its neighborhood from the input image.

Types of spatial filters:
1️⃣ Smoothing Filters: These are used to reduce noise and blur the image.
2️⃣ Sharpening Filters: These enhance edges and fine details in an image.
3️⃣ Combined Enhancement Methods: A combination of smoothing and sharpening to enhance quality.
"""

# Load image in grayscale
img = cv2.imread("C:/Users/ARSHAN/Desktop/5th/codes/trials/s.png", cv2.IMREAD_GRAYSCALE)


# Define function to apply filter
def apply_filter(image, kernel):
    """Applies a given kernel filter to an image."""
    return cv2.filter2D(image, -1, kernel)  # Convolve kernel with image

"""
🔹 1. SMOOTHING SPATIAL FILTERS 🔹
Smoothing filters help in reducing noise and blurring an image.
They work by averaging pixel values within a neighborhood.

📌 USE CASES:
- Removing grainy noise from images.
- Reducing details for further processing.
- Preparing images for edge detection.

🔹 **Mean Filter (Averaging)**:
This filter replaces each pixel value with the average value of its neighboring pixels. 
It helps in removing high-frequency noise but also blurs the edges slightly.

🔹 **Gaussian Filter**:
Instead of averaging equally, Gaussian filtering applies a weighted average where the center pixel has more weight.
This results in a more natural and smooth blur compared to the Mean filter.

🔹 **Median Filter**:
This is a non-linear filter that replaces each pixel with the median of its neighborhood.
It is particularly useful in removing salt-and-pepper noise while preserving edges.
"""

# Define kernels
mean_kernel = np.ones((3, 3), np.float32) / 9  # 3x3 Mean Filter (Averaging)
gaussian_kernel = cv2.getGaussianKernel(3, 1) @ cv2.getGaussianKernel(3, 1).T  # 3x3 Gaussian Filter
median_filtered = cv2.medianBlur(img, 3)  # 3x3 Median Filter (Non-Linear)

# Apply filters
mean_filtered = apply_filter(img, mean_kernel)
gaussian_filtered = apply_filter(img, gaussian_kernel)

"""
🔹 2. SHARPENING SPATIAL FILTERS 🔹
Sharpening enhances edges and details, making an image appear crisper.
It highlights regions of rapid intensity changes.

📌 USE CASES:
- Enhancing medical images (X-rays, MRI scans).
- Improving blurry photographs.
- Making text clearer in scanned documents.

🔹 **Laplacian Filter**:
A second-order derivative filter that highlights edges in an image.
It works by detecting areas of rapid intensity change and emphasizing them.

🔹 **High-Boost Filter**:
This filter sharpens an image by adding a scaled version of the original image back to a high-pass filtered image.
It enhances fine details while keeping important information intact.
"""

# Define sharpening kernels
laplacian_kernel = np.array([[0, -1, 0], [-1, 4, -1], [0, -1, 0]])  # Laplacian Filter
high_boost_kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])  # High-Boost Filter

# Apply sharpening filters
laplacian_filtered = apply_filter(img, laplacian_kernel)
high_boost_filtered = apply_filter(img, high_boost_kernel)

"""
🔹 3. COMBINING SPATIAL ENHANCEMENT METHODS 🔹
A common strategy is to first smooth the image to reduce noise, then sharpen it to restore clarity.

📌 USE CASES:
- Preprocessing images before edge detection.
- Enhancing images for better human interpretation.
- Improving satellite and astronomical images.

This method first applies a Gaussian Blur to remove unwanted noise and then sharpens the image to bring out important details.
This is particularly useful when dealing with noisy images where direct sharpening might also enhance the noise.
"""

# Step 1: Apply Gaussian Blur (Denoise)
gaussian_blurred = cv2.GaussianBlur(img, (3, 3), 1)

# Step 2: Apply High-Boost Filter (Sharpening)
sharpened_combined = apply_filter(gaussian_blurred, high_boost_kernel)

"""
🎯 SUMMARY 🎯
- **Smoothing filters** help remove noise and blur (Mean, Gaussian, Median).
- **Sharpening filters** enhance edges and restore clarity (Laplacian, High-Boost).
- **Combining both techniques** gives the best results: Denoise first, then sharpen!

This structured approach ensures image quality is improved while minimizing unwanted distortions.
"""

# Display all results using subplots
fig, axes = plt.subplots(2, 4, figsize=(15, 8))

# Original Image
axes[0, 0].imshow(img, cmap='gray')
axes[0, 0].set_title("Original Image")
axes[0, 0].axis("off")

# Smoothing Filters
axes[0, 1].imshow(mean_filtered, cmap='gray')
axes[0, 1].set_title("Mean Filter (Blur)")
axes[0, 1].axis("off")

axes[0, 2].imshow(gaussian_filtered, cmap='gray')
axes[0, 2].set_title("Gaussian Filter (Soft Blur)")
axes[0, 2].axis("off")

axes[0, 3].imshow(median_filtered, cmap='gray')
axes[0, 3].set_title("Median Filter (Noise Removal)")
axes[0, 3].axis("off")

# Sharpening Filters
axes[1, 0].imshow(laplacian_filtered, cmap='gray')
axes[1, 0].set_title("Laplacian Filter (Edge Detection)")
axes[1, 0].axis("off")

axes[1, 1].imshow(high_boost_filtered, cmap='gray')
axes[1, 1].set_title("High-Boost Filter (Sharpen)")
axes[1, 1].axis("off")

# Combined Enhancement
axes[1, 2].imshow(sharpened_combined, cmap='gray')
axes[1, 2].set_title("Combined Enhancement: Blur+Sharpen")
axes[1, 2].axis("off")

# Hide last subplot (extra slot)
axes[1, 3].axis("off")

plt.tight_layout()
plt.show()