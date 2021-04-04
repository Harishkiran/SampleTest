import sys, os
pypath = '/home/versa/sample_learn'

def add_paths(pypath):
    for dir_name in os.listdir(pypath):
        dir_path = os.path.join(pypath, dir_name)
        if os.path.isdir(dir_path):
            sys.path.insert(0, dir_path)
            add_paths(dir_path)
add_paths(pypath)