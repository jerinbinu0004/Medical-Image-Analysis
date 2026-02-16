import cv2
import numpy as np
import os

def process_image(image_path):
    img = cv2.imread(image_path)

    if img is None:
        return None

    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Histogram Equalization
    hist_equalized = cv2.equalizeHist(gray)

    # Gaussian Blur
    gaussian = cv2.GaussianBlur(hist_equalized, (5, 5), 0)

    # Median Filter
    median = cv2.medianBlur(gray, 5)

    # Sobel Edge Detection
    sobel_x = cv2.Sobel(gaussian, cv2.CV_64F, 1, 0, ksize=3)
    sobel_y = cv2.Sobel(gaussian, cv2.CV_64F, 0, 1, ksize=3)
    sobel_magnitude = cv2.magnitude(sobel_x, sobel_y)
    sobel_magnitude = cv2.convertScaleAbs(sobel_magnitude)

    # Laplacian
    laplacian = cv2.Laplacian(gaussian, cv2.CV_64F)
    laplacian = cv2.convertScaleAbs(laplacian)

    # Canny
    canny = cv2.Canny(gaussian, 100, 200)

    # Threshold
    _, threshold = cv2.threshold(gaussian, 120, 255, cv2.THRESH_BINARY)

    # Adaptive Threshold
    adaptive = cv2.adaptiveThreshold(
        gaussian,
        255,
        cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        cv2.THRESH_BINARY,
        11,
        2
    )

    # Morphology
    kernel = np.ones((3, 3), np.uint8)
    erosion = cv2.erode(threshold, kernel, iterations=1)
    dilation = cv2.dilate(threshold, kernel, iterations=1)

    # Create output folder
    output_folder = os.path.join("static", "outputs")
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Save images
    cv2.imwrite(os.path.join(output_folder, "1_grayscale.jpg"), gray)
    cv2.imwrite(os.path.join(output_folder, "2_hist_equalized.jpg"), hist_equalized)
    cv2.imwrite(os.path.join(output_folder, "3_gaussian.jpg"), gaussian)
    cv2.imwrite(os.path.join(output_folder, "4_median.jpg"), median)
    cv2.imwrite(os.path.join(output_folder, "5_sobel.jpg"), sobel_magnitude)
    cv2.imwrite(os.path.join(output_folder, "6_laplacian.jpg"), laplacian)
    cv2.imwrite(os.path.join(output_folder, "7_canny.jpg"), canny)
    cv2.imwrite(os.path.join(output_folder, "8_threshold.jpg"), threshold)
    cv2.imwrite(os.path.join(output_folder, "9_adaptive.jpg"), adaptive)
    cv2.imwrite(os.path.join(output_folder, "10_erosion.jpg"), erosion)
    cv2.imwrite(os.path.join(output_folder, "11_dilation.jpg"), dilation)

    # Return filenames for HTML display
    return [
        "outputs/1_grayscale.jpg",
        "outputs/2_hist_equalized.jpg",
        "outputs/3_gaussian.jpg",
        "outputs/4_median.jpg",
        "outputs/5_sobel.jpg",
        "outputs/6_laplacian.jpg",
        "outputs/7_canny.jpg",
        "outputs/8_threshold.jpg",
        "outputs/9_adaptive.jpg",
        "outputs/10_erosion.jpg",
        "outputs/11_dilation.jpg",
    ]
