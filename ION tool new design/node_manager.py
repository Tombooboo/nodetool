class Node:
    def __init__(self, name, ip):
        self.name = name
        self.ip = ip
        
class NodeManager:
    def __init__(self):
        self.nodes = []
        self.edges = []

    def add_node(self, name, ip):
        node = Node(name, ip)
        self.nodes.append(node)


    def remove_node(self, node):
        self.nodes.remove(node)
        self.remove_edges_related_to_node(node)

    def modify_node(self, node, new_node):
        index = self.nodes.index(node)
        self.nodes[index] = new_node
        self.modify_edges_related_to_node(node, new_node)

    def add_edge(self, source, target):
        self.edges.append((source, target))

    def remove_edge(self, source, target):
        self.edges.remove((source, target))

    def get_node_info(self):
        return self.nodes

    def get_edges(self):
        return self.edges

    def remove_edges_related_to_node(self, node):
        self.edges = [(source, target) for source, target in self.edges if source != node and target != node]

    def modify_edges_related_to_node(self, node, new_node):
        self.edges = [(new_node if source == node else source, new_node if target == node else target)
                      for source, target in self.edges]
