import cv2
import numpy as np
import matplotlib.pyplot as plt
"""
Each pixel in an 8-bit grayscale image is represented using 8 bits (values from 0 to 255).
 The technique helps in analyzing which bits contribute most to image clarity and which bits 
 contain noise or fine det
 
 Higher-order bits (MSB - Most Significant Bits) contain more structural information.
Lower-order bits (LSB - Least Significant Bits) contain fine details and often noise.
Extracting bit planes separately allows us to analyze and reconstruct an image with just
 a few significant bits.
 

 Consider a grayscale pixel value 235, its 8-bit binary representation is:
235 = 1 1 1 0 1 0 1 1
The leftmost bits (1 1 1 0) contribute most to the brightness.
The rightmost bits (1 0 1 1) contribute to fine details.
 """
# Load grayscale image
img = cv2.imread("C:/Users/ARSHAN/Desktop/5th/codes/trials/image.jpg", cv2.IMREAD_GRAYSCALE)

# Ensure the image is loaded
if img is None:
    raise FileNotFoundError("Image not found! Check the file path.")

### 🔹 Extract Bit-Planes
bit_planes = []  # List to store bit-plane images

# Extract 8 bit-planes one by one
for i in range(8):  
    bit_plane = (img & (1 << i)) >> i  # Mask and shift to extract the i-th bit plane
    bit_planes.append(bit_plane * 255)  # Scale up (0 → 0, 1 → 255 for visualization)
"""
        1️⃣ 1 << i (Bitwise Left Shift)

        1 << i shifts the binary 1 to the left by i positions.
        Example for different i values:

        1 << 0  →  00000001 (Extracts bit 0)
        1 << 1  →  00000010 (Extracts bit 1)
        1 << 2  →  00000100 (Extracts bit 2)
        ...
        1 << 7  →  10000000 (Extracts bit 7)

        2️⃣ img & (1 << i) (Bitwise AND Masking)
        The & (AND) operator keeps only the bit at position i and sets all other bits to 0.
        Example (for i = 2):
      
        img pixel:  11010110  (Example pixel value: 214)
        mask:       00000100  (1 << 2)
        Result:     00000100  (Only bit at position 2 is kept)

        3️⃣ >> i (Bitwise Right Shift)
        We shift the extracted bit all the way to the right, making it either 0 or 1.
        Example (continuing from i = 2):

        Before Shift:  00000100  (Bit we extracted)
        After Shift:   00000001  (Now it's either 0 or 1)

        """

fig, axes = plt.subplots(2, 4, figsize=(12, 6))

# for i in range(8):
#     ax = axes[i // 4, i % 4]  # Arrange in 2 rows, 4 columns
#     ax.imshow(bit_planes[i], cmap='gray')
#     ax.set_title(f"Bit Plane {i}")
#     ax.axis("off")
#or:


# Manually plot each bit-plane
axes[0, 0].imshow(bit_planes[0], cmap='gray')
axes[0, 0].set_title("Bit Plane 0")
axes[0, 0].axis("off")

axes[0, 1].imshow(bit_planes[1], cmap='gray')
axes[0, 1].set_title("Bit Plane 1")
axes[0, 1].axis("off")

axes[0, 2].imshow(bit_planes[2], cmap='gray')
axes[0, 2].set_title("Bit Plane 2")
axes[0, 2].axis("off")

axes[0, 3].imshow(bit_planes[3], cmap='gray')
axes[0, 3].set_title("Bit Plane 3")
axes[0, 3].axis("off")

axes[1, 0].imshow(bit_planes[4], cmap='gray')
axes[1, 0].set_title("Bit Plane 4")
axes[1, 0].axis("off")

axes[1, 1].imshow(bit_planes[5], cmap='gray')
axes[1, 1].set_title("Bit Plane 5")
axes[1, 1].axis("off")

axes[1, 2].imshow(bit_planes[6], cmap='gray')
axes[1, 2].set_title("Bit Plane 6")
axes[1, 2].axis("off")

axes[1, 3].imshow(bit_planes[7], cmap='gray')
axes[1, 3].set_title("Bit Plane 7")
axes[1, 3].axis("off")


plt.show()


