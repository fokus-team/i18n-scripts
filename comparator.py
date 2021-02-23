import json
import sys

from sty import fg, bg, ef, rs
from collections import OrderedDict


def iterate_entries(first, second, stack=[]):
	for i in range(len(first.items())):
		first_item = list(first.items())[i]
		second_item = list(second.items())[i]
		if first_item[0] == second_item[0]:
			if type(first_item[1]) is OrderedDict:
				stack.append([first_item[0], False])
				iterate_entries(first_item[1], second_item[1], stack)
				stack.pop()
		else:
			for i in range(len(stack)):
				if stack[i][1]:
					continue
				stack[i][1] = True
				print('\t' * i, fg.grey + ef.italic + stack[i][0] + rs.italic + rs.fg)
			print('\t' * len(stack), fg.red + first_item[0], "!=", second_item[0] + rs.fg)


if len(sys.argv) < 3:
	print('Pass two i18n json files as arguments')
	exit()
with open(sys.argv[1]) as first_file:
	with open(sys.argv[2]) as second_file:
		first = json.load(first_file, object_pairs_hook=OrderedDict)
		second = json.load(second_file, object_pairs_hook=OrderedDict)
		iterate_entries(first, second)
