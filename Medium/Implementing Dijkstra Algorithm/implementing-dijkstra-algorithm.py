import heapq
class Solution:

    #Function to find the shortest distance of all the vertices
    #from the source vertex S.
    def dijkstra(self, V, adj, S):
        # Create adjacency list
        # (Assuming adj is a list of lists where each inner list represents the neighbors and weights of a vertex)
        # Example: adj = [[(1, 2), (2, 4)], [(0, 2), (2, 1)], [(0, 4), (1, 1)]]
        # means vertex 0 is connected to vertices 1 and 2 with weights 2 and 4, and so on.
        adj_list = [[] for _ in range(V)]
        for i, neighbors in enumerate(adj):
            adj_list[i].extend(neighbors)

        # Initialize distance array with infinity
        dist = [float('inf')] * V

        # Priority queue to store (distance, vertex) pairs
        pq = [(0, S)]
        dist[S] = 0

        while pq:
            cur_dist, cur_vertex = heapq.heappop(pq)

            for neighbor, weight in adj_list[cur_vertex]:
                new_dist = cur_dist + weight
                if new_dist < dist[neighbor]:
                    dist[neighbor] = new_dist
                    heapq.heappush(pq, (new_dist, neighbor))

        return dist
        #code here

        




#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        V,E = map(int,input().strip().split())
        adj = [[] for i in range(V)]
        for i in range(E):
            u,v,w = map(int,input().strip().split())
            adj[u].append([v,w])
            adj[v].append([u,w])
        S=int(input())
        ob = Solution()
        
        res = ob.dijkstra(V,adj,S)
        for i in res:
            print(i,end=" ")
        print()
# } Driver Code Ends