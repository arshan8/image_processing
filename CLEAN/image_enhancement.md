# **Image Enhancement Techniques in Digital Image Processing**

Image Enhancement improves the **visual quality** of an image, making details more visible **without adding new information**. It is different from **image restoration**, which tries to remove distortions.

---

## **1️⃣ Spatial Domain Techniques (Directly Modify Pixels)**
These methods operate **directly on pixel intensities**.

### **📌 Intensity Transformations (Point Processing)**
    ✅ **Contrast Manipulation**  
        - **Histogram Equalization:** Spreads pixel intensities for better contrast.  
        - **Contrast Stretching:** Expands the range of pixel values.  
        - **Intensity Level Slicing:** Highlights specific intensity ranges.  
        - **Log & Power-Law (Gamma) Transformations:** Adjust brightness and contrast non-linearly.  

    ✅ **Thresholding**  
        - Converts an image to binary based on an intensity cutoff.  

        ---

### **📌 Spatial Filtering (Neighborhood Processing)**
    ✅ **Smoothing (Blurring) for Noise Reduction**  
        - **Mean Filter (Averaging)**
        - **Gaussian Blur**
        - **Median Filter** (Good for salt-and-pepper noise)

    ✅ **Sharpening (Edge Enhancement)**  
        - **Laplacian Filter**
        - **Unsharp Masking**
        - **High Boost Filtering**

    ✅ **Edge Detection**  
        - **Sobel, Prewitt, and Roberts Filters**
        - **Canny Edge Detection**

        ---

## **2️⃣ Frequency Domain Techniques (Using Fourier Transform)**
        These methods modify the **frequency components** of an image.

    ✅ **Low-Pass Filtering (Blur/Noise Reduction)**  
        - Removes high-frequency details (sharp edges).  

    ✅ **High-Pass Filtering (Sharpening)**  
        - Enhances high-frequency details (edges).  

    ✅ **Homomorphic Filtering**  
        - Enhances contrast while reducing lighting variations.

        ---

## **3️⃣ Color Image Enhancement**
    ✅ **Histogram Equalization for Color Images**  
        - Applies histogram equalization separately on each RGB channel or uses HSV.  

    ✅ **Color Correction & White Balancing**  
        - Adjusts color intensities to make images look more natural.  

    ✅ **Pseudo-color Processing**  
        - Assigns colors to grayscale images to highlight details (e.g., thermal imaging).  

        ---

        ## **Where Does Intensity Level Slicing Fit?**
        🔥 **Intensity Level Slicing** is a **spatial domain, intensity transformation technique** used for **contrast manipulation**.  

        ---

Would you like code examples for specific techniques? 🚀
