#!/usr/bin/python3

if __name__ == "__main__":
    import imp
    import sys

    file_object, module_path, description = imp.find_module('hidden_4')
    module = imp.load_module('hidden_4', file_object, module_path, description)

    names = dir(module)

    names = [name for name in names if not name.startswith('__')]

    names.sort()

    for name in names:
        print(name)
