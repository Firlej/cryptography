import sys
import numpy as np
from math import gcd

import itertools


def generateBBS(seed, n, loops):

	lastBits = []

	x = (seed * seed) % n

	for _ in range(loops):
		lastBits.append(x % 2)
		x = (x * x) % n

	return lastBits


def singleBitsTest(bits):
	ones = sum(bits)
	# print('Number of ones:', ones)
	# print('Number of zeros:', len(bits) - ones)
	passed = ones > 9725 and ones < 10275
	print(f"singleBitsTest passed: {passed}")


def longSeriesTest(bits):

	prev_bit = -1
	curr_series = 1
	max_series = 1
	for bit in bits:
		if bit == prev_bit:
			curr_series += 1
			max_series = max(curr_series, max_series)
		else:
			curr_series = 1
		prev_bit = bit

	# print(f"max_series: {max_series}")
	passed = max_series < 26
	print(f"longSeriesTest passed: {passed}")


def seriesTest(bits):

	series_counts = ({1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}, {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0})

	prev_bit = -1
	cnt = 1
	for bit in bits:
		if bit == prev_bit:
			cnt += 1
		elif prev_bit != -1:
			cnt = 6 if cnt > 6 else cnt
			series_counts[prev_bit][cnt] += 1
			cnt = 1
		prev_bit = bit

	cnt = 6 if cnt > 6 else cnt
	series_counts[prev_bit][cnt] += 1
	# print(series_counts)

	bounds = {1: (2315, 2685),
			  2: (1114, 1386),
			  3: (527, 723),
			  4: (240, 384),
			  5: (103, 209),
			  6: (103, 209)}

	passed = True
	for series_count in series_counts:
		for cnt, (lower, upper) in bounds.items():
			# print(cnt, lower, series_count[cnt], upper)
			if not (series_count[cnt] >= lower and series_count[cnt] < upper):
				passed = False
	
	print(f"seriesTest passed: {passed}")


def pokerTest(bits):

	# https://stackoverflow.com/questions/14931769/how-to-get-all-combination-of-n-binary-value
	counts = {key: 0 for key in list(itertools.product(range(2), repeat=4))}

	for i in range(0, len(bits), 4):
		counts[tuple(bits[i:i+4])] += 1

	# print(counts)
	
	x = 16 / 5000 * sum([val ** 2 for val in counts.values()]) - 5000

	# print(f"x: {x}")

	passed = x > 2.16 and x < 46.17

	print(f"pokerTest passed: {passed}")


def run():

	P = 2 ** 127 - 1
	Q = 2 ** 521 - 1

	n = P * Q

	SEED = 984661978996588571910503492855159913087256660449473418354928298767417477094308603012085490261513521173459

	# GENERATE

	# print('p =', P, 'mod 4 =', P % 4)
	# print('q =', Q, 'mod 4 =', Q % 4)
	# print('n =', n)
	# print('seed =', SEED)
	# print('gcd(n, seed) = ', gcd(n, SEED)) # == 1

	bits = generateBBS(SEED, n, loops=20000)

	# TESTS

	singleBitsTest(bits)
	seriesTest(bits)
	longSeriesTest(bits)
	pokerTest(bits)

if __name__ == '__main__':
	run()