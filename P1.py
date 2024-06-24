from PIL import Image

# Load image from disk
im = Image.open(r"C:\Users\Kirish\Desktop\CV\ML\kirish.png")

# Show image
im.show()

# Print image format
print(im.format)
