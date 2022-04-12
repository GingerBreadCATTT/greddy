
import numpy as np
import csv

cities =[]
sol = []

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
        
node_cnt = 1000 #노드 개수
inf = 10000000
total_cost = 0

best_node = 0
best_dist = 0
temp_dist = 0

cnt = 0
used_node_cnt = 1
token = 0

used_node = []
i = 0 
j = 0
k = 0

print(idx)
start_city = [float(cities[sol[idx]][0]), float(cities[sol[idx]][1])]
used_node.append(idx)

while True:#greedy: 가장 가까운 노드를 다음 노드로 삼는다
    best_dist = inf
    temp_dist = 0
    token = 0
    
    pos_city_1 = [float(cities[sol[idx]][0]), float(cities[sol[idx]][1])]
    
    i = 0
    k = 0
    cnt = 1
    idx_cnt = 0

        
    while True:#다음 노드를 결정하는 루프문
             
        
        if cnt == node_cnt:#자기자신으로 돌아오면 루프문을 탈출한다
            break

        idx_cnt = idx + cnt#현재 노드에서 cnt만큼 떨어진 노드
            
        if idx + cnt > node_cnt - 1:
            idx_cnt = idx + cnt - node_cnt #노드가 node_cnt를 넘어가면 0으로 돌아간다
            
        token = 0
            
        for i in range(used_node_cnt):#사용된 노드가 감지되면 token 값을 1 올린다
                if used_node[i] == idx_cnt:
                    token += 1
                else:
                    token += 0#idx_cnt가 사용된 노드가 아닐경우 token은 0이다
            
        if token == 0:#위 for문에 의해 사용된 노드면 건너뛰고 if문을 실행한다
            temp_city = [float(cities[sol[idx_cnt]][0]), float(cities[sol[idx_cnt]][1])]
            temp_dist = distance(pos_city_1, temp_city)
        
            if best_dist > temp_dist:#현재까지 결정된 가장 가까운 노드보다 이번 노드가 가까우면 작동한다
                best_dist = temp_dist#이번 거리를 가장 가까운 거리로 설정한다
                best_node = idx_cnt#이번 노드를 가장 가까운 노드로 설정한다
        
        cnt+=1
        
    dist = best_dist
    
    total_cost += dist
    
    print(best_node)#결정된 노드의 순서를 볼 수 있다

    idx = best_node#가장 가까운 노드를 현재노드로 설정한다

    used_node.append(best_node)#가장 가까운 노드를 사용한 노드에 추가한다
    used_node_cnt += 1#사용한 노드 개수에 +1한다
    
    if used_node_cnt == 1000:#사용한 노드가 1000개가 되면 greedy를 종료하고 결과를 표시한다.
        break

last_city = [float(cities[sol[best_node]][0]), float(cities[sol[best_node]][1])]
last_dist = distance(start_city, last_city)
#print(start_city, last_city, last_dist)

total_cost += last_dist#마지막노드에서 출발점으로 돌아오는 거리를 추가한다

print('\n')        
print('final cost: '+str(total_cost))