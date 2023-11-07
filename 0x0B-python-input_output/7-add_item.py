#!/usr/bin/python3
"""
script that adds all arguments to a Python list, and then save them to a file
"""
import sys
import os
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


def add_item(arguments):
    """
    adds all arguments to a Python list
    """
arguments = sys.argv[1:]

try:
    existing_list = load_from_json_file("add_item.json")
except FileNotFoundError:
    existing_list = []

updated_list = existing_list + arguments

save_to_json_file(updated_list, "add_item.json")
