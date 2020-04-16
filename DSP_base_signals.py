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
    fading_exponent_signal = [(fading_speed ** n) * unit_step[n] for n in range(signal_length)]
    return fading_exponent_signal


def cosine_generator(signal_length=None, **kwargs):
    assert signal_length is not None, "Signal length is not specified!"
    magnitude = 1
    phase0 = 0
    frequency = math.pi
    for key in kwargs:
        if key == 'Magnitude':
            magnitude = kwargs[key]
        elif key == 'init_phase':
            phase0 = kwargs[key]
        elif key == 'frequency':
            frequency = kwargs[key]
    cos_signal = [magnitude * math.cos(frequency * n + phase0) for n in range(signal_length)]
    return cos_signal


cosine_parameters = {'Magnitude': 1,
                     'frequency': 2 * math.pi / 16}
cosine_signal = cosine_generator(signal_length=15, **cosine_parameters)
plt.stem(cosine_signal)
plt.show()
