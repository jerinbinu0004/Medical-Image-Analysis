import cv2
import numpy as np
import matplotlib.pyplot as plt
import os

# -----------------------------
# 1. Load Image
# -----------------------------
image_path = "xray.jpg"   # Make sure image is in same folder

img = cv2.imread(image_path)

if img is None:
    print("Error: Image not found. Make sure xray.jpg is in the same folder.")
    exit()

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# -----------------------------
# 2. Histogram Equalization
# -----------------------------
hist_equalized = cv2.equalizeHist(gray)

# -----------------------------
# 3. Gaussian Smoothing
# -----------------------------
smoothed = cv2.GaussianBlur(hist_equalized, (5, 5), 0)

# -----------------------------
# 4. Sobel Edge Detection
# -----------------------------
sobel_x = cv2.Sobel(smoothed, cv2.CV_64F, 1, 0, ksize=3)
sobel_y = cv2.Sobel(smoothed, cv2.CV_64F, 0, 1, ksize=3)

sobel_magnitude = cv2.magnitude(sobel_x, sobel_y)
sobel_magnitude = cv2.convertScaleAbs(sobel_magnitude)

# -----------------------------
# 5. Thresholding (Segmentation)
# -----------------------------
_, thresholded = cv2.threshold(smoothed, 120, 255, cv2.THRESH_BINARY)

# -----------------------------
# 6. Save Outputs Automatically
# -----------------------------
if not os.path.exists("outputs"):
    os.makedirs("outputs")

cv2.imwrite("outputs/grayscale.jpg", gray)
cv2.imwrite("outputs/hist_equalized.jpg", hist_equalized)
cv2.imwrite("outputs/smoothed.jpg", smoothed)
cv2.imwrite("outputs/edges.jpg", sobel_magnitude)
cv2.imwrite("outputs/thresholded.jpg", thresholded)

print("Processing complete! Check the 'outputs' folder.")

# -----------------------------
# 7. Display Results
# -----------------------------
plt.figure(figsize=(12, 8))

plt.subplot(2, 3, 1)
plt.title("Original")
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.axis("off")

plt.subplot(2, 3, 2)
plt.title("Grayscale")
plt.imshow(gray, cmap="gray")
plt.axis("off")

plt.subplot(2, 3, 3)
plt.title("Histogram Equalized")
plt.imshow(hist_equalized, cmap="gray")
plt.axis("off")

plt.subplot(2, 3, 4)
plt.title("Smoothed")
plt.imshow(smoothed, cmap="gray")
plt.axis("off")

plt.subplot(2, 3, 5)
plt.title("Sobel Edges")
plt.imshow(sobel_magnitude, cmap="gray")
plt.axis("off")

plt.subplot(2, 3, 6)
plt.title("Thresholded")
plt.imshow(thresholded, cmap="gray")
plt.axis("off")

plt.tight_layout()
plt.show()
