# Represent real life data (Social networking, Family tree, networks, roads routes, recommendations engine)


# Types of Graphs:
    # Directed: specific direction between nodes (Twitter followers)
    # Undirected: (facebook connections)

    # Weighted: info on edges between nodes (google map fastest rout)
    # Unweighted: 

    # Cyclic: path is closed
    # Acyclic: 



# Representing a Graph using three ways:
    # Edge List ==>  graph = [[0,2], [2,3], [2,1], [1,3]]
    # Adjacent List ==>  graph = {0:[2], 1:[2,3], 2:[0,1,3], 3:[1,2]}
    # Adjacent Matrix ==>  graph = {0:[0,0,1,0], 1:[0,0,1,1], 2:[1,1,0,1], 3:[0,1,1,0]}



class Graph():
    nodes_number = 0
    adjacent_list = {}

    def add_vertex(self, value):
        if value in self.adjacent_list:
            self.adjacent_list[value]['count'] += 1
        else:
            self.adjacent_list[value] = {'count':1,'adjacent':[]}
            self.nodes_number += 1

    def add_edge(self, value1, value2):
        is_value1 = (value1 in self.adjacent_list) == True
        is_value2 = (value2 in self.adjacent_list) == True
        if is_value1 and is_value2:
            self.adjacent_list[value1]['adjacent'].append(value2)
            self.adjacent_list[value2]['adjacent'].append(value1)
        else:
            raise IndexError(f'{value1}:{is_value1} {value2}:{is_value2}')

    def show_connections(self):
        for node in self.adjacent_list:
            print(node,'-->',self.adjacent_list[node]['adjacent'])




graph = Graph()

for value in range(7):
    graph.add_vertex(value)

graph.add_edge(0,1)
graph.add_edge(0,2)
graph.add_edge(1,2)
graph.add_edge(1,3)
graph.add_edge(2,4)
graph.add_edge(3,4)
graph.add_edge(5,4)
graph.add_edge(5,6)

print(graph.nodes_number) # 7
graph.show_connections() 

"""
final result ===>
    0 --> [1, 2]
    1 --> [0, 2, 3]
    2 --> [0, 1, 4]
    3 --> [1, 4]   
    4 --> [2, 3, 5]
    5 --> [4, 6]
    6 --> [5]
"""