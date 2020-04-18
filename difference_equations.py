import matplotlib.pyplot as plt
import DSP_base_signals as bs


def difference_equation(input_signal, *coefficients):
    work_signal_length = len(input_signal)
    coefficients_b = coefficients[0]
    coefficients_a = coefficients[1]
    b_length = len(coefficients_b)
    a_length = len(coefficients_a)
    for signal_sample in range(work_signal_length):
        a_part, b_part = 0, 0
        for i in range(b_length):
            b_part += coefficients_b[i] * input_signal[signal_sample - i]
        for i in range(a_length):
            a_part += coefficients_a[i] * output_signal[signal_sample - i]
        output_signal[signal_sample] = b_part - a_part
    return output_signal


signal_length = 64
delta_signal = bs.delta_signal_generator(signal_length, 0)
# unit_step_signal = bs.unit_step_function_generator(signal_length)
output_signal = [0 * j for j in range(signal_length)]    # initialization with zeros
# all filter coefficients are in the file: first string -- b coeffs, second string -- a coeffs
filename = 'filter_coefficients'
file = open(filename, 'r')
file_data = file.read()
i = 0
coefficients_string = file_data.split('\n', 2)
coefficients_string[0] = coefficients_string[0].split(' ')
coefficients_string[1] = coefficients_string[1].split(' ')
coefficients_b_tuple = tuple([float(value) for value in coefficients_string[0]])
coefficients_a_tuple = tuple([float(value) for value in coefficients_string[1]])

filtered_signal = difference_equation(delta_signal, *(coefficients_b_tuple, coefficients_a_tuple))

plt.stem(output_signal)
plt.grid(True)
plt.show()

