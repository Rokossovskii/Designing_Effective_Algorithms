from branch_and_bound import *

import time

def main():
    files = list()
    with open('./BranchBound/test_dane.ini', 'r') as data:
        files = [line.split(',') for line in data]

    # Branch_and_bound.create_file('breadth_search')
    # Branch_and_bound.create_file('depth_search')
    # Branch_and_bound.create_file('low_cost')
    for file in files:
        
        st = time.process_time_ns()
        for i in range(int(file[2].strip('\n'))):
            BB = Branch_and_bound(file[0])
            print('############breadth_search############')
            BB.find_shortest_path(BB.breadth_search)
        en = time.process_time_ns()
        BB.upload_data('breadth_search',file[0],(en - st/int(file[2].strip('\n')))/1000_000)
            
        st = time.process_time_ns()
        for i in range(int(file[2].strip('\n'))):
            BB = Branch_and_bound(file[0])
            print('############depth_search############')
            BB.find_shortest_path(BB.depth_search)
        en = time.process_time_ns()
        BB.upload_data('depth_search',file[0],(en - st/int(file[2].strip('\n')))/1000_000)

        st = time.process_time_ns()
        for i in range(int(file[2].strip('\n'))):
            BB = Branch_and_bound(file[0])
            print('############low_cost############')
            BB.find_shortest_path(BB.low_cost)
        en = time.process_time_ns()
        BB.upload_data('low_cost',file[0],(en - st/int(file[2].strip('\n')))/1000_000)
        

if __name__ == '__main__':
    main()