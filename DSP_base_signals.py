import matplotlib.pyplot as plt
import numpy as nm


# Delta function generation

def delta_function_generator(signal_length=None, delta_n=0):
    assert signal_length is not None, "Signal length is not specified!"
    assert delta_n < signal_length, "Signal length is smaller than delta tap!"
    delta_function_signal = [x * 0 + (x == delta_n) for x in range(signal_length)]
    return delta_function_signal


delta_function = delta_function_generator(signal_length=10)
plt.stem(delta_function)
plt.show()
