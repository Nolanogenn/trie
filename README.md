# trie

This repository is dedicated to my implementation of trie structures for Python. This was mainly developed to handle vocabulary search.  

A trie is a type of tree data structure, where each node identifies a string, and edges between nodes represent individual characters. Given a vocabulary, two nodes $n_1$ and $n_2$ are connected by an edge $c_1$ only if $n_1+c_1$ = $n_2$. The resulting structure can traversed depth-first to optimize search in the given vocabulary. 


Our trie structure is initialized as follows:
```
from trie.trie import Trie

T = Trie()
```

Once it is initialized, our structure has only a `_root_` node, which will represent the starting point of all the following nodes. The root node can be accessed through `T.root`, and it cannot have any parent node.

A node is represented by a simple object with a string value (usually a single character), a depth, an identifier, a parent and a list of children. Only the value is needed to initialize a basic node, as follows:
```
a = Node('a')
# this node represents the letter 'a'
```
## Adding Nodes

Nodes can then be inserted in two different ways:

1. manually by using the function `T.add\_node(parent_node, child_node)`

```
T.add_node(T.root, a)

```
this will automatically assign the correct depth to the child node, give it an unique identifier, and update its parent node. Furthermore, the children list for `T.root` are updated as well.

2. automatically using the function `T.insert_string(string)`. In this case, the module will look for the string in the current trie, and the it will insert all the characters that are not present in the structure

```
T.insert_string('alba')
#since the string 'a' is already present in the trie, this function will add nodes representing the strings 'al', 'alb', and 'alba'.

```

## Searching for Strings

You can look for a specific string by using the function `T.search(string)`, which will traverse the trie depth-first and will return the deepest node it can find given the query string. If the node is terminal (i.e., it does not have any children of its own) the string was found successfully.



