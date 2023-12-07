#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    # Check if the key exists before trying to delete
    if key in a_dictionary:
        del a_dictionary[key]
    return a_dictionary
