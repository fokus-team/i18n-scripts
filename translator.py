import json
import sys


param_check = lambda text: '{' not in text and '[' not in text
content = ''


def assign_entries(base):
	global content
	current_output = {}
	for key in base:
		if type(base[key]) is dict:
			current_output[key] = assign_entries(base[key])
		else:
			if param_check(base[key]):
				content_split = content.split('\n', 1)
				if len(content_split) == 2:
					content = content_split[1]
				current_output[key] = content_split[0]
			else:
				current_output[key] = base[key]
	return current_output


def gather_entries(base):
	global content
	for key in base:
		if type(base[key]) is dict:
			gather_entries(base[key])
		else:
			content += base[key].replace('\n', '/n ') + '\n' if param_check(base[key]) else ''


def gather():
	with open(sys.argv[1]) as base_file:
		base = json.load(base_file)
		gather_entries(base)
		with open(sys.argv[2], 'w+') as output_file:
			output_file.write(content)


def write():
	global content
	with open(sys.argv[1]) as base_file:
		base = json.load(base_file)
		with open(sys.argv[2], 'r') as output_file:
			content = output_file.read()
		with open(sys.argv[2], 'w+') as output_file:
			json.dump(assign_entries(base), output_file, indent='\t', ensure_ascii=False)


if len(sys.argv) < 3:
	print('Pass input and output files arguments')
	exit()
# gather()
write()
