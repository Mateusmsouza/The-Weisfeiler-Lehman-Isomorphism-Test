from wl_algo import run_wl
from service_graph import ServiceGraph
from data.graphs import ISOMORPHIC_GRAPHS, NOT_ISOMORPHIC_GRAPHS_THAT_PASSES_WL

def main():
    service_graph = ServiceGraph()
    graph_one, graph_two = ISOMORPHIC_GRAPHS[0], ISOMORPHIC_GRAPHS[1]
    
    seems_isomorphic = run_wl(graph_one, graph_two)
    if seems_isomorphic:
        print('those looks like isomorphic graphs')
    else:
        print('they arent isomorphic')

    service_graph.plot_graph(graph_one)
    service_graph.plot_graph(graph_two)

if __name__ == '__main__':
    main()
