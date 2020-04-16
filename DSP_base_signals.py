import matplotlib.pyplot as plt
import math


def delta_function_generator(signal_length=None, delta_n=0):
    assert signal_length is not None, "Signal length is not specified!"
    assert delta_n < signal_length, "Signal length is smaller than delta offset!"
    delta_function_signal = [x * 0 + (x == delta_n) for x in range(signal_length)]
    return delta_function_signal


def unit_step_function_generator(signal_length=None, unit_step_n=0):
    assert signal_length is not None, "Signal length is not specified!"
    assert unit_step_n < signal_length, "Signal length is smaller than unit step offset!"
    unit_function_signal = [0 + (x >= unit_step_n) for x in range(signal_length)]
    return unit_function_signal


def fading_exponent_generator(signal_length=None, fading_speed=None):
    assert signal_length is not None, "Signal length is not specified!"
    assert fading_speed is not None, "Fading parameter is not specified!"
    assert fading_speed < 1, "Fading parameter is wrong!"
    unit_step = unit_step_function_generator(signal_length)
    fading_exponent_signal = [(fading_speed ** n)*unit_step[n] for n in range(signal_length)]
    return fading_exponent_signal


fading_exponent = fading_exponent_generator(signal_length=10, fading_speed=0.7)
plt.stem(fading_exponent)
plt.show()
