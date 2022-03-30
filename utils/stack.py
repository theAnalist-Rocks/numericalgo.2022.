import os
import time
import numpy as np


class Stack:
    def __init__(self):
        self.items = []
        self.params = {}

    def is_empty(self):
        return self.items == []

    def pis_empty(self):
        return self.params == {}

    def ppush(self, item, *args):
        self.params[item] = args

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            self.items.pop()

    def ppop(self):
        if not self.is_empty():
            self.params.popitem()

    def __str__(self):
        data = ""
        for i, k in self.params.items():
            data += f'| {i} |'
        return data

    def __getitem__(self, index):
        return self.items[index]

    def exec(self):
        # print('\033[92;1mDone\033[0m')
        for i, k in self.params.items():
            print('\033[96;1m', i.__name__, '\033[0m')
            eval(f'print({i(*k)})')
