from node import Node
from trie import Trie

t = Node('t')
a = Node('a')
e = Node('e')
s = Node('s')
t2 = Node('t')


T = Trie()
T.insert_node('test')
T.insert_node('tamarindo')
T.insert_node('tamarro')

tree = T.tree
#for depth in tree:
#    print(depth, [x.value for x in tree[depth]])

T.predict('ta')
