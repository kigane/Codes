import matplotlib.pyplot as plt

def showimg(ax, img, title=None, cmap='viridis'):
    ax.imshow(img, cmap=cmap)
    ax.set_title(title)
    ax.set_xticks([])
    ax.set_yticks([])


def showimgs(rows, cols, imgs, titles=None, cmap='viridis'):
    _, axes = plt.subplots(rows, cols, figsize=(4*cols, 4*rows))
    axes = axes.reshape(-1)
    for ax, img, title in zip(axes, imgs, titles):
        showimg(ax, img, title, cmap)
    plt.show()
