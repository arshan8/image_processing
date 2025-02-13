import numpy as np
import matplotlib.pyplot as plt
from scipy import fftpack
from scipy.ndimage import convolve

"""
Difference between Spatial Filtering, Spatial Operations, Frequency Filtering, and Frequency Operations:

1. *Spatial Filtering*:
   - Involves applying a filter (kernel) to the image directly in the spatial domain.
   - The pixel values are modified based on their neighbors using operations like convolution.
   - Example: Blurring, edge detection, and sharpening.

2. *Spatial Operations*:
   - Refers to image operations that modify the pixel values based on their position in the image.
   - These are not always convolution-based; they can include operations like thresholding, inversion, and pixel-wise addition.
   - Example: Thresholding (binary segmentation), inversion (negative effect), and scaling pixel values.

3. *Frequency Filtering*:
   - Involves transforming the image to the frequency domain (using Fourier Transform), applying filters to the frequency components, and then transforming it back to the spatial domain.
   - Filters can either enhance or suppress certain frequency components, which correspond to specific features in the image (e.g., high-frequency components are often associated with edges).
   - Example: Low-pass (blur) and high-pass (edge detection) filters.

4. *Frequency Operations*:
   - These operations involve manipulating the image in the frequency domain without necessarily applying filters. Operations can include modifying specific frequency components, removing noise, or enhancing certain details.
   - Example: Direct manipulation of frequency components, applying phase shifts, or changing the magnitude spectrum.
"""

# Function to create a sample image (a simple gradient)
def create_image():
    return np.linspace(0, 255, 256)

# Example image: Simple gradient
image = np.tile(create_image(), (256, 1))

# Spatial Filtering: Applying different types of filters (e.g., Gaussian, Edge detection, etc.)
def spatial_filtering(image, kernel):
    """ Applies a spatial filter (convolution) to the image. """
    return convolve(image, kernel)

# Example kernels for spatial filtering

# 1. Gaussian Filter (Blurring)
gaussian_kernel = np.array([[1, 4, 6, 4, 1],
                            [4, 16, 24, 16, 4],
                            [6, 24, 36, 24, 6],
                            [4, 16, 24, 16, 4],
                            [1, 4, 6, 4, 1]]) / 256

# 2. Sobel Operator for Edge Detection
sobel_kernel = np.array([[-1, -2, -1],
                         [0, 0, 0],
                         [1, 2, 1]])

# 3. Sharpening Filter
sharpen_kernel = np.array([[0, -1, 0],
                            [-1, 5, -1],
                            [0, -1, 0]])

# Frequency Domain Filtering (Low-pass and High-pass)
def frequency_filtering(image, low_pass=True):
    """ Applies frequency domain filtering (low-pass or high-pass). """
    # Step 1: Perform Fourier Transform to move to frequency domain
    F = fftpack.fft2(image)
    F_shifted = fftpack.fftshift(F)  # Shift zero-frequency component to the center
    
    # Step 2: Create a frequency filter
    rows, cols = image.shape
    crow, ccol = rows // 2, cols // 2  # Center
    mask = np.zeros((rows, cols))
    
    # Apply a low-pass or high-pass filter
    if low_pass:
        r = 30  # Radius of low-pass filter
        mask[crow - r:crow + r, ccol - r:ccol + r] = 1
    else:
        mask[:crow - 30, :ccol - 30] = 1
        mask[crow + 30:, ccol + 30:] = 1
    
    # Step 3: Apply mask to the frequency domain
    F_filtered = F_shifted * mask
    
    # Step 4: Inverse Fourier Transform to get back to image domain
    F_ishift = fftpack.ifftshift(F_filtered)
    img_back = np.abs(fftpack.ifft2(F_ishift))
    
    return img_back

# Spatial Operation (example: Thresholding)
def spatial_operation(image, operation_type):
    """ Applies a spatial operation on the image (e.g., thresholding). """
    if operation_type == 'threshold':
        return np.where(image > 128, 255, 0)
    elif operation_type == 'invert':
        return 255 - image
    else:
        return image

# Plotting the examples
fig, axs = plt.subplots(2, 3, figsize=(15, 10))

# Original Image
axs[0, 0].imshow(image, cmap='gray')
axs[0, 0].set_title('Original Image')
axs[0, 0].axis('off')

# Spatial Filtering (example with Gaussian kernel)
gaussian_filtered = spatial_filtering(image, gaussian_kernel)
axs[0, 1].imshow(gaussian_filtered, cmap='gray')
axs[0, 1].set_title('Spatial Filtering (Gaussian Blur)')
axs[0, 1].axis('off')

# Edge Detection (Sobel)
sobel_filtered = spatial_filtering(image, sobel_kernel)
axs[0, 2].imshow(sobel_filtered, cmap='gray')
axs[0, 2].set_title('Edge Detection (Sobel)')
axs[0, 2].axis('off')

# Frequency Filtering (Low-pass filter)
low_pass_image = frequency_filtering(image, low_pass=True)
axs[1, 0].imshow(low_pass_image, cmap='gray')
axs[1, 0].set_title('Frequency Filtering (Low-pass)')
axs[1, 0].axis('off')

# Frequency Filtering (High-pass filter)
high_pass_image = frequency_filtering(image, low_pass=False)
axs[1, 1].imshow(high_pass_image, cmap='gray')
axs[1, 1].set_title('Frequency Filtering (High-pass)')
axs[1, 1].axis('off')

# Spatial Operation (Thresholding)
thresholded_image = spatial_operation(image, 'threshold')
axs[1, 2].imshow(thresholded_image, cmap='gray')
axs[1, 2].set_title('Spatial Operation (Thresholding)')
axs[1, 2].axis('off')

plt.tight_layout()
plt.show()