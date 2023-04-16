
import heapq
def astar(graph, start,goal):
    open_set = set([start])
    closed_set = set()
    g_scores = {start: 0}
    f_scores = {start: g_scores[start]+heuristic(start,goal)}
    heap = []
    heapq.heappush(heap,(f_scores[start],g_scores[start],[start]))

    while heap:
        current_f_score,current_g_score,path = heapq.heappop(heap)
        current_node = path[-1]


        if(current_node == goal):
            return current_g_score,path
        
        closed_set.add(current_node)
        open_set.remove(current_node)

        for neigbour in graph[current_node].keys():
            if neigbour not in closed_set:
                tentative_g_score = current_g_score + graph[current_node][neigbour]
                if neigbour not in open_set:
                    open_set.add(neigbour)
                elif tentative_g_score > g_scores[neigbour]:
                    continue
                
                g_scores[neigbour] = tentative_g_score
                new_path = path + [neigbour]
                f_scores[neigbour] = tentative_g_score + heuristic(neigbour,goal)
                heapq.heappush(heap,(f_scores[neigbour],g_scores[neigbour],new_path))

    return None,None