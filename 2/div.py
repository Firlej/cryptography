from PIL import Image, ImageDraw
import os
from random import SystemRandom

random = SystemRandom()

def split(infile):
	img = Image.open(infile)
	img = img.convert('1')

	print("Image size: {}".format(img.size))

	w, h = img.size

	img_a = Image.new('1', (w*2, h*2))
	img_b = Image.new('1', (w*2, h*2))

	draw_a = ImageDraw.Draw(img_a)
	draw_b = ImageDraw.Draw(img_b)

	options = (('1010', '0101'),('1001', '0110'))

	for x in range(w):
		for y in range(h):
			pixel = img.getpixel((x, y))
			if pixel == 0:
				combination = random.choice(options[0])
				draw_a.point((x*2, y*2), int(combination[0]))
				draw_a.point((x*2+1, y*2), int(combination[1]))
				draw_b.point((x*2, y*2), int(combination[2]))
				draw_b.point((x*2+1, y*2), int(combination[3]))
				draw_a.point((x*2, y*2+1), int(combination[0]))
				draw_a.point((x*2+1, y*2+1), int(combination[1]))
				draw_b.point((x*2, y*2+1), int(combination[2]))
				draw_b.point((x*2+1, y*2+1), int(combination[3]))
			else:
				combination = random.choice(options[1])
				draw_a.point((x*2, y*2), int(combination[0]))
				draw_a.point((x*2+1, y*2), int(combination[1]))
				draw_b.point((x*2, y*2), int(combination[2]))
				draw_b.point((x*2+1, y*2), int(combination[3]))
				draw_a.point((x*2, y*2+1), int(combination[0]))
				draw_a.point((x*2+1, y*2+1), int(combination[1]))
				draw_b.point((x*2, y*2+1), int(combination[2]))
				draw_b.point((x*2+1, y*2+1), int(combination[3]))

	# filepath, extenstion
	f, e = os.path.splitext(infile)

	out_a = f + "_a" + e
	out_b = f + "_b" + e

	img_a.save(out_a, 'PNG')
	img_b.save(out_b, 'PNG')

	print(f"Created files: {out_a} and {out_b}")

	return out_a, out_b


def merge(infile_a, infile_b, outfile):

	a = Image.open(infile_a)
	b = Image.open(infile_b)

	w, h = a.size

	out = Image.new('1', (w, h))
	draw_out = ImageDraw.Draw(out)

	for x in range(w):
		for y in range(h):
			px = a.getpixel((x, y)), b.getpixel((x, y))
			if px == (0,0):
				draw_out.point((x, y), fill=1)
			elif px == (0,1):
				draw_out.point((x, y), fill=1)
			elif px == (1,0):
				draw_out.point((x, y), fill=1)
			elif px == (1,1):
				draw_out.point((x, y), fill=0)

	out.save(outfile, 'PNG')


print()

def run():    
    
	infile = "star.png"
	outfile = "star_out.png"
	
	a, b = split(infile)

	merge(a, b, outfile)


if __name__ == "__main__":
    run()