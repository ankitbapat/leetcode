class Solution():
    
    def canApplyColorToNode(self, c, n, node_to_color):
        for e in edges[n]:
            # Check if adjacent node has the same color
            if e in node_to_color and node_to_color[e]==c: return False
        return True 
    
    def fun(self, node, node_to_color):
        if node==N: return True
        for c in range(M):
            if self.canApplyColorToNode(c, node, node_to_color):
                node_to_color[node]=c
                if self.fun(node+1, node_to_color): 
                    return True
        return False

    
sol=Solution()
# N=4
# M=3
# E=5
# edges_set = {  
#   (0, 1),  
#   (1, 2),  
#   (2, 3),  
#   (3, 0),  
#   (0, 2)  
# }
N = 3  
M = 2  
E = 3  
edges_set = {  
  (0, 1),  
  (1, 2),  
  (0, 2)  
}  

edges = {i:[] for i in range(N)}
for u, v in edges_set:
    edges[u].append(v)
    edges[v].append(u)

print(sol.fun(0,{},))

# time:- O(C^N) - C number of colors. N number of nodes
# space:- O(N) - depth of rec stack -> length of nodes