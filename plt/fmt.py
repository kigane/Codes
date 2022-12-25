import matplotlib.pyplot as plt
# fmt='color+style'
# color:b,g,r,c(青),m(粉),y,k(黑),w
# style:., o, v^<>(三角形), s, p, *, h, d, + x, |, -, --(虚线), :, -.
# plot(x, y, fmt)
plt.plot([x+1 for x in range(4)], [x*x for x in range(1, 5)], 'rv-')
plt.axis([0, 6, 0, 20])
plt.show()