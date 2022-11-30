import os
import time
from datetime import datetime
from brute_force import BruteForce

def main():
    files = list()
    with open('dane.ini', 'r') as data:
        files = [line.split(',') for line in data]
    files.pop()

    for file in files:
        BF = BruteForce()
        BF.download_data(file[0])
        st = time.process_time_ns()
        for i in range(int(file[1])):   
            iterations,shortest_paths,len_of_shortest = BF.brute_force_algorithm(0,0)
        en = time.process_time_ns()
        print(f'time: {(en-st)//1000_000} [ms],iterations: {iterations}, lowets path: {shortest_paths}, length of path: {len_of_shortest}')
        BF.upload_data(datetime.now(),(en-st)//1000_000,file[0][file[0].rfind('/')+1:])
    
        

if __name__ == '__main__':
    main()
