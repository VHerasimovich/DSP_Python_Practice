import matplotlib.pyplot as plt
import numpy as nm


# Delta function generation
def delta_function_generator(signal_length=None, delta_n=0):
    assert signal_length is not None, "Signal length is not specified!"
    assert delta_n < signal_length, "Signal length is smaller than delta offset!"
    delta_function_signal = [x * 0 + (x == delta_n) for x in range(signal_length)]
    return delta_function_signal


# Unit step function generation
def unit_step_function_generator(signal_length=None, unit_step_n=0):
    assert signal_length is not None, "Signal length is not specified!"
    assert unit_step_n < signal_length, "Signal length is smaller than unit step offset!"
    unit_function_signal = [0 + (x >= unit_step_n) for x in range(signal_length)]
    return unit_function_signal


unit_function = unit_step_function_generator(signal_length=10)
plt.stem(unit_function)
plt.show()
