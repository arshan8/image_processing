import numpy as np
import cv2
import matplotlib.pyplot as plt


"""Intensity Level Slicing is used to enhance specific intensity ranges in an image while keeping others unchanged. It is useful in medical imaging and satellite images to highlight important features.

Two types of slicing:
1️⃣ Without Background Change: Only intensities in a given range are highlighted, while others remain unchanged.
2️⃣ With Background Change: Pixels inside a range are highlighted, while others are set to a constant value (e.g., black)."""
# Load grayscale image
img = cv2.imread("image.jpg", cv2.IMREAD_GRAYSCALE)

# Define intensity range for slicing (highlight range 100-200)
low, high = 100, 200

# 1️⃣ Intensity Level Slicing Without Background Change
sliced_img1 = np.where((img >= low) & (img <= high), 255, img)
"""Pixels in range [low, high] → Set to 255 (highlighted).
Pixels outside the range → Keep original intensity (unchanged).
💡 Use case: Highlights a range while keeping the original background."""

# 2️⃣ Intensity Level Slicing With Background Change
sliced_img2 = np.where((img >= low) & (img <= high), 255, 0)
"""Pixels in range [low, high] → Set to 255 (highlighted).
Pixels outside the range → Set to 0 (black background).
💡 Use case: Completely removes the background, making only selected pixels visible.

"""
# Visualization
fig, axes = plt.subplots(1, 3, figsize=(15, 5))
titles = ["Original Image", "Slicing (Without Background Change)", "Slicing (With Background Change)"]
images = [img, sliced_img1, sliced_img2]

for i in range(3):
    axes[i].imshow(images[i], cmap="gray")
    axes[i].set_title(titles[i])
    axes[i].axis("off")

plt.show()
