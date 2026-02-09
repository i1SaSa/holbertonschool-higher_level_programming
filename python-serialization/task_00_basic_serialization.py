#!/usr/bin/env python3
'''
Basic Serialization
'''
import json


def serialize_and_save_to_file(data, filename):
    '''
        Ser to json

        :param data: obj to ser
        :param filename: ser saved to this file
        '''
    with open(filename, "w", encoding="utf-8") as f:
        return json.dump(data, f)


def load_and_deserialize(filename):
    '''
        DEser from json

        :param filename: DEser from this file
        '''
    with open(filename, "r") as f:
        return json.load(f)
