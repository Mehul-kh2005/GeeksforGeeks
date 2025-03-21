#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math


# } Driver Code Ends
#User function Template for python3
class Solution:
    def findTriplets(self, arr):
        elements_set=set()
        n=len(arr)
        freq_map={}
        
        for i in range(n):
            for j in range(i+1,n):
                s=arr[i]+arr[j]
                
                if s not in freq_map:
                    freq_map[s]=[]
                    
                freq_map[s].append((i,j))
                
        for i in range(n):
            rem=-arr[i]
            if rem in freq_map:
                for value in freq_map[rem]:
                    
                    if value[0]!=i and value[1]!=i:
                        current=sorted([i,value[0],value[1]])
                        elements_set.add(tuple(current))
                        
        return [list(triplet) for triplet in elements_set]

#{ 
 # Driver Code Starts.

def main():
    T = int(input())
    while (T > 0):

        A = [int(x) for x in input().strip().split()]

        ob = Solution()
        res = ob.findTriplets(A)
        res = sorted(res)
        if len(res) == 0:
            print('[]')
        for i in range(len(res)):
            for j in range(len(res[i])):
                print(res[i][j], end=" ")
            print("")
        print('~')
        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends