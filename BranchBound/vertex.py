import numpy as np

class Vertex():
    def __init__(self,p, matrix, num) -> None:
        self.path = []
        self.path += p
        self.unvisited = [x for x in range(num) if x not in self.path]
        self.prediction = 0
        self.matrix = matrix
        self.num_of_vertex = num

    def relax_matrix(self):
        r = 0

        for i in range(self.num_of_vertex):
            r = min(self.matrix[:,i])
            if(r != np.inf): 
                self.prediction += r
                self.matrix[:,i] = self.matrix[:,i] - r

        for i in range(self.num_of_vertex):
            r = min(self.matrix[i,:])
            if(r != np.inf):  
                self.prediction += r  
                self.matrix[i,:] = self.matrix[i,:] - r      
    
    def add_destination(self,x,cost):
        self.prediction += cost
        self.path.append(x)
        self.unvisited.remove(x)
        self.obscuring_the_matrix(self.path[-2],self.path[-1])
        self.relax_matrix()

    def obscuring_the_matrix(self, x,y):
        self.matrix[x,:] = np.inf
        self.matrix[:,y] = np.inf
        self.matrix[y,x] = np.inf

    def show_matrix_data(self):
        print(f'\n{self.path}\n{self.prediction}\n')