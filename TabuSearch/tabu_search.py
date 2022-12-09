import random as rd

class TabuSearch():
    def __init__(self,path,seed) -> None:
        self.seed = seed
        self.num_of_vertex,self.graph = self.download_data(path)
        self.best_solition = self.initial_soluion(self.num_of_vertex,self.seed)
        self.best_of_the_best = self.best_solition.copy()
        self.tabu_list = None
        
    
    def download_data(self,path):
        with open(path, 'r') as file:
            num_of_vertex = int(file.readline())
            graph = [[int(num) for num in line.split()] for line in file]
            graph.pop()
        return num_of_vertex,graph

    def initial_soluion(self,num_of_vertex,seed):
        initial_solution = list(range(1, num_of_vertex+1))
        rd.seed(seed)
        rd.shuffle(initial_solution)
        return initial_solution

    def swap(self, solution, i, j):
        solution = solution.copy()

        i_index = solution.index(i)
        j_index = solution.index(j)
        
        solution[i_index], solution[j_index] = solution[j_index], solution[i_index]

    def calculate_path(self,solution):
        distance = 0
        for previous_vertex,vertex in zip([solution[-1]] + solution[-1],solution):
            # TODO
            # suming path

            pass
        return distance