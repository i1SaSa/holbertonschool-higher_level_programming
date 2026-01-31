#!/usr/bin/python3

class CountedIterator(iter):
    def __init__(self, data):
        self.data_iterator = iter(data)
        self.counter = 0

    def get_count(self):
        return self.count

    def __next__(self):
        try:
            item = next(self.iterator)
            self.count += 1
            return item

        except StopIteration:

            raise StopIteration

    def __iter__(self):
        return self
