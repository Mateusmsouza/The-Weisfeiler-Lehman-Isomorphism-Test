from igraph import *

def run_wl(graph_one: Graph.Tree, graph_two: Graph.Tree) -> bool:
    
    __set_all_as_one(graph_one)
    __set_all_as_one(graph_two)
    
    for i in range(graph_one.vcount()):
        nodeg1 = graph_one.vs[i]
        nodeg2 = graph_one.vs[i]
        
        nodeg1['L'] = {
            'label': nodeg1['name'],
            'multiset': graph_one.neighbors(nodeg1)
        }
        
        nodeg2['L'] = {
            'label': nodeg2['name'],
            'multiset': graph_one.neighbors(nodeg2)
        }
        print(nodeg1['L'])
        print(nodeg2['L'])

def __set_all_as_one(graph: Graph.Tree) -> Graph.Tree:
    for node in graph.vs:
        node['name'] = 1