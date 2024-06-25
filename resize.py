from PIL import Image

# Load image from disk
im = Image.open(r"C:\Users\Kirish\Desktop\CV\ML\kirish.png")

# Resize image to 100x100 with a specified resampling filter
im_resized = im.resize((100, 100), Image.Resampling.LANCZOS)

# Show resized image
im_resized.show()
