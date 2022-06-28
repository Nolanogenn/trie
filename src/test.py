from trie.node import Node
from trie.trie import Trie


t = Node('t')
a = Node('a')
e = Node('e')
s = Node('s')
t2 = Node('t')


T = Trie()
T.insert_string('test')
T.insert_string('tamarindo')
T.insert_string('tamarro')

tree = T.tree
#for depth in tree:
#    print(depth, [x.value for x in tree[depth]])


x = T.search('tam')
print(x)
