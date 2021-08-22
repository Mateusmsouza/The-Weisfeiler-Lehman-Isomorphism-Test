from service_graph import ServiceGraph

service_graph = ServiceGraph()

ISOMORPHIC_GRAPHS = [
    service_graph.create(
        vertex_amount=7,
        edges=[
            [0,1],
            [3,2]
        ]
    ),
    service_graph.create(
        vertex_amount=7,
        edges=[
            [3,2],
            [0,1]
        ]
    )
]

NOT_ISOMORPHIC_GRAPHS_THAT_PASSES_WL = [
    service_graph.create(
        vertex_amount=6,
        edges=[
            [0,1],
            [1,2],
            [2,3],
            [3,4],
            [4,5],
            [5,0]
        ]
    ),
    service_graph.create(
        vertex_amount=6,
        edges=[
            [0,1],
            [1,2],
            [2,0],
            [3,4],
            [4,5],
            [5,3]
        ]
    )
]