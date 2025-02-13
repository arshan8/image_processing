import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load grayscale image
img = cv2.imread("C:/Users/ARSHAN/Desktop/5th/codes/trials/s.png", cv2.IMREAD_GRAYSCALE)
if img is None:
    raise FileNotFoundError("Image not found! Check the file path.")

# ========================== 1️⃣ Sobel Filter ==========================
# ➤ **Use Case**: Used in object detection, medical imaging (MRI edge detection).
# ➤ **Significance**: Enhances edges by giving more weight to central pixels.

sobel_x_kernel = np.array([[-1, 0, 1], 
                           [-2, 0, 2], 
                           [-1, 0, 1]])  # X-direction (Gx)

sobel_y_kernel = np.array([[-1, -2, -1], 
                           [0, 0, 0], 
                           [1, 2, 1]])  # Y-direction (Gy)

# Convolution
sobel_x = cv2.filter2D(img, -1, sobel_x_kernel)
sobel_y = cv2.filter2D(img, -1, sobel_y_kernel)

# Compute gradient magnitude
sobel_mag = cv2.magnitude(sobel_x.astype(float), sobel_y.astype(float))

"""
Mathematical Formula:
G(x, y) = sqrt(Gx² + Gy²)
- Enhances **strong edges** while ignoring weak ones.
- Uses weighted gradient calculations (center pixels matter more).
"""

# ========================== 2️⃣ Prewitt Filter ==========================
# ➤ **Use Case**: Used in industrial applications for **simple edge detection**.
# ➤ **Significance**: Computationally cheaper than Sobel but less accurate.

prewitt_x_kernel = np.array([[-1, 0, 1], 
                             [-1, 0, 1], 
                             [-1, 0, 1]])  # X-direction

prewitt_y_kernel = np.array([[-1, -1, -1], 
                             [0, 0, 0], 
                             [1, 1, 1]])  # Y-direction

# Convolution
prewitt_x = cv2.filter2D(img, -1, prewitt_x_kernel)
prewitt_y = cv2.filter2D(img, -1, prewitt_y_kernel)

# Compute magnitude
prewitt_mag = cv2.magnitude(prewitt_x.astype(float), prewitt_y.astype(float))

"""
Mathematical Formula:
G(x, y) = sqrt(Gx² + Gy²)
- Similar to Sobel but **does not emphasize center pixels** as much.
- Works well for **general edge detection** in low-compute environments.
"""

# ========================== 3️⃣ Roberts Filter ==========================
# ➤ **Use Case**: Used in **real-time edge detection**, OCR (Optical Character Recognition).
# ➤ **Significance**: Fastest filter since it uses a 2×2 kernel.

roberts_x_kernel = np.array([[1, 0], 
                             [0, -1]])  # X-direction

roberts_y_kernel = np.array([[0, 1], 
                             [-1, 0]])  # Y-direction

# Convolution
roberts_x = cv2.filter2D(img, -1, roberts_x_kernel)
roberts_y = cv2.filter2D(img, -1, roberts_y_kernel)

# Compute magnitude
roberts_mag = cv2.magnitude(roberts_x.astype(float), roberts_y.astype(float))

"""
Mathematical Formula:
G(x, y) = sqrt(Gx² + Gy²)
- **Quickest** edge detector but lacks accuracy.
- Works well for **small-scale images** (e.g., handwritten text recognition).
"""

# ========================== 4️⃣ Laplacian Filter ==========================
# ➤ **Use Case**: Used in **blob detection**, fingerprint enhancement.
# ➤ **Significance**: Detects **both edges and fine details** (but sensitive to noise).

laplacian_kernel = np.array([[0, -1, 0], 
                             [-1, 4, -1], 
                             [0, -1, 0]])  # 3×3 Laplacian Kernel

# Convolution
laplacian = cv2.filter2D(img, -1, laplacian_kernel)

"""
Mathematical Formula:
L(x, y) = d²f/dx² + d²f/dy²
- Computes **second-order derivatives**, capturing sudden intensity changes.
- Used where both **edge & texture detection** is needed.
"""

# ========================== 🔹 Display Results ==========================
titles = ['Original', 'Sobel', 'Prewitt', 'Roberts', 'Laplacian']
images = [img, sobel_mag, prewitt_mag, roberts_mag, laplacian]

plt.figure(figsize=(12, 6))
for i in range(5):
    plt.subplot(2, 3, i + 1)
    plt.imshow(images[i], cmap='gray')
    plt.title(titles[i])
    plt.axis("off")

plt.show()
