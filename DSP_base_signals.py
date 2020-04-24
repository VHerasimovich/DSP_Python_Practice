import matplotlib.pyplot as plt
import math

# def delta_function_generator(signal_length=None, delta_n=0):
#     assert signal_length is not None, "Signal length is not specified!"
#     assert delta_n < signal_length, "Signal length is smaller than delta offset!"
#     delta_function_signal = [x * 0 + (x == delta_n) for x in range(signal_length)]
#     return delta_function_signal


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


def discrete_harmonic_signal_generator(**kwargs):
    assert len(kwargs) == 5, "Not enough parameters for signal generator!"
    for key in kwargs:
        if key == 'magnitude':
            magnitude = kwargs[key]
        elif key == 'frequency':
            frequency = kwargs[key]
        elif key == 'sampling_rate':
            sampling_rate = kwargs[key]
        elif key == 'init_phase':
            init_phase = kwargs[key]
        elif key == 'duration':
            duration = kwargs[key]

    harmonic_signal = [magnitude * math.sin(2 * math.pi * frequency * (time_n * float(1 / sampling_rate)) + init_phase)
                       for time_n in range(int(duration * sampling_rate))]
    return harmonic_signal


# harmonic_parameters = {'magnitude': 1,
#                        'frequency': 100,
#                        'sampling_rate': 8000,
#                        'init_phase': 0,
#                        'duration': 1}
# sin_signal = discrete_harmonic_signal_generator(**harmonic_parameters)
# plt.plot(sin_signal[1:80])
# plt.show()
# plt.magnitude_spectrum(sin_signal)
# plt.show()

delta_signal_generator = lambda signal_length, delta_n: [x * 0 + (x == delta_n) for x in range(signal_length)]
# plt.stem(delta_signal_generator(10, 5))
# plt.show()
