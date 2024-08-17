'''
An unweighted, undirected Graph class based on an adjaceny list model.
'''
class Graph:
    def __init__(self, adjacency_list:dict[str, set[str]]):
        '''The Graph class constructor.
          Inititalizes the following data attributes:
            - self.__adjacency_list (dict[str, st[str]]): An adjaceny list model of our Graph
            - self.__vertices (set[str]): A set of all the vertices in the graph
            - self.__edges (set[tuple[str]]]): A set of tuples representing all the edges int the graph 

            Args:
              adjacency_list (dict[str, set[str]]): An adjaceny list model of our Graph
        '''
        self.__adjacency_list = adjacency_list
        self.__vertices = set(adjacency_list.keys())
        self.__edges = set()

        for vertex, neighbors in adjacency_list.items():
            for neighbor in neighbors:
                self.__edges.add(tuple(sorted((vertex, neighbor))))
    
  
    @property
    def vertices(self):
      '''Accessor method for the vertices attribute'''
      return self.__vertices

    @property
    def edges(self):
      '''Accessor method for the edges attribute'''
      return self.__edges
    
    def is_vertex(self, vertex:str) -> bool:
       '''Determines whether a vertex is present on the graph'''

       return vertex in self.__vertices


    def get_neighbors(self, vertex:str) -> set[str]:
        '''Accessor method for the neighbors of an edge

            Args:
              vertex (str): The given vertex

            Returns:
              set[str] : A set of strings representing all the neighbors of the vertex
        '''

        if vertex not in self.vertices:
           return set()
        else:
           return self.__adjacency_list.get(vertex, set())

    
    def is_valid_path(self, path:tuple[str]) -> bool:
       ''' Determines whether a given path is a valid path on the graph

          Args:
            path (tuple[str]): A list of path vertices

          Returns:
            bool - True if the given path is a valid path on the Graph, otherwise False
       '''

       for i in range(len(path) - 1):
          if path[i] not in self.__adjacency_list:
            return False
       return True


    def get_shortest_bfs_path(self, start:str, target:str) -> tuple[str]:
        ''' Finds a shortest paths connecting the start vertex with the target vertex.

          Args:
            start: the starting vertex in the path
            target: the last vertex in the path

          Returns:
           tuple[str] - a tuple of str vertivces representing a shortest path from start node to target node
        '''
        path_queue = [[start]]
   
        while path_queue:
            old_path = path_queue.pop(0)
            last_node = old_path[-1]

            for neighbour in self.get_neighbors(last_node):
                if neighbour not in old_path:
                    new_path = old_path.copy()
                    new_path.append(neighbour)
                    path_queue.append(new_path)
        
                if neighbour == target:
                    return tuple(new_path)
        
        return tuple()

    def get_shortest_bfs_path_length(self, start:str, target:str) -> int:
        ''' Finds the number of edges in the shortest path generated by bfs connecting
            the start vertex with the target vertex.

          Args:
            start: the starting vertex in the path
            target: the last vertex in the path

          Returns:
            int - the number of edges traversed to get from source to target in the shortest bfs path
                  invalid paths result in a path length of 0
        '''

        shortest_path = self.get_shortest_bfs_path(start, target)
        if shortest_path: 
          return len(shortest_path) - 1 
        else:
          return 0


    def get_all_shortest_bfs_paths(self, source:str, target:str) -> set[tuple[str]]:
        ''' Finds all of the shortests paths connecting the start vertex with the target vertex.

          Args:
            start: the starting vertex in the path
            target: the last vertex in the path

          Returns:
            set[tuple[str]] - a set of tuples of str vertivces representing all of the shortest paths
                             from start node to target node
        '''

        paths = set()
        path_queue = [[source]]
        min_length = float('inf')

        while path_queue:
            current_path = path_queue.pop(0)
            last_node = current_path[-1]

            for neighbor in self.get_neighbors(last_node):
                if neighbor not in current_path:
                    new_path = current_path + [neighbor]
                    if neighbor == target:
                        if len(new_path) <= min_length:
                            min_length = len(new_path)
                            paths.add(tuple(new_path))
                    else:
                        path_queue.append(new_path)
        
        return {path for path in paths if len(path) == min_length}


if __name__ == "__main__":
  binary_tree_graph ={
       'A':{'B'},
       'B':{'F','A','D'},
       'C':{'D'},
       'D':{'B','C','E'},
       'E':{'D'},
       'F':{'B', 'G'},
       'G':{'F','I'},
       'H':{'I'},
       'I':{'G', 'H'}
    }
  myGraph = Graph(binary_tree_graph)
  print("Vertices:", myGraph.vertices)
  print("Edges:", myGraph.edges)  
  vertex = "F"
  print(f"Neighbers ({vertex}):", myGraph.get_neighbors(vertex))
  good_path=["F", "B", "D", "C"]
  bad_path=["F", "B", "D", "I"]
  print(f"Valid Path {good_path}:", myGraph.is_valid_path(good_path))
  print(f"Invalid Path {bad_path}:", myGraph.is_valid_path(bad_path))
  start = "H"
  target= "C"
  print(f"Shortest Path from {start} to {target}:", myGraph.get_shortest_bfs_path(start, target))
  print(f"Shortest Path Length from {start} to {target}:", myGraph.get_shortest_bfs_path_length(start, target))

  print("--------------------------")
  small_dictionary={
       "foul":{"fool", "foil"},
       "fool":{"foul", "foil", "cool", "pool"},
       "cool":{"fool", "pool"},
       "pool":{"fool", "poll"},
       "poll":{"pool", "pall", "pole"},
       "pole":{"poll", "pale", "pope"},
       "pope":{"pole"},
       "pale":{"pole","pall","page","sale"},
       "sale":{"pale","sage"},
       "sage":{"sale","page"},
       "page":{"pale", "sage"},
       "pall":{"poll", "pale", "fall"},
       "fall":{"fail","pall"},
       "fail":{"fall","foil"},
       "foil":{"foul", "fail"}
     }
  myGraph2 = Graph(small_dictionary)
  print("Vertices:", myGraph2.vertices)
  print("Edges:", myGraph2.edges)  
  vertex = "foil"
  print(f"Neighbers ({vertex}):", myGraph2.get_neighbors(vertex))
  good_path=["pope", "pole", "pale", "page"]
  bad_path=["F", "B", "D", "I"]
  print(f"Valid Path {good_path}:", myGraph2.is_valid_path(good_path))
  print(f"Invalid Path {bad_path}:", myGraph2.is_valid_path(bad_path))
  start = "fool"
  target= "sage"
  print(f"Shortest Path from {start} to {target}:", myGraph2.get_shortest_bfs_path(start, target))
  print(f"Shortest Path Length from {start} to {target}:", myGraph2.get_shortest_bfs_path_length(start, target))
