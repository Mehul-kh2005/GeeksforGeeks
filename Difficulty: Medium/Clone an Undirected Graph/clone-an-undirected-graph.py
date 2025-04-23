from collections import deque

'''
class Node:
    def __init__(self, val = 0, neighbors = []):
        self.val = val
        self.neighbors = neighbors
'''

class Solution():
    def cloneGraph(self, node):
        if node is None:
            return None
            
        mapClone={}
        mapClone[node]=Node(node.val)
        
        queue=deque([node])
        
        while queue:
            currNode=queue.popleft()
            
            for neighbor in currNode.neighbors:
                if neighbor not in mapClone:
                    mapClone[neighbor]=Node(neighbor.val)
                    queue.append(neighbor)
                    
                mapClone[currNode].neighbors.append(mapClone[neighbor])
                
        return mapClone[node]

#{ 
 # Driver Code Starts
#Initial Template for Python 3

from queue import Queue
import sys

sys.setrecursionlimit(10**6)


class Node:

    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


def compare(prev, new, prev_vis=set(), new_vis=set()):
    if prev == new:
        return False
    if not prev or not new:
        if (not prev and new) or (prev and not new):
            return False
        return True

    if prev in prev_vis or new in new_vis:
        if (prev in prev_vis and new not in new_vis) or (prev not in prev_vis
                                                         and new in new_vis):
            return False
        return True
    prev_vis.add(prev)
    new_vis.add(new)

    if prev.val != new.val:
        return False

    prev_n = len(prev.neighbors)
    new_n = len(new.neighbors)
    if prev_n != new_n:
        return False

    prev.neighbors.sort(key=lambda x: x.val)
    new.neighbors.sort(key=lambda x: x.val)
    for i in range(prev_n):
        if not compare(prev.neighbors[i], new.neighbors[i], prev_vis, new_vis):
            return False

    return True


if __name__ == "__main__":
    for _ in range(int(input())):
        N = int(input())
        v = [Node(i) for i in range(N)]
        for i in range(N):
            v[i].neighbors = [v[int(x)] for x in input().split()]
        ob = Solution()
        ans = ob.cloneGraph(v[0])
        print("true" if compare(v[0], ans) else "false")
        print("~")

# } Driver Code Ends