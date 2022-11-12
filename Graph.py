class Graph:
    def __init__(self, edges):
        self.edges = edges
        self.graph_dict = {}
        for start, end in edges:
            if start in self.graph_dict:
                self.graph_dict[start].append(end)
            else:
                self.graph_dict[start] = [end]
        print("Graph dict : ",self.graph_dict)

    def get_path(self, start, end, path=[]):
        path = path + [start]
        if start is end:
            return [path]
        if start not in self.graph_dict:
            return []
        paths = []
        for node in self.graph_dict[start]:
            if node not in path:
                new_path  = self.get_path(node, end, path)
                for p in new_path:
                    paths.append(p)
        return paths

    def get_shorted_path(self, start, end, path=[]):
        path  = path + [start]
        if start is end:
            return path
        if start not in self.graph_dict:
            return None
        shorted_path = None
        for node in self.graph_dict[start]:
            if node not in path:
                sp = self.get_shorted_path(node, end, path)
                if sp:
                    if shorted_path is None or len(sp) < len(shorted_path):
                        shorted_path = sp
        return shorted_path

if __name__ == '__main__':
    routes = [
        ("Mumbai", "Pune"),
        ("Mumbai", "Surat"),
        ("Surat", "Bangaluru"),
        ("Pune", "Hyderabad"),
        ("Pune", "Mysuru"),
        ("Hyderabad", "Bangaluru"),
        ("Hyderabad", "Chennai"),
        ("Mysuru", "Bangaluru"),
        ("Chennai", "Bangaluru")
    ]

    route_graph = Graph(routes)
    sart = "Mumbai"
    end = "Bangaluru"

    print(f"All paths between {sart} to {end} :",route_graph.get_path(sart, end))
    print(f"Shortest path between {sart} and {end} : ",route_graph.get_shorted_path(sart, end))


