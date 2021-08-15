from service_graph import ServiceGraph
from wl_algo import run_wl

def main():
    service_graph = ServiceGraph()
    
    graph_one = service_graph.create(
        vertex_amount=4,
        edges=[
            [0,1],
            [3,2]
        ]
    )
    
    graph_two = service_graph.create(
        vertex_amount=4,
        edges=[
            [3,2],
            [0,1]
        ]
    )
    
    seems_isomorphic = run_wl(graph_one, graph_two)
    if seems_isomorphic:
        print('those looks like isomorphic graphs')
    else:
        print('they arent isomorphic')

    service_graph.plot_graph(graph_one)
    service_graph.plot_graph(graph_two)

if __name__ == '__main__':
    main()
