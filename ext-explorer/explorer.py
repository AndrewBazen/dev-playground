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

    ext_counts = collect(path)
    
    display(ext_counts)


def collect(path):
    # new dictionary to hold {ext, # of times seen}
    ext_counts = {}

    try:
        for p in path.iterdir():
            if p.is_dir():
                continue
            ext = p.name
            if p.suffix != '':
                ext = p.suffix
            if ext in ext_counts:
                ext_counts[ext] += 1
            else:
                ext_counts[ext] = 1
    except FileNotFoundError:
        print("Directory not found")
        return None
    except PermissionError:
        print("Permission denied")
        return None

    return ext_counts


def display(info):
    print("extension - count")
    print("-------------------------")
    for i in info:
        print(f"{i} - {info[i]}")


if __name__ == '__main__':
    main(sys.argv[1:])