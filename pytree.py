#!/usr/bin/env python3

import os
import sys
import string

indent = '│   '
space = '    '

branch = '├── '
end_branch = '└── '

file_count = 0
directory_count = 0


def tree_path(path, symbol):
    global directory_count
    global file_count
    all_children = sorted([c for c in os.listdir(path) if not c.startswith('.')], key=lambda s: s.strip('_').lower())
    file_end = 0
    children_count = 0
    for children in all_children:
        if(children_count < (len(all_children) - 1)):
            print(symbol + branch + str(children))
        else:
            file_end = 1
            print(symbol + end_branch + str(children))
        if (os.path.isdir(os.path.join(path, children))):
            directory_count =  directory_count + 1
            if(file_end == 1):
                tree_path(os.path.join(path, children), symbol + space)
            else:
                tree_path(os.path.join(path, children), symbol + indent)
        elif(os.path.isfile(os.path.join(path, children))):
            file_count = file_count + 1
        children_count = children_count + 1

if __name__ == '__main__':
    dir_path = "."
    if(len(sys.argv) == 2):
        dir_path = sys.argv[1]
    print(dir_path)
    tree_path(dir_path, "")
    print()
    print(str(directory_count) + " directories, " + str(file_count) + " files")

