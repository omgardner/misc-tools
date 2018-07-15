import os
import glob
import shutil
import re

def get_ext_dict():
    ext_paths = [os.path.abspath(path) for path in glob.iglob('./ext/**') if os.path.isfile(path)]
    ext = {}
    for path in ext_paths:
        filename = os.path.split(path)[-1]
        with open(path, 'r') as file:
            ext[filename] = file.read().splitlines()
    return ext

    
def create_directory(path):
    # ensure dir exists
    if not os.path.exists(path):
        os.mkdir(path)

        
def clean_input(s):
    result = input(s)
    # strip leading and trailing tab, space, double quotes, single quotes
    return result.strip('\t \"\'')

    
def main(src,dst):

    src_path = os.path.abspath(src)
    dst_path = os.path.abspath(dst)

    # check if source exists
    if not os.path.exists(src):
        print('Error: invalid source path')
        return
    
    # ensure destination dir exists
    create_directory(dst_path)

    # setup ext list for sorting files
    ext_dict = get_ext_dict()
    for cat in ext_dict.keys():
        create_directory(os.path.join(dst_path,cat))
    
    # create misc directory for all others
    create_directory(os.path.join(dst_path,'misc'))
    
    # setup formatting for creating glob
    src_format = '{}/**'.format(src)

    count = 1
    # copy all files over regardless of position in filetree
    for src_path in glob.iglob(src_format, recursive=True):
        # print formatting prefix
        print('[%d]' % count, end=' ')
        count += 1
        
        # move files to out_p
        src_filename = os.path.split(src_path)[-1]
        src_ext = src_filename.split('.')[-1]
        
        
        new_dst_path =  os.path.join(dst_path,'misc')
        # add subdirectory that sorts files by file type category
        for ext_category, ext_list in ext_dict.items():
            if src_ext in ext_list:
                new_dst_path = os.path.join(dst_path,ext_category)
                break
        
        # copy over to destination if it is a file
        if os.path.isfile(src_path):
            try:
                shutil.copy(src_path, os.path.join(new_dst_path, src_filename))
                print(src_filename, 'copied successfuly.')
            except FileExistsError:
                print(src_filename, ' already exists.')


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('source',help='input directory path')
    parser.add_argument('destination', help='output directory path')
    args = parser.parse_args()
    
    main(args.source, args.destination)