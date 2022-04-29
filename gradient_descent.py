import matplotlib.pyplot as plt
import numpy as np


# Simple Cost function should look like this
# f(x) = x^2 + x + 1


def f(x):
    return x**2 + x + 1


def df(x):
    # derivative of f(x)
    return 2*x + 1


# Make data
# x_1 = np.linspace(start=-3, stop=3, num=100)
# plt.xlim([-3, 3])
# plt.ylim(0, 8)
# plt.plot(x_1, f(x_1))
# plt.show()

## plot function and Derivative side by side

x_1 = np.linspace(start=-3, stop=3, num=100)
plt.figure(figsize=[15, 5])
# Sub chart 1
plt.subplot(1, 2, 1)
plt.title('SLope of the cost function', fontsize=17)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.xlim([-3, 3])
plt.ylim(0, 8)
plt.plot(x_1, f(x_1), color='blue', linewidth=3)

# sub chart 1
plt.subplot(1, 2, 2)
plt.title('SLope of the cost function', fontsize=17)
plt.xlabel('x')
plt.ylabel('df(x)')
plt.grid()
plt.plot(x_1, df(x_1), color='skyblue', linewidth=5)

plt.show()