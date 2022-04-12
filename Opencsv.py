import numpy as np
import csv

cities =[]
sol = []
class open_csv:
    def distance(x,y):
        dist = np.linalg.norm(np.array(x)-np.array(y))
        return dist


    with open('example_solution.csv', mode='r', newline='') as solution:
    
        reader = csv.reader(solution)
        for row in reader:
            sol.append(int(row[0]))
        
        idx = sol.index(0)
        
        front = sol[idx:]
        back = sol[0:idx]
    
        sol = front + back
    
        sol.append(int(0))

    
    with open('TSP.csv', mode='r', newline='') as tsp:
    
        reader = csv.reader(tsp)
        for row in reader:
            cities.append(row)