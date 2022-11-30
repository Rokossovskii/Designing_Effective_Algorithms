import csv
from datetime import datetime


class BruteForce():
    def __init__(self) -> None:
        self.num_of_vertices = 0
        self.len_of_path = 0
        self.iterations = 0
        self.shortest_path = [0,list()]
        self.graph = list()
        self.stack = list()

    def download_data(self,filename):
        with open(filename,'r') as file:
            self.num_of_vertices = int(file.readline())
            self.visited_vertecies = [False for i in range(self.num_of_vertices)]
            self.graph = [[int(num) for num in line.split()] for line in file]
            self.graph.pop()

    def upload_data(self,now:datetime ,time_spend,source_file_name):
        with open(f'./dane/bf_out_{now.day}-{now.month}.csv','a') as file:
            csv_writer = csv.writer(file,delimiter=',')
            csv_writer.writerow(['nazwa pliku zrodlowego','ilosc iteracji','czas wykonania[ms]','koszt sciezki','sciezka'])
            csv_writer.writerow([source_file_name,self.iterations,time_spend,self.shortest_path[0],self.shortest_path[1]])
            


    def get_num_of_vercities(self):
        return self.num_of_vertices

    def brute_force_algorithm(self,current_vertex:int,privious_vertex:int):
        self.iterations += 1                                                    #Zlicznaie wykonanych iteracji
        self.stack.append(current_vertex)                                       #Wrzucanie na stos wierzchołka w którym obecnie sie znajdujemy   

        if(len(self.stack)<self.num_of_vertices):                               #Sprawdzenie czy nie mamy już maksymalnej liczby wierzchołków na stosie 

            self.visited_vertecies[current_vertex] = True                       #Zaznaczanie obecnego wierzchołka jako odwiedzony oraz dodawanie nowej długości drogi do scieżki
            self.len_of_path += self.graph[privious_vertex][current_vertex]     

            for index,visited in enumerate(self.visited_vertecies):             #Wybór następnego wierzchołka do odwiedzenia oraz jego wybór
                if(not visited):                                                                                                
                    self.brute_force_algorithm(index,current_vertex)

            self.visited_vertecies[current_vertex] = False                      #Odznaczanie obecnego wierzchołka jako odwiedzonego, usuwanie krawędzi do niego prowadzącego oraz usuwanie go ze stosu
            self.len_of_path -= self.graph[privious_vertex][current_vertex] 
            self.stack.pop()

        else:                                                                   #Jeżeli kod wchodzi w ten etap oznacza ze przeszedł juz wszystkie wierzchołki i musi wrócić do wierzchołka startowego

            final_path_length = self.len_of_path + self.graph[privious_vertex][current_vertex] + self.last_path(current_vertex)
            self.stack.append(self.stack[0])
            final_path_length -= self.graph[0][0]   
            self.choose_shortest_path(final_path_length)                        #Sprawdzanie czy obecna scieżka jest najkrótszą jak dotąd
            self.stack.pop()
            self.stack.pop()            
        
        return self.iterations,self.shortest_path[0],self.shortest_path[1]

    def choose_shortest_path(self, pt_len:int):
        #print(pt_len,self.stack)
        if(self.shortest_path[0] > pt_len or self.shortest_path[0] == 0): self.shortest_path = [pt_len,self.stack.copy()]

    def last_path(self,cur_ver):
        try:
            return self.graph[cur_ver][self.stack[0]]
        except:
            return 0

