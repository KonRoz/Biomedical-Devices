import numpy as np
from matplotlib import pyplot as plt

samp_rate = 1/1500
t = np.arange(0,2,samp_rate)
y = np.sin(6*np.pi*t) * np.sin(2*np.pi*t) * t

my_fig, subs = plt.subplots(2)
my_fig.tight_layout()

sin_plt = subs[0]
ft_plt = subs[1]

sin_plt.set_ylabel('Y(t)')
sin_plt.set_xlabel('Time (seconds)')
sin_plt.set_title('Sin(6*PI*t)*Sin(2*PI*t)*t')
sin_plt.plot(t, y)

yf = np.fft.fft(y)
xf = np.fft.fftfreq(t.size, samp_rate)
yfm = np.absolute(yf)

ft_plt.set_ylabel('Magnitude of Freq Components')
ft_plt.set_xlabel('Frequency (Hz)')
ft_plt.set_title('Fourier Transform Plot for Y(t)')
ft_plt.plot(xf, yfm)

plt.show()
