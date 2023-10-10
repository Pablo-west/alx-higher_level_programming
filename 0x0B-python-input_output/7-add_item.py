#!/usr/bin/python3
import sys
import json
from os import path

def save_to_json_file(my_obj, filename):
    with open(filename, mode='w', encoding='utf-8') as file:
        json.dump(my_obj, file)

def load_from_json_file(filename):
    if not path.exists(filename):
        return []
    with open(filename, mode='r', encoding='utf-8') as file:
        return json.load(file)

if __name__ == "__main__":
    filename = 'add_item.json'

    # Check if the file exists, and load its contents
    my_list = load_from_json_file(filename)

    # Append the command-line arguments to the list
    my_list.extend(sys.argv[1:])

    # Save the updated list back to the file
    save_to_json_file(my_list, filename)
