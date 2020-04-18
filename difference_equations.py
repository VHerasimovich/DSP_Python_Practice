import matplotlib.pyplot as plt
import DSP_base_signals as bs


def difference_equation(input_signal, *coefficients):
    signal_length = len(input_signal)
    coeffs_b = coefficients[0]
    coeffs_a = coefficients[1]
    b_length = len(coeffs_b)
    a_length = len(coeffs_a)
    for signal_sample in range(signal_length):
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
# a and b filter coefficients
coefficients_b = (0.67549, 0.05196, 1.35097)
coefficients_a = (1, 0.06797, 1.53449)

filtered_signal = difference_equation(delta_signal, *(coefficients_b, coefficients_a))

plt.stem(output_signal)
plt.grid(True)
plt.show()

