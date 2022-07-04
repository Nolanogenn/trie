class Node:
    def __init__(self, value, depth=0, identifier=0, parent= None, is_terminal=False):
        self.parent = parent
        self.children = []
        self.value = value
        self.depth = depth
        self.identifier = identifier
        self.is_terminal=is_terminal

    def __str__(self):
        return f"""NodeObject(value: {self.value}, depth: {self.depth}, identifier:{self.identifier}, is_terminal: {self.is_terminal})"""
    def __repr__(self) :
        return f"""NodeObject(value: {self.value}, depth: {self.depth}, identifier: {self.identifier}, is_terminal: {self.is_terminal})"""

