
class Solution(object):
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        def dfs(node, visited, M):
            for v in range(len(M[node])):
                if M[node][v] == 1 and visited[v] == 0:
                    visited[v] = 1
                    dfs(v, visited, M)
        
        visited = [0]*len(M)
        cnt = 0        
        for node in range(len(visited)):
            if visited[node] == 0:
                cnt += 1
                dfs(node, visited, M)
                
        return cnt
