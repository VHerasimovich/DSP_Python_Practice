import matplotlib.pyplot as plt
import DSP_base_signals as bs
import math
import cmath


def difference_equation(input_signal, *coefficients):
    work_signal_length = len(input_signal)
    output_signal = [0 * j for j in range(work_signal_length)]  # initialization with zeros
    coefficients_b = coefficients[0]
    coefficients_a = coefficients[1]
    b_length = len(coefficients_b)
    a_length = len(coefficients_a)
    for signal_sample in range(work_signal_length):
        a_part, b_part = 0, 0
        for b_i in range(b_length):
            b_part += coefficients_b[b_i] * input_signal[signal_sample - b_i]
        for a_i in range(a_length):
            a_part += coefficients_a[a_i] * output_signal[signal_sample - a_i]
        output_signal[signal_sample] = b_part - a_part
    return output_signal


def magnitude_phase_response(frequency_response_length, *coefficients):
    impulse_response = difference_equation(bs.delta_signal_generator(frequency_response_length, 0), *coefficients)
    frequency_response = [0 * n for n in range(frequency_response_length)]
    magnitude_response = [0 * n for n in range(frequency_response_length)]
    phase_response = [0 * n for n in range(frequency_response_length)]
    omega = 0   # frequency dots for response evaluation
    for n in range(frequency_response_length):
        omega += cmath.pi / frequency_response_length
        for m in range(frequency_response_length):
            frequency_response[n] += impulse_response[m] * cmath.exp(1j * omega * m)
        magnitude_response[n] = 20*math.log10(math.sqrt(frequency_response[n].real ** 2 + frequency_response[n].imag ** 2))
        phase_response[n] = math.atan2(-frequency_response[n].imag, frequency_response[n].real)
        # Matlab's unwrap func analogue: it allows to cross over [-pi +pi] atan2 limit
        if phase_response[n] - phase_response[n-1] > math.pi:
            while phase_response[n] - phase_response[n-1] > math.pi:
                phase_response[n] -= 2*math.pi
    # radians to degree conversion
    for n in range(frequency_response_length):
        phase_response[n] *= 180/math.pi

    return magnitude_response, phase_response


# all filter coefficients are in the file: first string -- b coeffs, second string -- a coeffs
filename = 'filter_coefficients'
file = None
try:
    file = open(filename, 'r')
    file_data = file.read()
    i = 0
    coefficients_string = file_data.split('\n', 2)
    coefficients_string[0] = coefficients_string[0].split(' ')
    coefficients_string[1] = coefficients_string[1].split(' ')
    coefficients_b_tuple = tuple([float(value) for value in coefficients_string[0]])
    coefficients_a_tuple = tuple([float(value) for value in coefficients_string[1]])
except FileNotFoundError:
    print("There is no coefficients file!")
    coefficients_b_tuple = (0, 0, 0)
    coefficients_a_tuple = (0, 0, 0)
finally:
    if file is not None:
        file.close()

signal_length = 64
delta_signal = bs.delta_signal_generator(signal_length, 0)
filtered_signal = difference_equation(delta_signal, *(coefficients_b_tuple, coefficients_a_tuple))

# plt.stem(filtered_signal)
# plt.grid(True)
# plt.show()

response_length = 512
(filter_magnitude_response, filter_phase_response) = \
    magnitude_phase_response(response_length, *(coefficients_b_tuple, coefficients_a_tuple))

# x axis dots of normalized frequency
x_axis = [i/response_length for i in range(response_length)]

plt.subplot(2, 1, 1)
plt.plot(x_axis, filter_magnitude_response)
plt.xlabel("Normalized frequency")
plt.ylabel("Magnitude, dB")
plt.grid(True)
plt.xlim(0, max(x_axis))

plt.subplots_adjust(hspace=0.3, top=0.95)
# hspace -- space between axes, top -- space from top to axes

plt.subplot(2, 1, 2)
plt.plot(x_axis, filter_phase_response)
plt.ylabel("Phase, degree")
plt.xlabel("Normalized frequency")
plt.grid(True)
plt.xlim(0, max(x_axis))

plt.show()
