class UDGraph:
    def __init__(self):
        self.graph = dict()

    def addVertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []

    def addEdge(self, from_vertex, to_vertex):
        # Auto-create vertices if they don't exist
        if from_vertex not in self.graph:
            self.addVertex(from_vertex)

        if to_vertex not in self.graph:
            self.addVertex(to_vertex)

        # Add directed edge (from_vertex -> to_vertex)
        if to_vertex not in self.graph[from_vertex]:
            self.graph[from_vertex].append(to_vertex)

    def listOutgoingAdjacentVertex(self, vertex):
        if vertex in self.graph:
            return self.graph[vertex]
        return []

    def listIncomingAdjacentVertex(self, vertex):
        incoming = []
        for v in self.graph:
            if vertex in self.graph[v]:
                incoming.append(v)
        return incoming

    def print_graph(self):
        print("\n=== Network Graph ===")
        for vertex in self.graph:
            print(f"{vertex} -> {self.graph[vertex]}")
        print("=" * 40)