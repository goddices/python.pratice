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

# plt.plot([1, 2, 3, 4], [1, 4, 9, 16],'ro')
# plt.axis([0, 6, 0, 20])
# plt.show()

## evenly sampled time at 200ms intervals
#t = np.arange(0., 5., 0.2)

## red dashes, blue squares and green triangles
# plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')
# plt.show()


# names = ['group_a', 'group_b', 'group_c']
# values = [1, 10, 100]

# plt.figure(figsize=(9, 3))

# plt.subplot(131)
# plt.bar(names, values)
# plt.subplot(132)
# plt.scatter(names, values)
# plt.subplot(133)
# plt.plot(names, values)
# plt.suptitle('Categorical Plotting')
# plt.show()


# def f(t):
#     return np.exp(-t) * np.cos(2*np.pi*t)

# t1 = np.arange(0.0, 5.0, 0.1)
# t2 = np.arange(0.0, 5.0, 0.02)

# plt.figure()
# plt.subplot(211)
# plt.plot(t1, f(t1), 'bo', t2, f(t2), 'k')

# plt.subplot(212)
# plt.plot(t2, np.cos(2*np.pi*t2), 'r--')
# plt.show()
 
# plt.figure(1)                # the first figure
# plt.subplot(211)             # the first subplot in the first figure
# plt.plot([1, 2, 3])
# plt.subplot(212)             # the second subplot in the first figure
# plt.plot([4, 5, 6])


# plt.figure(2)                # a second figure
# plt.plot([4, 5, 6])          # creates a subplot(111) by default

# plt.figure(1)                # figure 1 current; subplot(212) still current
# plt.subplot(211)             # make subplot(211) in figure1 current
# plt.title('Easy as 1, 2, 3') # subplot 211 title
# plt.show()

plt.pie([0.4,0.6],labels=['aaa','bb'])
plt.show()