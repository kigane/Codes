import os

from PIL import Image
from tqdm import tqdm


def webp_to_gif(webp_name, image_dir, save_dir="result"):
    if not os.path.exists(save_dir):
        os.mkdir(save_dir)

    if not os.path.exists(image_dir):
        print("目标路径不存在!")
        return

    base = "".join(webp_name.split(".")[:-1])
    im = Image.open(os.path.join(image_dir, webp_name))
    im.info.pop('background', None)
    im.save(os.path.join(save_dir, base + ".gif"), 'gif', save_all=True)


if __name__ == '__main__':
    img_dir = r"C:\Users\kigane\Downloads\孤独摇滚表情包"
    webps = os.listdir(img_dir)
    for webp_name in tqdm(webps):
        webp_to_gif(webp_name, img_dir)
