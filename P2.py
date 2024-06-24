# Import PIL
from PIL import Image, ImageOps

# create image
im = Image.open(r"C:\Users\Kirish\Desktop\CV\ML\kirish.png")
#im1 = Image.open("dog.png")

# flip vertically
im2 = ImageOps.flip(im)

# flip horizontally
im3 = ImageOps.mirror(im)

# turn image into gray scale
im4 = ImageOps.grayscale(im)

# invert image
im5 = ImageOps.invert(im)

im2.show()
im3.show()
im4.show()
im5.show()


