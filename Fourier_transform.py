# Fourier transform estimation in trigonometric and exponential form
import math
import cmath
import matplotlib.pyplot as plt
import DSP_base_signals as bs


class ArraySizeException(Exception): pass


def DFT(input_signal, transform_length, computation_type="exponential"):
    input_signal_length = len(input_signal)
    output_signal_real = [0 * i for i in range(transform_length)]
    output_signal_imag = [0 * i for i in range(transform_length)]
    output_signal_complex = [0 * i for i in range(transform_length)]

    function_output = None

    tmp = 0
    if computation_type == "exponential":
        # exponential form
        for k in range(transform_length):
            for n in range(input_signal_length):
                tmp += input_signal[n]*cmath.exp(-1j * 2 * cmath.pi * k * n / input_signal_length)
                output_signal_complex[k] += input_signal[n] * cmath.exp(
                    -1j * 2 * cmath.pi * k * n / input_signal_length)

        function_output = output_signal_complex
    elif computation_type == "trigonometric":
        # trigonometric form
        for k in range(transform_length):
            for n in range(input_signal_length):
                output_signal_real[k] += input_signal[n] * math.cos(2 * math.pi * k * n / input_signal_length)
                output_signal_imag[k] += -(input_signal[n] * math.sin(2 * math.pi * k * n / input_signal_length))
        function_output = (output_signal_real, output_signal_imag)

    return function_output


def magnitude(*fourier_image):
    if len(fourier_image) == 2:
        real_part = fourier_image[0]
        imag_part = fourier_image[1]
    else:
        real_part = [0 * i for i in range(len(fourier_image))]
        imag_part = [0 * i for i in range(len(fourier_image))]
        for n in range(len(fourier_image)):
            real_part[n] = fourier_image[n].real
            imag_part[n] = fourier_image[n].imag

    magnitude_spectre = [0 * i for i in range(len(real_part))]
    for binN in range(len(real_part)):
        magnitude_spectre[binN] = math.sqrt(real_part[binN] ** 2 + imag_part[binN] ** 2)

    return magnitude_spectre


def runDFT():
    harmonic_parameters = {'magnitude': 1,
                           'frequency': 50,
                           'sampling_rate': 8000,
                           'init_phase': 0,
                           'duration': 0.05}
    test_signal = bs.discrete_harmonic_signal_generator(**harmonic_parameters)
    # plt.specgram(test_signal, Fs=8000, NFFT=512, noverlap=256)
    # plt.show()

    # Ctrl+P to see func args
    frequency_domain = DFT(test_signal, transform_length=len(test_signal), computation_type="exponential")

    signal_magnitudes = magnitude(*frequency_domain)

    plt.stem(signal_magnitudes)
    plt.show()

    # try:
    #     for column_number in range(len(frequency_domain[0])):
    #         if len(frequency_domain[0]) < 2:
    #             raise ArraySizeException
    #         else:
    #             for string_number in range(1):
    #                 print(str(frequency_domain[string_number][column_number]))
    #             print('\n')
    # except ArraySizeException:
    #     print("Wrong printed array size!")
    # except Exception:
    #     print("Exception instead of hand made class")
    # except LookupError:
    #     print("LookupError instead of hand made class")
    # except IndexError:
    #     print("IndexError instead of hand made class")


# runDFT()
