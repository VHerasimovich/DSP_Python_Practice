import matplotlib.pyplot as plt
import DSP_base_signals as bs
import math
import cmath


def difference_equation(input_signal, *coefficients):
    work_signal_length = len(input_signal)
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


signal_length = 64
delta_signal = bs.delta_signal_generator(signal_length, 0)
# unit_step_signal = bs.unit_step_function_generator(signal_length)
output_signal = [0 * j for j in range(signal_length)]    # initialization with zeros

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

filtered_signal = difference_equation(delta_signal, *(coefficients_b_tuple, coefficients_a_tuple))

# plt.stem(filtered_signal)
# plt.grid(True)
# plt.show()

frequency_response = [0*n for n in range(signal_length)]
magnitude_response = [0 * n for n in range(signal_length)]
omega = 0
frequency_response_length = 64
for n in range(signal_length):
    omega += cmath.pi / signal_length
    for m in range(frequency_response_length):
        frequency_response[n] += filtered_signal[m] * cmath.exp(1j*omega*m)
    magnitude_response[n] = math.sqrt(frequency_response[n].real ** 2 + frequency_response[n].imag ** 2)

plt.plot(magnitude_response)
plt.grid(True)
plt.show()
