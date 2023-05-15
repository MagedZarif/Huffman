e = open("encoding_input.txt", "r")
text=e.read()
e.close()


probablity = {}
for i in text:
    if i in probablity:
        probablity[i] += 1
    else:
        probablity[i] = 1

probablity = sorted(probablity.items(), key=lambda a: a[1], reverse=True)

nodes = probablity


class nodet():

    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right

    def nodes(self):
        return (self.left, self.right)

    def children(self):
        return (self.left, self.right)

    



def code_tree(node, left=True, code=''):
    if type(node) is str:
        return {node: code}

    (l, r) = node.children()
    n = dict()
    n.update(code_tree(l, True, code + '0'))
    n.update(code_tree(r, False, code + '1'))
    return n





while len(nodes) > 1:
    (key1,c1) = nodes[-1]
    (key2, c2) = nodes[-2]
    nodes = nodes[:-2]
    node = nodet(key1, key2)
    nodes.append((node, c1 + c2))

    nodes = sorted(nodes, key=lambda x: x[1], reverse=True)





huffmanCode = code_tree(nodes[0][0])

s=""
for (char, i) in probablity:
    s=s+(char+ ":"+huffmanCode[char]+" ")

code=""
for i in text:
    if i in huffmanCode:
       code=code+ huffmanCode[i]

d = open("encoding_output.txt", "w")

d.write( '-the table : \n' )

d.write(s+"\n")    
d.write('----------------------\n')
d.write(code)        

d.close()
