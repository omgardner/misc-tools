import os
import glob
def main(target_dir):
	target_dir = os.path.abspath(target_dir)
	# find all subdirectories and file paths.
	subdir_glob_fmt = target_dir + '/**/'
	file_glob_fmt = target_dir + '/**/*.*'
	# note {less,css} gives optionals...

	for path in glob.iglob(subdir_glob_fmt):
		print('DIR\t', path)

	for path in glob.iglob(file_glob_fmt):
		print('FILE\t', path)



if __name__ == '__main__':
	import argparse
	parser = argparse.ArgumentParser()
	parser.add_argument('target_dir',help='input directory path')
	args = parser.parse_args()

	main(args.target_dir)