class Node:
    def __init__(self, value, depth=0, parent= None):
        self.parent = parent
        self.children = []
        self.value = value
        self.depth = depth

    def __str__(self):
        return f"""NodeObject(value: {self.value}, depth: {self.depth}, children:{len(self.children)})"""
    def __repr__(self) :
        return f"""NodeObject(value: {self.value}, depth: {self.depth}, children: {len(self.children)})"""

