import matplotlib.pyplot as plt

t1 = [1, 2, 3, 4]
t2 = [2, 4, 6, 8]

# plt.subplot(2,2,1, facecolor='c')
# plt.plot(t1, t2, 'ro')

# plt.subplot(2, 2, 2, facecolor='m')
# plt.plot(t2, t2, 'g*')

# plt.subplot(2, 1, 2, facecolor='y')
# plt.plot(t2, t2, 'k+')


# fig, axes = plt.subplots(2, 2, figsize=(12, 8))

# axes[0, 0].plot(t1, t2, 'bo:', drawstyle='steps-pre', label='default')
# axes[0, 0].legend(loc='best')
# props = {
#     'title': 'PLT plot',
#     'xlabel': 'Stages'
# }
# axes[0, 0].set(**props)
# axes[0, 1].plot(t2, 'ro--', drawstyle='steps-post', label='default')



fig = plt.figure(facecolor='g')
ax = fig.add_subplot(2, 2, 1)
ax.plot(t1, t2, 'bo:', drawstyle='steps-pre', label='default', markevery=(2, 1))
ax2 = fig.add_subplot(2, 2, 3)
ax2.plot(t1, t2, 'bo:', drawstyle='steps-pre', label='default')
plt.show()
