from PIL import Image, ImageEnhance

# Open the image file
image = Image.open('assets/tmp/D5_000.png')

# Create a contrast object
contrast = ImageEnhance.Contrast(image)

# Enhance the contrast of the image
contrast.enhance(1.5).show()