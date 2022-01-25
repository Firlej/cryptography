import numpy as np
from PIL import Image

char_size = 3
stop_char = '#'

bin = np.binary_repr

def encode(infile, outfile, secret):

	img = Image.open(infile)
	img = img.convert('RGB')
	w, h = img.size
	pxs_raw = img.load()
	secret += stop_char
	characters_coded = 0

	for y in range(0, h):
		for x in range(0, w, char_size):

			if x + char_size >= w:
				continue

			c_raw = secret[characters_coded]
			c = bin(ord(c_raw))

			characters_coded += 1
			
			for i in range(char_size * 3 - len(c)):
				c = '0' + c

			coded_bits = 0
			for i in range(0, char_size):
				pixel = pxs_raw[x + i, y]
				color_bits = [bin(pixel[0]), bin(pixel[1]), bin(pixel[2])]

				color_bits_new = []
				for v in color_bits:
					color_bits_new.append(v[:-1] + c[coded_bits])
					coded_bits += 1
				
				pxs_raw[x + i, y] = (int(color_bits_new[0], 2), int(color_bits_new[1], 2), int(color_bits_new[2], 2))

			if c_raw == stop_char:
				img.save(outfile)
				return


def decode(filepath):

	img = Image.open(filepath)
	img = img.convert('RGB')

	w, h = img.size
	secret = ""

	pxs = img.load()

	for y in range(0, h):
		for x in range(0, w, char_size):

			if x + char_size >= w:
				continue

			bits = ''
			for i in range(char_size):
				bits += ''.join([bin(v)[-1] for v in pxs[x + i, y]])
				
			c = chr(int(bits, base=2))

			if c == stop_char:
				return secret
			
			secret += c

def run():

	secret = "xd xd xd xd xd xd xd xd xd"
	file_raw = "clock.png"
	file_encoded = "clock_encoded.png"

	print(f"Secret: {secret}")

	encode(file_raw, file_encoded, secret)

	secret_out = decode(file_encoded)

	print(f"Secret decoded: {secret_out}")


if __name__ == '__main__':
	run()
