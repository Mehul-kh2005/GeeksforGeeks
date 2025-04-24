from collections import deque

class Solution:
    def findOrder(words):
        n=len(words)
        adjList=[[] for _ in range(26)]
        
        indegree=[0]*26
        exists=[False]*26
        
        for word in words:
            for char in word:
                exists[ord(char)-ord('a')]=True
                
        for i in range(n-1):
            word1,word2=words[i],words[i+1]
            min_len=min(len(word1),len(word2))
            j=0
            
            while j<min_len and word1[j]==word2[j]:
                j+=1
                
            if j<min_len:
                u=ord(word1[j])-ord('a')
                v=ord(word2[j])-ord('a')
                
                adjList[u].append(v)
                indegree[v]+=1
                
            elif len(word1)>len(word2):
                return ""
              
                
        queue=deque([i for i in range(26) if exists[i] and indegree[i]==0])
        result=[]
        
        while queue:
            u=queue.popleft()
            result.append(chr(u+ord('a')))
            
            for v in adjList[u]:
                indegree[v]-=1
                
                if indegree[v]==0:
                    queue.append(v)
                    
        if len(result)!=sum(exists):
            return ""
            
        return "".join(result)

#{ 
 # Driver Code Starts
#Initial Template for Python 3
import sys
from collections import deque

#Position this line where user code will be pasted.


def validate(original, order):
    char_map = {}
    for word in original:
        for ch in word:
            char_map[ch] = 1

    for ch in order:
        if ch not in char_map:
            return False
        del char_map[ch]

    if char_map:
        return False

    char_index = {ch: i for i, ch in enumerate(order)}

    for i in range(len(original) - 1):
        a, b = original[i], original[i + 1]
        k, n, m = 0, len(a), len(b)
        while k < n and k < m and a[k] == b[k]:
            k += 1
        if k < n and k < m and char_index[a[k]] > char_index[b[k]]:
            return False
        if k != n and k == m:
            return False

    return True


if __name__ == "__main__":
    input_data = sys.stdin.read().strip().split("\n")
    index = 0
    t = int(input_data[index])
    index += 1
    while t > 0:
        words = input_data[index].split()
        index += 1
        original = words[:]

        order = Solution.findOrder(words)

        if order == "":
            print("\"\"")
        else:
            print("true" if validate(original, order) else "false")
        print("~")
        t -= 1

# } Driver Code Ends