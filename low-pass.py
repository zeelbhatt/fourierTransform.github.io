img = cv2.imread('/home/zeelb/Downloads/Bliss_(Windows_XP).png', cv2.IMREAD_GRAYSCALE)

f_transform = np.fft.fft2(img)
f_transform_shifted = np.fft.fftshift(f_transform)

rows, cols = img.shape
center_row, center_col = rows // 2, cols // 2

cutoff_low = 20  # Cutoff frequency for low-pass filter
cutoff_high = 100  # Cutoff frequency for high-pass filter
radius_bandpass_low = 20  # Lower cutoff frequency for bandpass filter
radius_bandpass_high = 100  # Upper cutoff frequency for bandpass filter


def butterworth_low_pass(rows, cols, center_row, center_col, cutoff, n=1):
    x = np.arange(cols) - center_col
    y = np.arange(rows) - center_row
    xx, yy = np.meshgrid(x, y)
    distance = np.sqrt(xx ** 2 + yy ** 2)

    # Butterworth low-pass filter formula
    filter = 1 / (1 + (distance / cutoff) ** (2 * n))
    return filter


def butterworth_high_pass(rows, cols, center_row, center_col, cutoff, n=1):
    return 1 - butterworth_low_pass(rows, cols, center_row, center_col, cutoff, n)


def butterworth_bandpass(rows, cols, center_row, center_col, radius_low, radius_high, n=1):
    low_pass = butterworth_low_pass(rows, cols, center_row, center_col, radius_low, n)
    high_pass = butterworth_high_pass(rows, cols, center_row, center_col, radius_high, n)
    return low_pass * high_pass


n_value = 2  
low_pass_filter = butterworth_low_pass(rows, cols, center_row, center_col, cutoff_low, n_value)
high_pass_filter = butterworth_high_pass(rows, cols, center_row, center_col, cutoff_high, n_value)
bandpass_filter = butterworth_bandpass(rows, cols, center_row, center_col, radius_bandpass_low, radius_bandpass_high,
                                       n_value)

low_pass_result = f_transform_shifted * low_pass_filter
high_pass_result = f_transform_shifted * high_pass_filter
bandpass_result = f_transform_shifted * bandpass_filter

low_pass_image = np.fft.ifftshift(low_pass_result)
low_pass_image = np.fft.ifft2(low_pass_image).real

high_pass_image = np.fft.ifftshift(high_pass_result)
high_pass_image = np.fft.ifft2(high_pass_image).real

bandpass_image = np.fft.ifftshift(bandpass_result)
bandpass_image = np.fft.ifft2(bandpass_image).real

fourier_transform = np.fft.fft2(img)
fourier_transform_shifted = np.fft.fftshift(fourier_transform)  

magnitude0 = np.abs(fourier_transform_shifted)
phase = np.angle(fourier_transform_shifted)

fourier_transform = np.fft.fft2(low_pass_image)
fourier_transform_shifted = np.fft.fftshift(fourier_transform)  

magnitude1 = np.abs(fourier_transform_shifted)
phase = np.angle(fourier_transform_shifted)

fourier_transform = np.fft.fft2(high_pass_image)
fourier_transform_shifted = np.fft.fftshift(fourier_transform) 

magnitude2 = np.abs(fourier_transform_shifted)
phase = np.angle(fourier_transform_shifted)

fourier_transform = np.fft.fft2(bandpass_image)
fourier_transform_shifted = np.fft.fftshift(fourier_transform)  

# Calculate magnitude and phase
magnitude3 = np.abs(fourier_transform_shifted)
phase = np.angle(fourier_transform_shifted)


plt.figure(figsize=(12, 8))

plt.subplot(1, 4, 1)
plt.imshow(img, cmap='gray')
plt.title('Original Image')
plt.axis('off')

plt.subplot(1, 4, 2)
plt.imshow(low_pass_image, cmap='gray')
plt.title('Low-Pass Filtered Image')
plt.axis('off')

plt.subplot(1, 4, 3)
plt.imshow(high_pass_image, cmap='gray')
plt.title('High-Pass Filtered Image')
plt.axis('off')

plt.subplot(1, 4, 4)
plt.imshow(bandpass_image, cmap='gray')
plt.title('Bandpass Filtered Image')
plt.axis('off')

plt.tight_layout()
plt.savefig('/home/zeelb/Downloads/fliters.png')
