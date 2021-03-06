import math
import matplotlib.pyplot as plt
import DSP_base_signals as bs
import Fourier_transform as dft
from random import uniform


def power_estimation(signal_under_test):
    power = sum([signal_sample**2 for signal_sample in signal_under_test])
    power /= len(signal_under_test)
    assert power > 0, "Signal power must be greater than zero."
    power_db = 10 * math.log10(power)

    return power, power_db


def periodogram(signal_under_test):
    length_info = len(signal_under_test)
    frequency_domain = dft.DFT(signal_under_test, length_info)
    signal_magnitudes = dft.magnitude(*frequency_domain)
    periodogram_array = [magnitude_element**2/length_info for magnitude_element in signal_magnitudes]

    return periodogram_array


test_signals_length = 1024
test_harmonic_1 = bs.cosine_generator(test_signals_length, **{'frequency': 2*math.pi*3/128, 'magnitude': 0.5})
test_harmonic_2 = bs.cosine_generator(test_signals_length, **{'frequency': 2*math.pi*30/128, 'magnitude': 0.5})
harmonic_part_1 = bs.cosine_generator(test_signals_length, **{'frequency': 2*math.pi*6/128, 'magnitude': 0.3})
harmonic_part_2 = bs.cosine_generator(test_signals_length, **{'frequency': 2*math.pi*10/128, 'magnitude': 0.4})
test_harmonic_3 = []
for i in range(test_signals_length):
    test_harmonic_3.append(harmonic_part_1[i]+harmonic_part_2[i])

# white noise generation
magnitude_noise = 0.5
noise = [magnitude_noise * uniform(-1, 1) for n in range(test_signals_length)]

new_cosine = bs.cosine_generator(test_signals_length, **{'frequency': 2*math.pi*9/128, 'magnitude': 0.4})

mixed_signal = []
for i in range(test_signals_length):
    mixed_signal.append(new_cosine[i] + noise[i])

harmonic_power, harmonic_power_db = power_estimation(test_harmonic_3)
signal_periodogram = periodogram(mixed_signal)
SNR = 10*math.log10(power_estimation(new_cosine)[0] / power_estimation(noise)[0])

plt.stem(signal_periodogram[1:round(len(signal_periodogram)/2)])
plt.show()

pass
