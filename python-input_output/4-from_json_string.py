#!/usr/bin/python3

'''
    Docstring for python-input_output.4-from_json_string
    '''

import json


def from_json_string(my_str):
    '''
    convert from json to py

    :param my_str: python obj
    '''
    return json.loads(my_str)
