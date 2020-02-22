import numpy as np
import matplotlib.pyplot as plt

# x = np.linspace(0, 2, 100)

# plt.plot(x, x, label='linear')
# plt.plot(x, x**2, label='quadratic')
# plt.plot(x, x**3, label='cubic')

# plt.xlabel('x label')
# plt.ylabel('y label')

# plt.title("Simple Plot")

# plt.legend()

# plt.show()


# x = np.arange(0, 10, 0.2)
# y = np.sin(x)
# fig, ax = plt.subplots()
# ax.plot(x, y)
# plt.show()

plt.plot([1, 2, 3, 4], [1, 4, 9, 16],'ro')
plt.axis([0, 6, 0, 20])
plt.show()