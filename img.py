from PIL import Image, ImageDraw

k = 1
width = 255 * k
height = 255 * k
image = Image.new('RGB', (width, height))
draw = ImageDraw.Draw(image)

for i in range(width):
	for j in range(height):
		a = i
		b = j
		c = max(i, j)
		if (a > 255):
			a = 255
		if (b > 255):
			b = 255
		if (c > 255):
			c = 255
		draw.point((i,j), (a,b,c))
image.save('image.png')
