from service_graph import ServiceGraph
from wl_algo import run_wl

if __name__ == '__main__':
    graph_one = ServiceGraph().create(
        vertex_amount=4,
        edges=[
            [0,1],
            [3,2]
        ]
    )
    
    graph_two = ServiceGraph().create(
        vertex_amount=4,
        edges=[
            [3,2],
            [0,1]
        ]
    )    
    run_wl(graph_one, graph_two)