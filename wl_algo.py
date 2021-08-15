from igraph import *

def run_wl(graph_one: Graph, graph_two: Graph) -> bool:
    """ run wl algo
    
    Args:
        graph_one (Graph): first graph
        graph_two (Graph): second graph

    Returns:
        bool: maybe these graphics are isomorphic
    """
    
    if graph_one.vcount() != graph_two.vcount():
        return False

    __set_all_as_one(graph_one)
    __set_all_as_one(graph_two)
    
    recently_setted_as_one = True
    
    graph_one_vs_count = graph_one.vcount()

    for i in range(graph_one_vs_count):

        for j in range(graph_one_vs_count):
            nodeg1 = graph_one.vs[j]
            nodeg2 = graph_two.vs[j]

            nodeg1['metadata'] = {
                'multiset': [
                    graph_one.vs[x]['name'] for x in graph_one.neighbors(nodeg1)
                ]
            }
            
            nodeg2['metadata'] = {
                'multiset': [
                    graph_two.vs[x]['name'] for x in graph_two.neighbors(nodeg2)
                ]
            }

        multiset_one, multiset_two = __gather_multisets(graph_one, graph_two)

        if multiset_one == multiset_two and not recently_setted_as_one:
            return True
        __recolor_vertex(graph_one)
        __recolor_vertex(graph_two)
        recently_setted_as_one = False

    return False
            
        
def __gather_multisets(graph_one: Graph, graph_two: Graph) -> (list, list):
    """Gather all vertex multisets in a graph in a list for comparision
    purposes.
    
    Args:
        graph_one (Graph): first graph
        graph_two (Graph): second graph

    Returns:
        (list, list): sorted multiset list from graph one and sorted multiset list from graph two
    """

    multiset_list_one = []
    multiset_list_two = []

    for i in range(graph_one.vcount()):
        node_one = graph_one.vs[i]
        node_two = graph_two.vs[i]

        multiset_list_one.append(node_one['metadata']['multiset'])
        multiset_list_two.append(node_two['metadata']['multiset'])

    return sorted(multiset_list_one), sorted(multiset_list_two)

def __recolor_vertex(graph: Graph):
    """recolor each vertex to have their hashed multiset as their new label

    Args:
        graph (Graph): graph to be recolored
    """

    for i in range(graph.vcount()):
        node = graph.vs[i]
        multiset = node['metadata']['multiset']
        node['name'] = abs(hash(str(multiset)))

def __set_all_as_one(graph: Graph) -> None:
    """set all vertex to have label 1 to start first iteration.
    that's inspired in this implementation https://davidbieber.com/post/2019-05-10-weisfeiler-lehman-isomorphism-test/

    Args:
        graph (Graph): graph to be setted to all 1.

    Returns:
        None
    """    
    for node in graph.vs:
        node['name'] = 1