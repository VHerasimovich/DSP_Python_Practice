import matplotlib.pyplot as plt
import DSP_base_signals as base_signals

x = base_signals.delta_signal_generator(64, 0)
y = [0*j for j in range(len(x))]
b = (0.3, 0.6, 0.3)
a = (1, 0, 0.9)
N = len(x)
M = len(b)
for n in range(0, N, 1):
    a_part, b_part = 0, 0
    for i in range(M):
        b_part += b[i] * x[n-i]
    for i in range(M):
        a_part += a[i] * y[n - i]
    y[n] = b_part - a_part

plt.stem(y)
plt.grid(True)
plt.show()

