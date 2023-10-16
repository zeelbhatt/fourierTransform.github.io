# Fourier Transform of Images

The idea behind the Fourier transform of an image is to break down the image into its component frequencies. Instead of representing the image as a grid of pixel values, the Fourier transform represents the image as a sum of sinusoidal functions of different frequencies and amplitudes. These sinusoidal functions are characterized by their spatial frequency (how rapidly they oscillate across the image) and their phase (where they start in their cycle).

## The Magnitude and the Phase Plot

The magnitude plot of the Fourier Transform represents the amplitude or strength of various spatial frequency components in the image. It is also known as the amplitude spectrum. In the context of image analysis, the magnitude plot helps us understand which spatial frequencies are prevalent in the image and to what extent. High values in the magnitude plot indicate the presence of prominent features or patterns at the corresponding spatial frequencies.

```python
########## Section 4.1 MAGNITUDE-PHASE PLOTS ###################

import numpy as np

dft = np.fft.fft2(image) # Fast Fourier transform
magnitude = np.abs(dft) # Magnitude of the FFT 
phase = np.angle(dft) # Phase of the FFT

################################################################

