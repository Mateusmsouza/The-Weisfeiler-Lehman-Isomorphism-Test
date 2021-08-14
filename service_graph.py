from igraph import *

class ServiceGraph:

    def create(self, vertex_amount: int, edges: list) -> Graph:
        return Graph(
            n=vertex_amount,
            edges=edges
        )
    
    def plot_graph(self, graph: Graph):
        plot(
            graph,
            layout=graph.layout('kk')
        )