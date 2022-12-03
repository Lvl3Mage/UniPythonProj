from PIL import Image
import random

img = Image.new('RGB', (100, 100))
data = []
for i in range(100*100):
	data.append((random.randint(1, 255),random.randint(1, 255),random.randint(1, 255)))
img.putdata(data)
img.save('image.png')
img.show()