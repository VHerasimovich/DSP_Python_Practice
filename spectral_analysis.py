import math
import matplotlib.pyplot as plt
import DSP_base_signals as bs


def power_estimation(signal_under_test):
    power = 0
    for i in range(len(signal_under_test)):
        power += signal_under_test[i]**2
    power /= len(signal_under_test)
    assert power > 0, "Signal power must be greater than zero."
    power_db = 10 * math.log10(power)

    return power, power_db


test_signals_length = 1024
test_harmonic_1 = bs.cosine_generator(test_signals_length, **{'frequency': 2*math.pi*3/128, 'magnitude': 0.5})
test_harmonic_2 = bs.cosine_generator(test_signals_length, **{'frequency': 2*math.pi*30/128, 'magnitude': 0.5})
harmonic_part_1 = bs.cosine_generator(test_signals_length, **{'frequency': 2*math.pi*6/128, 'magnitude': 0.3})
harmonic_part_2 = bs.cosine_generator(test_signals_length, **{'frequency': 2*math.pi*10/128, 'magnitude': 0.4})
test_harmonic_3 = []
for i in range(test_signals_length):
    test_harmonic_3.append(harmonic_part_1[i]+harmonic_part_2[i])

harmonic_power, harmonic_power_db = power_estimation(test_harmonic_3)

plt.plot(test_harmonic_3)
plt.show()

pass
