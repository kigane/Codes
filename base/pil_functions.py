from PIL import Image

image = Image.open("assets/images/009.jpg")
print(image.size)
# 如果image中包含的颜色超过了maxcolors则会返回None
colors = image.getcolors(maxcolors=image.size[0]*image.size[1])

for count, color in colors:
    if count > 150:
        print(f"Color: {color}, Count: {count}")
