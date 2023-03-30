import matplotlib.pyplot as plt
import matplotlib.image as mpimg

t = list(range(10, 50, 10))
plt.xlabel('xlabel')
plt.ylabel('ylabel')
plt.title('title')

img = mpimg.imread('images/pixel_beauty.png')
imgplot = plt.imshow(img)
plt.plot(t, t, 'r--') # attention: the direction of y has changed
plt.text(70, 10, 'Hello Pixel')
plt.savefig('my.png')
plt.show()