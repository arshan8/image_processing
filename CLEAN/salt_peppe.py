import cv2
import numpy as np
import matplotlib.pyplot as plt

def add_salt_pepper_noise(image, salt_prob=0.3, pepper_prob=0.2):
    noisy_img = np.copy(image)
    total_pixels = image.size
    
    num_salt = int(salt_prob * total_pixels)
    rows = np.random.randint(0, image.shape[0], num_salt)  # Select row indices
    cols = np.random.randint(0, image.shape[1], num_salt)  # Select column indices

    noisy_img[rows, cols] = 255  # Set salt noise pixels to white
    
    
    num_pepper = int(pepper_prob * total_pixels)
    pepper_coords = [np.random.randint(0, i, num_pepper) for i in image.shape]   #same as above , u can do either
    noisy_img[pepper_coords[0], pepper_coords[1]] = 0  
    
    return noisy_img

# def median_filter(img, kernel_size=3):
#     h, w = img.shape
#     pad = kernel_size // 2
#     filtered_img = np.zeros_like(img)
    
#     padded_img = np.pad(img, pad, mode='constant', constant_values=0)

#     for i in range(h):
#         for j in range(w):
#             region = padded_img[i:i+kernel_size, j:j+kernel_size]
#             filtered_img[i, j] = np.median(region)

#     return filtered_img

img = cv2.imread("C:/Users/ARSHAN/Desktop/5th/codes/trials/s.png", cv2.IMREAD_GRAYSCALE)
noisy_img = add_salt_pepper_noise(img)
median_filtered = cv2.medianBlur(noisy_img, 3)  
mean_filtered = cv2.blur(noisy_img, (3,3))  



fig, axes = plt.subplots(1, 4, figsize=(12, 6))  # Create 1 row, 4 columns

# Original Image
axes[0].imshow(img, cmap='gray')
axes[0].set_title("Original Image")
axes[0].axis("off")

# Salt & Pepper Noise
axes[1].imshow(noisy_img, cmap='gray')
axes[1].set_title("Salt & Pepper Noise")
axes[1].axis("off")

# Median Filtered Image
axes[2].imshow(median_filtered, cmap='gray')
axes[2].set_title("Median Filter (Preserves Edges)")
axes[2].axis("off")

# Mean Filtered Image
axes[3].imshow(mean_filtered, cmap='gray')
axes[3].set_title("Mean Filter (Smooths)")
axes[3].axis("off")

# Adjust layout and show
plt.tight_layout()
plt.show()
