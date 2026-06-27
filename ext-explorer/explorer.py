# A small python script to list the type and number of extensions
# in a given directory.

from pathlib import Path
import sys

def main(args):
    # check the args for the path and searchable dir and default to cwd if none is given
    if len(args) == 1:
        path = Path('.').joinpath(f"{args[0]}")
    elif len(args) == 0:
        path = Path('.')
    else:
        print("Too many arguments")
        sys.exit()

    # collect the info of all the different extensions in the Dir and exit if there is an error
    ext_info = collect(path)
    if ext_info is None:
        sys.exit()

    ext_info_sorted = sorted(ext_info.items(), key=get_size, reverse=True)

    display(ext_info_sorted)

def get_size(item):
    return item[1]['size']

def collect(path):
    # new dictionary to hold {ext, # of times seen}
    ext_info = {}

    # try to get the count and size of each file extension type.
    try:
        for p in path.rglob('*'):
            if p.is_dir():
                continue
            ext = p.name
            ext_size = p.stat().st_size
            if p.suffix != '':
                ext = p.suffix
            if ext in ext_info:
                ext_info[ext]['count'] += 1
                ext_info[ext]['size'] += ext_size
            else:
                ext_info[ext] = {'count': 1, 'size': ext_size}
    except FileNotFoundError:
        print("Directory not found")
        return None
    except PermissionError:
        print("Permission denied")
        return None

    return ext_info


def display(info):
    print("extension | count | size")
    print("-------------------------")
    for i in info:
        print(f"{i[0]:9s} | {i[1]['count']:5d} | {i[1]['size']}")


if __name__ == '__main__':
    main(sys.argv[1:])