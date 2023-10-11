import numpy as np
import cv2
import matplotlib.pyplot as plt

# Load the image
img_colour = cv2.imread('/home/zeelb/Downloads/Bliss_(Windows_XP).png')

image_rgb = cv2.cvtColor(img_colour, cv2.COLOR_BGR2RGB)

image = cv2.imread('/home/zeelb/Downloads/Bliss_(Windows_XP).png', cv2.IMREAD_GRAYSCALE)

# Perform Fourier Transform
f_transform = np.fft.fft2(image)
f_transform_shifted = np.fft.fftshift(f_transform)

# Calculate magnitude and phase
magnitude = np.abs(f_transform_shifted)
phase = np.angle(f_transform_shifted)

fig, axs = plt.subplots(2, 2)
axs[0, 0].imshow(image_rgb)
axs[0, 0].set_title('Original Image')
axs[0, 0].axis('off')

axs[0, 1].imshow(image, cmap='gray')
axs[0, 1].set_title('Grayscale')
axs[0, 1].axis('off')

axs[1, 0].imshow(np.log1p(magnitude), cmap='gray')
axs[1, 0].set_title('Magnitude sprectrum')
axs[1, 0].axis('off')

axs[1, 1].imshow(phase, cmap='gray')
axs[1, 1].set_title('Phase Spectrum')
axs[1, 1].axis('off')
