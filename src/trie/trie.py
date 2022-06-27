from node import Node

class Trie:
    def __init__(self):
        self.root = Node('_root_', 0)  
        self.tree = {0 : [self.root]}

    def add_node(self, parent_node, child_node):
        assert child_node.parent == None, "The child node already has a parent.";
        assert child_node != self.root, "Root node cannot be chosen as a child node.";
        child_depth = parent_node.depth + 1
        child_node.depth = child_depth

        child_node.parent = parent_node
        parent_node.children.append(child_node)

        if child_depth not in self.tree:
            self.tree[child_depth] = []

        self.tree[child_depth].append(child_node)

    def add_nodes(self, parent_node, child_nodes: list):
        for child_node in child_nodes:
            self.add_node(parent_node, child_node)

    def remove_node(self, node):
        parent_node = node.parent
        parent_node.children.remove(node)

        children = node.children
        for child in children:
            self.remove_node(child)
        self.tree[node.depth].remove(node)
        if self.tree[node.depth] == []:
            del self.tree[node.depth]

    def search(self, key):
        current_node = self.root
        to_search = True
        i = 0
        while i < len(key) and to_search == True:
            character = key[i]
            found = 0
            for child in current_node.children:
                if character == child.value:
                    current_node = child
                    found = 1
                    i+=1
            if found == 0:
                to_search = False
        return i, current_node
    def insert_node(self, key):
        starting_i, starting_node = self.search(key)
        key=key[starting_i:]
        for character in key:
            new_node = Node(character, starting_i+1)
            self.add_node(starting_node, new_node)
            starting_node = new_node

    def delete_node(self, key):
        starting_i, starting_node = self.search(key)
        if starting_i == len(key):
            self.remove_node(starting_node)
        else:
            print("the key cannot be found")

    def predict(self,key):
        starting_i, starting_node = self.search(key)
        prediction = self.traverse_tree_depth_first(starting_node)
        return prediction

    def traverse_tree_depth_first(self, starting_node):
        current_node = starting_node
        list_to_return = []
        to_search = [(c, c.value) for c in current_node.children]
        while len(to_search) > 0:
            to_pop = to_search.pop(0)
            node_to_add = to_pop[0]
            string_value = to_pop[1]
            if len(node_to_add.children) > 0:
                for node in node_to_add.children:
                    to_search.insert(0, (node, string_value+node.value))
            else:
                list_to_return.append(string_value)
        return list_to_return

            
