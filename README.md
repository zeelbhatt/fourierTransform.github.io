# Fourier Transform of Images

The idea behind the Fourier transform of an image is to break down the image into its component frequencies. Instead of representing the image as a grid of pixel values, the Fourier transform represents the image as a sum of sinusoidal functions of different frequencies and amplitudes. These sinusoidal functions are characterized by their spatial frequency (how rapidly they oscillate across the image) and their phase (where they start in their cycle).

## The Magnitude and the Phase Plot

The magnitude plot of the Fourier Transform represents the amplitude or strength of various spatial frequency components in the image. It is also known as the amplitude spectrum. In the context of image analysis, the magnitude plot helps us understand which spatial frequencies are prevalent in the image and to what extent. High values in the magnitude plot indicate the presence of prominent features or patterns at the corresponding spatial frequencies.

![image1](images/mag_freq.png)


```python
########## Section 4.1 MAGNITUDE-PHASE PLOTS ###################

import numpy as np

dft = np.fft.fft2(image) # Fast Fourier transform
magnitude = np.abs(dft) # Magnitude of the FFT 
phase = np.angle(dft) # Phase of the FFT

################################################################
```

The phase plot of the Fourier Transform represents the phase information associated with each spatial frequency component. The phase is the angle information associated with each frequency component and describes the relative positions and orientations of patterns in the image. It provides information about the position and orientation of edges, patterns, and textures in the image.

# Low-Pass, High-Pass, and Band-Pass Filters

![Lincoln in Dalivision](img/Lincon.jpg)

*Artwork Information: 'Lincoln in Dalivision' (1977)*

## Low-Pass, High-Pass & Band-Pass Filters

In this section, we'll discuss low-pass, high-pass, and band-pass filters used in image processing.

### Low-Pass Filter

A low-pass filter allows low-frequency components to pass through while attenuating or removing high-frequency components. In the context of images, low-frequency components correspond to smooth, slowly changing areas of the image, such as gradients, edges, and textures. Low-pass filtering is used for tasks like noise reduction and blurring. It can make images appear smoother and less detailed.

```python
# Define Butterworth low-pass filter function
def butterworth_low_pass(rows, cols, center_row, center_col, cutoff, n=1):
    x = np.arange(cols) - center_col
    y = np.arange(rows) - center_row
    xx, yy = np.meshgrid(x, y)
    distance = np.sqrt(xx ** 2 + yy ** 2)
    # Butterworth low-pass filter formula
    filter = 1 / (1 + (distance / cutoff) ** (2 * n))
    return filter
```

