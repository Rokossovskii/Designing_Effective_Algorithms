import numpy as np
import csv
from vertex import Vertex
class Branch_and_bound():
    def __init__(self, data_path:str) -> None:
        Branch_and_bound.download_data(self,data_path)
        self.vertex_arr = []
        self.upper_bound = np.inf
    
    def download_data(self,path):
        with open(path,'r') as file:
            self.num_of_vertex = int(file.readline())
            self.matrix = np.array([[float(num) for num in line.split()] for line in file])
            for i in range(self.num_of_vertex):
                self.matrix[i,i] = np.inf

    def find_upper_bound(self):
        starting_ver = Vertex([0],self.matrix, self.num_of_vertex)
        starting_ver.relax_matrix()
        buff = self.expand_level(starting_ver)
        for i in range(self.num_of_vertex-1):
            current_ver = min(buff, key= lambda v:v.prediction)
            buff.remove(current_ver)
            self.expand_level(current_ver)
            self.vertex_arr +=buff
            buff = self.expand_level(current_ver)
        self.upper_bound = current_ver.prediction
        self.vertex_arr.append(current_ver)
        
        self.vertex_arr = list(filter(lambda x: x.prediction <= self.upper_bound, self.vertex_arr))

    def expand_level(self, ver: Vertex) -> list:
        buff = []
        for i in ver.unvisited:
            buff.append(Vertex(ver.path,ver.matrix.copy(),self.num_of_vertex))
            buff[-1].add_destination(i,ver.prediction + ver.matrix[ver.path[-1],i])
            if(buff[-1].prediction > self.upper_bound):
                buff.pop()
        return buff

    def find_shortest_path(self,strategy):
        self.find_upper_bound()
        self.solution = strategy()
        try:
            self.solution.show_matrix_data()
        except:
            print("I can't find a solution")

    def breadth_search(self):
        solution = None
        while(len(self.vertex_arr)):
            current_ver = self.vertex_arr[0]
            if(len(current_ver.path)< self.num_of_vertex):
                self.vertex_arr += self.expand_level(current_ver)
            else:
                if(current_ver.prediction <= self.upper_bound):
                    solution = current_ver
                    self.upper_bound = current_ver.prediction
                    self.vertex_arr = list(filter(lambda x: x.prediction <= self.upper_bound, self.vertex_arr))
            print(current_ver.path)
            self.vertex_arr.pop(0)
        return solution

    def depth_search(self):
        solution = None
        while(len(self.vertex_arr)):
            current_ver = self.vertex_arr.pop()
            if(len(current_ver.path)< self.num_of_vertex):
                self.vertex_arr += self.expand_level(current_ver)
            else:
                if(current_ver.prediction <= self.upper_bound):
                    solution = current_ver
                    self.upper_bound = current_ver.prediction
                    self.vertex_arr = list(filter(lambda x: x.prediction <= self.upper_bound, self.vertex_arr))
            print(current_ver.path)
        return solution

    def low_cost(self):
        solution = None
        while(len(self.vertex_arr)):
            current_ver = min(self.vertex_arr, key= lambda v:v.prediction)
            self.vertex_arr.remove(current_ver)
            if(len(current_ver.path)< self.num_of_vertex):
                self.vertex_arr += self.expand_level(current_ver)
            else:
                if(current_ver.prediction <= self.upper_bound):
                    solution = current_ver
                    self.upper_bound = current_ver.prediction
                    self.vertex_arr = list(filter(lambda x: x.prediction <= self.upper_bound, self.vertex_arr))
            print(current_ver.path)
        return solution
    
    def create_file(strategy_name):
        with open(f'./BranchBound/output/bb_out_{strategy_name}.csv','a') as file:
            csv_writer = csv.writer(file,delimiter=',')
            csv_writer.writerow(['nazwa pliku zrodlowego','czas wykonania[ms]','koszt sciezki','sciezka'])

    def upload_data(self,strategy_name,source_file_name,time):
        with open(f'./BranchBound/output/bb_out_{strategy_name}.csv','a') as file:
            csv_writer = csv.writer(file,delimiter=',')
            csv_writer.writerow([source_file_name,time,self.solution.prediction,self.solution.path])
