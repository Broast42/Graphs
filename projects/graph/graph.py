"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        if vertex_id not in self.vertices:
            self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # Create an empty queue and enqueue the starting_vertex
        queue = Queue()
        queue.enqueue(starting_vertex) 
        # Create an empty set to track visited verticies
        visited = set()
        # while the queue is not empty:
        while queue.size() != 0:
            # get current vertex (dequeue from queue)
            current = queue.dequeue()
            # Check if the current vertex has not been visited:
            if current not in visited:
                # print the current vertex
                print(current)
                # Mark the current vertex as visited
                    # Add the current vertex to a visited_set
                visited.add(current)     
                # queue up all the current vertex's neighbors (so we can visit them next)
                neighbors = self.get_neighbors(current)
                for i in neighbors:
                    queue.enqueue(i)

        

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """

        # Create an empty stack and add the starting_vertex
        s = Stack()
        s.push(starting_vertex) 
        # Create an empty set to track visited verticies
        visited = set()

        # while the stack is not empty:
        while s.size() != 0:
            # get current vertex (pop from stack)
            current = s.pop()

            # Check if the current vertex has not been visited:
            if current not in visited:
                # print the current vertex
                print(current)
                # Mark the current vertex as visited
                    # Add the current vertex to a visited_set
                visited.add(current)

                #push up all the current vertex's neighbors (so we can visit them next
                neighbors = self.get_neighbors(current)
                
                for i in neighbors:
                    s.push(i)

    dft_r_visited = set()    

    def dft_recursive(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        if starting_vertex not in self.dft_r_visited:
            print(starting_vertex)
            self.dft_r_visited.add(starting_vertex)
            neighbors = self.get_neighbors(starting_vertex)
            for i in neighbors:
                self.dft_recursive(i)
        

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # Create an empty queue and enqueue the PATH TO starting_vertex
        q = Queue()
        q.enqueue([1]) 
        # Create an empty set to track visited verticies
        visited = set()
        # while the queue is not empty:
        while q.size() != 0:
            # get current vertex PATH (dequeue from queue)
            current_paths = q.dequeue()
            
            # set the current vertex to the LAST element of the PATH
            current = current_paths[-1]
            
            # Check if the current vertex has not been visited:
            if current not in visited:
                
                # CHECK IF THE CURRENT VERTEX IS DESTINATION
                if current == destination_vertex:
                    # IF IT IS, STOP AND RETURN
                    return current_paths

                # Mark the current vertex as visited
                    # Add the current vertex to a visited_set
                visited.add(current)

                neighbors = self.get_neighbors(current)
                # Queue up NEW paths with each neighbor:
                
                for i in neighbors:
                    # take current path
                    new_path = []
                    new_path = new_path + current_paths
                    new_path.append(i)
                    
                    # append the neighbor to it
                    # queue up NEW path
                    q.enqueue(new_path)
        

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # Create an empty stack and enqueue the PATH TO starting_vertex
        s = Stack()
        s.push([starting_vertex]) 
        # Create an empty set to track visited verticies
        visited = set()
        # while the queue is not empty:
        while s.size() != 0:
            # get current vertex PATH (dequeue from queue)
            current_paths = s.pop()
            
            # set the current vertex to the LAST element of the PATH
            current = current_paths[-1]
            
            # Check if the current vertex has not been visited:
            if current not in visited:
                
                # CHECK IF THE CURRENT VERTEX IS DESTINATION
                if current == destination_vertex:
                    # IF IT IS, STOP AND RETURN
                    return current_paths

                # Mark the current vertex as visited
                    # Add the current vertex to a visited_set
                visited.add(current)

                neighbors = self.get_neighbors(current)
                # Queue up NEW paths with each neighbor:
                
                for i in neighbors:
                    # take current path
                    new_path = []
                    new_path = new_path + current_paths
                    new_path.append(i)
                    
                    # append the neighbor to it
                    # queue up NEW path
                    s.push(new_path)
    
    dfs_r_path = []
    dfs_r_visited = set()

    def dfs_recursive(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
       

        if isinstance(starting_vertex, list) is False:
            starting_vertex = list([starting_vertex])

        if starting_vertex[-1] == destination_vertex:
            self.dfs_r_path = starting_vertex
            
        
        if starting_vertex[-1] not in self.dfs_r_visited:
            self.dfs_r_visited.add(starting_vertex[-1])
            neighbors = self.get_neighbors(starting_vertex[-1])
            
            for i in neighbors:
                
                new_path = list(starting_vertex)
                new_path.append(i)
                
                self.dfs_recursive(new_path, destination_vertex)

        return self.dfs_r_path
        

if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)
    print("")

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    print('')
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print("")
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print("")
    print(graph.dfs(1, 6))
    print("")
    print(graph.dfs_recursive(1, 6))
